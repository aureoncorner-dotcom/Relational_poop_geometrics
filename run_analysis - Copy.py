"""Retrospective multi-coordinate audit; reads originals, writes this directory only."""
import collections as C
import datetime as dt
import hashlib
import json
import pathlib
import re
import statistics

HERE = pathlib.Path(__file__).resolve().parent
ROOT = pathlib.Path(r'C:\Users\drewd\Downloads\audits')
def read(p):
    return json.loads(p.read_text(encoding='utf-8-sig'))
def save(name, obj):
    (HERE / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
data = {k: read(ROOT / (k + '.json')) for k in ['nodes','events','candidates','evidence_table']}
table = data['evidence_table']
cases = {s['case'] for s in table['sources']}
nodes = [n for n in data['nodes'] if n['case'] in cases]
index = {(n['case'], n['node']): n for n in nodes}
events = table['events']
event_index = {(e['case'], e['node']): e for e in events}
bycase = C.defaultdict(list)
for n in nodes:
    bycase[n['case']].append(n)
for rows in bycase.values():
    rows.sort(key=lambda n:n['node'])
def hidden(n):
    return n['metadata'].get('is_visually_hidden_from_conversation') is True
def assistant(n):
    return n['role']=='assistant' and n['content_type'] in ('text','multimodal_text') and bool(n['text'].strip()) and not hidden(n)
def user(n):
    return n['role']=='user' and not hidden(n)
def workflow(n):
    return assistant(n) and n['content_type']=='text' and n['metadata'].get('is_thinking_preamble_message') is True
def normalized(s):
    return re.sub(r'[^\w\s]', '', s.casefold()).strip()
extra = {'looking now','one minute','reading','give me a beat'}
def status_reason(n):
    e = event_index.get((n['case'],n['node']))
    if e and e['status_only']:
        return 'INHERITED_STATUS_ONLY'
    if normalized(n['text']) in extra:
        return 'PREVIOUSLY_OBSERVED_EXTRA_FORM'
    if n['text'].strip() and not re.search(r'\w',n['text']):
        return 'PUNCTUATION_ONLY'
    return None
def node_record(n):
    if n is None:
        return None
    return {k:n.get(k) for k in ['case','node','role','content_type','text','time_utc','message_id','metadata','source_file','line','body_line']}
def seconds(a,b):
    try:
        return (dt.datetime.fromisoformat(b['time_utc'])-dt.datetime.fromisoformat(a['time_utc'])).total_seconds()
    except (KeyError,TypeError,ValueError):
        return None

source_checks=[]
body_mismatches=[]
for s in table['sources']:
    p=pathlib.Path(s['file'])
    source_checks.append({'case':s['case'],'path':str(p),'expected':s['sha256'],'actual':sha(p),'matches':sha(p)==s['sha256']})
    # Preserve embedded lone CR characters; universal-newline translation changes
    # recorded line addresses after a source body containing CR-CR-LF.
    lines=p.read_bytes().decode('utf-8-sig').replace('\r\n','\n').split('\n')
    for n in bycase[s['case']]:
        if n['text']:
            expected=n['text'].split('\n')
            if lines[n['body_line']-1:n['body_line']-1+len(expected)]!=expected:
                body_mismatches.append([s['case'],n['node']])
save('SOURCE_MANIFEST.json',{'analysis_time_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
    'protocol_sha256':sha(HERE/'PROTOCOL.md'),
    'input_hashes':{k:sha(ROOT/(k+'.json')) for k in data},'raw_sources':source_checks,
    'method_snapshots':{p.name:sha(p) for p in HERE.glob('*_SOURCE.md')},'source_body_mismatches':body_mismatches})

# Next retained text under the frozen exclusion rule, including all visible text types.
next_candidates={}
for c,rows in bycase.items():
    forthcoming=None
    for n in reversed(rows):
        next_candidates[c,n['node']]=forthcoming
        if assistant(n) and not status_reason(n):
            forthcoming=n

derived=[]
changes=[]
for e in events:
    c,nid=e['case'],e['node']
    candidate=next_candidates[c,nid] if e['status_only'] else index[c,nid]
    endpoint=candidate['node'] if candidate else float('inf')
    between=[n for n in bycase[c] if nid<n['node']<endpoint] if e['status_only'] else []
    old=e.get('next_substantive')
    row={'event_id':e['event_id'],'case':c,'node':nid,'event':node_record(e),
         'unfinished_candidate':e['unfinished_candidate'],'status_only_inherited':e['status_only'],
         'metadata_preamble':e['metadata'].get('is_thinking_preamble_message') is True,
         'phrases':[o['phrase'] for o in e['occurrences']],
         'preceding_user':e.get('previous_user'),'old_endpoint':node_record(old),
         'content_candidate':node_record(candidate),
         'endpoint_changed':(old['node'] if old else None)!=(candidate['node'] if candidate else None),
         'record_seconds':seconds(e,candidate) if candidate else None,
         'old_record_seconds':e.get('next_substantive_record_seconds'),
         'intervening_user_nodes':[n['node'] for n in between if user(n)],
         'intervening_status_nodes':[n['node'] for n in between if assistant(n) and status_reason(n)],
         'intervening_tool_nodes':[n['node'] for n in between if n['role']=='tool'],
         'intervening_blank_nodes':[n['node'] for n in between if not n['text'].strip()],
         'intervening_hidden_nodes':[n['node'] for n in between if hidden(n)],
         'intervening_redacted_nodes':[n['node'] for n in between if n['metadata'].get('is_redacted') is True],
         'intervening_records':[node_record(n) for n in between],
         'candidate_is_workflow':bool(candidate and workflow(candidate)),
         'content_validity':'INHERITED_NON_STATUS_LABEL_NOT_TASK_COMPLETION' if not e['status_only'] else 'CANDIDATE_NOT_TASK_COMPLETION',
         'tool_evidence':'VISIBLE_TOOL_RECORD' if any(n['role']=='tool' for n in between) else 'NO_VISIBLE_TOOL_RECORD'}
    if not e['status_only']:
        row['structure']='SAME_MESSAGE_NON_STATUS_CONTENT_INHERITED'
    elif not candidate:
        row['structure']='NO_LATER_CONTENT_CANDIDATE'
    elif row['intervening_user_nodes']:
        row['structure']='LATER_CANDIDATE_AFTER_USER_INTERPOSITION'
    else:
        row['structure']='LATER_CANDIDATE_BEFORE_NEXT_USER'
    derived.append(row)
    if row['endpoint_changed']:
        changes.append(row)
save('EVENT_COORDINATES.json',derived)
save('ENDPOINT_CHANGES.json',changes)

# Retrieval is intentionally broader than prospective correction classification.
marker=re.compile(r'\b(?:checking|one moment|one sec(?:ond)?|hang on|hold on|preamble)\b',re.I)
cue=re.compile(r"\b(?:don['’]?t|do not|stop|quit|cut|drop|without|instead|no more|not asking|asked|want|why)\b",re.I)
candidates=[]
for c,rows in bycase.items():
    for pos,n in enumerate(rows):
        if not user(n) or not marker.search(n['text']) or not cue.search(n['text']):
            continue
        later=rows[pos+1:]
        next_u=next((v['node'] for v in later if user(v)),float('inf'))
        opportunity=[v for v in later if v['node']<next_u and assistant(v)]
        immediate=next((v for v in later if assistant(v)),None)
        candidates.append({'anchor_id':f'{c}:n{n["node"]:03}', 'anchor':node_record(n),
            'immediate_assistant':node_record(immediate),
            'next_user_node':None if next_u==float('inf') else next_u,
            'response_opportunity':[node_record(v) for v in opportunity],
            'actual_markers_in_opportunity':[
                {'node':v['node'],'occurrences':event_index[c,v['node']]['occurrences'],'text':v['text']}
                for v in opportunity if (c,v['node']) in event_index],
            'preceding_visible_context':[node_record(v) for v in rows[max(0,pos-8):pos] if assistant(v) or user(v)]})
save('CORRECTION_CANDIDATES.json',candidates)
out=[]
for r in candidates:
    out.append(r['anchor_id']+' USER '+r['anchor']['text'])
    for a in r['response_opportunity']:
        out.append('  ASSISTANT n'+str(a['node'])+' '+a['text'])
    if not r['response_opportunity']:
        out.append('  [NO ASSISTANT BEFORE NEXT USER]')
(HERE/'CORRECTION_CANDIDATES.txt').write_text('\n\n'.join(out),encoding='utf-8')

conversational=[n for n in nodes if assistant(n) and not workflow(n)]
post=[n for n in conversational if n['case']=='twentythird_share' and n['node']>334]
checking=[n for n in post if re.search(r'\bchecking\b',n['text'],re.I)]
actual_checking=[n for n in post if any(o['phrase']=='checking' for o in event_index.get((n['case'],n['node']),{}).get('occurrences',[]))]
post_inline=[n for n in actual_checking if not event_index[n['case'],n['node']]['status_only']]
save('POST_CORRECTION_WINDOW.json',{'anchor':node_record(index['twentythird_share',334]),
    'population':'All conversational assistant replies after n334 through source end; not independent opportunities or a sustained-consent adjudication',
    'replies':[node_record(n) for n in post], 'literal_checking_nodes':[n['node'] for n in checking],
    'actual_checking_nodes':[n['node'] for n in actual_checking],
    'actual_checking_inline_nodes':[n['node'] for n in post_inline],
    'user_messages_after_anchor':[node_record(n) for n in bycase['twentythird_share'] if n['node']>334 and user(n)]})

def timing(v):
    v=[x for x in v if x is not None]
    return {'n':len(v),'median':statistics.median(v) if v else None,'minimum':min(v) if v else None,'maximum':max(v) if v else None,
            'negative':sum(x<0 for x in v),'zero_to_0_1':sum(0<=x<=.1 for x in v),'at_least_10':sum(x>=10 for x in v),'at_least_30':sum(x>=30 for x in v)}
def counts(rows):
    solo=[r for r in rows if r['status_only_inherited']]
    before=[r for r in solo if r['structure']=='LATER_CANDIDATE_BEFORE_NEXT_USER']
    return {'n':len(rows),'structure':dict(C.Counter(r['structure'] for r in rows)),
            'preamble_tagged':sum(r['metadata_preamble'] for r in rows),
            'status_only':len(solo),'endpoint_changes':sum(r['endpoint_changed'] for r in rows),
            'additional_status_before_candidate':sum(bool(r['intervening_status_nodes']) for r in solo),
            'record_time_before_next_user':timing([r['record_seconds'] for r in before]),
            'record_time_by_preamble_flag':{str(flag):timing([r['record_seconds'] for r in before if r['metadata_preamble']==flag]) for flag in (True,False)},
            'with_visible_tool_before_candidate':sum(bool(r['intervening_tool_nodes']) for r in solo),
            'candidate_workflow_count':sum(r['candidate_is_workflow'] for r in rows)}
omitted=[n for n in conversational if normalized(n['text']) in extra and (n['case'],n['node']) not in event_index]
summary={'scope':{'cases':len(cases),'nodes':len(nodes),'visible_assistant_text':sum(assistant(n) for n in nodes),
    'conversational_assistant_text':len(conversational)},'source_hashes_passed':sum(s['matches'] for s in source_checks),
    'source_body_mismatches':len(body_mismatches), 'inclusive':counts(derived),
    'strict':counts([r for r in derived if not r['unfinished_candidate']]),
    'per_case':{c:counts([r for r in derived if r['case']==c]) for c in sorted(cases)},
    'correction_candidates':len(candidates),'post_n334':{'conversational_replies':len(post),
    'literal_checking':len(checking),'actual_checking_events':len(actual_checking),
    'actual_checking_with_inherited_inline_content':len(post_inline)},
    'supplementary_status_nodes':[node_record(n) for n in omitted],
    'endpoint_changes_compact':[{'event':r['event_id'],'old_node':r['old_endpoint']['node'] if r['old_endpoint'] else None,
        'old_text':r['old_endpoint']['text'] if r['old_endpoint'] else None,
        'new_node':r['content_candidate']['node'] if r['content_candidate'] else None,
        'new_text':r['content_candidate']['text'] if r['content_candidate'] else None,
        'old_seconds':r['old_record_seconds'],'new_seconds':r['record_seconds'],
        'users':r['intervening_user_nodes'],'statuses':r['intervening_status_nodes']} for r in changes]}
checks={'source_hashes':all(s['matches'] for s in source_checks),'source_bodies':not body_mismatches,
    'event_count_preserved':len(derived)==len(events)==len(data['events']),
    'unique_event_ids':len({r['event_id'] for r in derived})==len(derived),
    'strict_plus_unfinished':len([r for r in derived if not r['unfinished_candidate']])+sum(r['unfinished_candidate'] for r in derived)==len(events),
    'all_endpoints_pass_frozen_rule':all(r['content_candidate'] is None or not status_reason(index[r['case'],r['content_candidate']['node']]) for r in derived),
    'endpoints_ordered':all(r['content_candidate'] is None or r['content_candidate']['node']>=r['node'] for r in derived),
    'known_chain':abs(next(r for r in derived if r['event_id']=='eleventh_share:n657')['record_seconds']-107.632848)<1e-8}
save('SUMMARY.json',summary)
save('VERIFICATION.json',checks)
assert all(checks.values()),checks
print(json.dumps({k:v for k,v in summary.items() if k not in ('per_case','supplementary_status_nodes','endpoint_changes_compact')},ensure_ascii=False,indent=2))
print('CHECKS',checks)
print('POST INLINE NODES',[n['node'] for n in post_inline])
