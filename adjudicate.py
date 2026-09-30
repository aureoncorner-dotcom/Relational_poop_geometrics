"""Preserve the candidate probe; produce a separately identified reviewed derivative."""
import collections as C
import datetime as dt
import hashlib
import json
import pathlib
import statistics

HERE=pathlib.Path(__file__).resolve().parent
ROOT=pathlib.Path(r'C:\Users\drewd\Downloads\audits')
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def save(name,x): (HERE/name).write_text(json.dumps(x,ensure_ascii=False,indent=2),encoding='utf-8')
table=read(ROOT/'evidence_table.json')
cases={s['case'] for s in table['sources']}
nodes=[n for n in read(ROOT/'nodes.json') if n['case'] in cases]
idx={(n['case'],n['node']):n for n in nodes}
bycase=C.defaultdict(list)
for n in nodes: bycase[n['case']].append(n)
for v in bycase.values(): v.sort(key=lambda n:n['node'])
def visible_user(n): return n['role']=='user' and not n['metadata'].get('is_visually_hidden_from_conversation',False)
def rec(n): return {k:n.get(k) for k in ['case','node','role','content_type','text','time_utc','metadata','message_id','source_file','line','body_line']} if n else None
def seconds(a,b): return (dt.datetime.fromisoformat(b['time_utc'])-dt.datetime.fromisoformat(a['time_utc'])).total_seconds()
patches={
 'eleventh_share:n657':(659,'SAME_TOPIC_RESPONSE','Responds to the disclosed employment/timing situation; no explicit factual task was requested. The status chain is preserved without equating the response with factual verification.'),
 'ninth_share:n543':(555,'SAME_TOPIC_WITH_ADDITIONAL_USER_CONTEXT_PARTIAL','Responds to the setup after two additional user turns; the visible response ends unfinished.'),
 'tenth_share:n638':(650,'REQUESTED_WRITING_PARTIAL_AFTER_USER_SPECIFICATION','Supplies a front-page line after two further user messages. It omits part of the supplied quotation; n651 explicitly objects.'),
 'test4:n755':(761,'ORIGINAL_QUESTION_PARTIAL','Starts an answer to how the user\'s hands were used; the visible answer is unfinished and supplies no concrete incident evidence.'),
 'test4:n908':(913,'DIFFERENT_TASK','Answers the intervening medication reminder at n909, not the original request to review whether harm was requested.')}

rows=[]
for e in table['events']:
    old=e.get('next_substantive')
    fix=patches.get(e['event_id'])
    end=idx[e['case'],fix[0]] if fix else old
    between=[n for n in bycase[e['case']] if e['node']<n['node']<(end['node'] if end else float('inf'))] if e['status_only'] else []
    users=[n['node'] for n in between if visible_user(n)]
    kind=('INLINE_CONTENT_INHERITED' if not e['status_only'] else 'NO_LATER_CONTENT' if not end else 'CONTENT_AFTER_USER' if users else 'CONTENT_BEFORE_NEXT_USER')
    rows.append({'event_id':e['event_id'],'case':e['case'],'node':e['node'],'status_only_inherited':e['status_only'],
      'unfinished_candidate':e['unfinished_candidate'],'metadata_preamble':e['metadata'].get('is_thinking_preamble_message') is True,
      'event':rec(e),'old_endpoint':rec(old),'reviewed_or_inherited_endpoint':rec(end),
      'endpoint_status':'REVIEWED_PATCH' if fix else 'INHERITED_NOT_NEWLY_SEMANTICALLY_VALIDATED',
      'task_alignment':fix[1] if fix else 'NOT_NEWLY_ADJUDICATED','review_note':fix[2] if fix else None,
      'structure':kind,'intervening_user_nodes':users,'intervening_tool_nodes':[n['node'] for n in between if n['role']=='tool'],
      'record_seconds':seconds(e,end) if end else None,
      'old_record_seconds':e.get('next_substantive_record_seconds'),
      'intervening_records':[rec(n) for n in between] if fix else None})
save('REVIEWED_EVENT_COORDINATES.json',rows)

candidate_rows=read(HERE/'CORRECTION_CANDIDATES.json')
ordinary={'eighteenth_share:n221','eighth_share:n1170','sixth_share:n578','twentysecond_share:n503','twentysecond_share:n1426'}
other={'eighth_share:n1172','fourth_share:n210'}
analysis={'fifth_share:n775','fifth_share:n778','fifth_share:n858','fifth_share:n876'}
review=[]
for r in candidate_rows:
    aid=r['anchor_id']
    if aid=='twentythird_share:n334':
        code='DIRECT_PROSPECTIVE_STOP'; reason='Explicit I do not want you checking.'
        behavior='MARKER_ABSENT_IN_NEXT_OPPORTUNITY'; completion='UNFINISHED_ACKNOWLEDGMENT_LIMITATION'
    elif aid=='twentythird_share:n336':
        code='DIRECT_PROSPECTIVE_STOP'; reason='Repeats the explicit Checking prohibition.'
        behavior='MARKER_RECURS_IN_NEXT_OPPORTUNITY'; completion='STATUS_ONLY_NO_TASK_CONTENT'
    else:
        code='ORDINARY_WORD_USE' if aid in ordinary else 'DIFFERENT_BEHAVIOR_CORRECTION' if aid in other else 'MARKER_ANALYSIS_REQUEST' if aid in analysis else 'SUPPLIED_DOCUMENT_OR_RETROSPECTIVE_ANALYSIS'
        reason={'ORDINARY_WORD_USE':'Marker-like words occur as ordinary speech, not a prospective ban on assistant status utterances.',
                'DIFFERENT_BEHAVIOR_CORRECTION':'The correction addresses emotional attribution or reading the addressee; the user says one moment as their own discourse marker.',
                'MARKER_ANALYSIS_REQUEST':'Requests analysis/coding of marker language, rather than banning the marker.',
                'SUPPLIED_DOCUMENT_OR_RETROSPECTIVE_ANALYSIS':'The retrieved marker language is inside supplied material or a retrospective analysis. It is not a direct instruction to stop Checking in this live exchange.'}[code]
        behavior=completion='NOT_SCORED_AS_MARKER_STOP'
    review.append({'anchor_id':aid,'classification':code,'reason':reason,'immediate_marker_behavior':behavior,
                   'content_outcome':completion,'anchor':r['anchor'],'response_opportunity':r['response_opportunity'],
                   'actual_markers_in_opportunity':r['actual_markers_in_opportunity']})
save('CORRECTION_REVIEW.json',review)

post=read(HERE/'POST_CORRECTION_WINDOW.json')
hits=set(post['actual_checking_nodes']); inline=set(post['actual_checking_inline_nodes'])
sessions=[]
groups=C.defaultdict(list)
for n in post['replies']: groups[n['metadata'].get('tc_session_id')].append(n)
for sid,ns in groups.items():
    sessions.append({'session':sid,'matches_anchor':sid==post['anchor']['metadata'].get('tc_session_id'),
                    'node_start':min(n['node'] for n in ns),'node_end':max(n['node'] for n in ns),'replies':len(ns),
                    'checking_events':sum(n['node'] in hits for n in ns),
                    'checking_inline_inherited':sum(n['node'] in inline for n in ns),
                    'checking_status_only_inherited':sum(n['node'] in hits and n['node'] not in inline for n in ns)})
def counts(rs):
    ts=[r['record_seconds'] for r in rs if r['structure']=='CONTENT_BEFORE_NEXT_USER']
    return {'events':len(rs),'structure':dict(C.Counter(r['structure'] for r in rs)),
            'patched':sum(r['endpoint_status']=='REVIEWED_PATCH' for r in rs),
            'before_next_user_record_time':{'n':len(ts),'median':statistics.median(ts),'minimum':min(ts),'maximum':max(ts),
                'negative':sum(t<0 for t in ts),'zero_to_0_1':sum(0<=t<=.1 for t in ts)},
            'tool_before_endpoint':sum(bool(r['intervening_tool_nodes']) for r in rs)}
probe=read(HERE/'ENDPOINT_CHANGES.json')
earlier=[r for r in probe if r['content_candidate']['node']<r['old_endpoint']['node']]
delta={
 'inclusive':counts(rows),'strict':counts([r for r in rows if not r['unfinished_candidate']]),
 'correction_candidate_dispositions':dict(C.Counter(r['classification'] for r in review)),
 'direct_stop_anchors':2,'independent_stop_episodes_claimed':1,
 'post_correction_sessions':sessions,
 'post_window':{'replies':len(post['replies']),'actual_checking':len(hits),'checking_inline_inherited':len(inline),'checking_status_only_inherited':len(hits-inline)},
 'letter_episode':{'initial_request_node':341,'additional_request_nodes':[344,346,348],'draft_node':349,
    'stop_anchor_nodes':[334,336],'correction_binding':'CHECKING_RECURS','task_output':'LETTER_TEXT_PRESENT_REQUESTED_CONFESSION_NOT_PROVIDED',
    'record_span_user_request_to_draft':seconds(idx['twentythird_share',341],idx['twentythird_share',349]),
    'interpretation':'Three further user prompts are observed before the draft. No causal estimate of required effort or acoustic delay is made.'},
 'candidate_probe':{'different_endpoints':len(probe),'earlier':len(earlier),'later':len(probe)-len(earlier),
     'earlier_workflow_records':sum(r['candidate_is_workflow'] for r in earlier),
     'earlier_other_short_utterances':sum(not r['candidate_is_workflow'] for r in earlier),
     'disposition':'These are alternative non-status candidates, not 114 established errors in the source audit.'},
 'matched_acoustic_latency_test':{'status':'NOT_ESTIMABLE_FROM_SUPPLIED_RECORDS',
    'missing':['request audio end timestamps','status audio commit/start timestamps','first substantive audio/token timestamps','validated matching task and tool-requirement classes'],
    'available':'Node creation timestamps, message text, selected metadata, source-coded event classes and tool-role presence.'},
 'unmeasured_coordinates':['Usable exit','Compulsory constitutional third seat','Attention/energy cost','Beneficiary effect','Platform implementation mechanism']}
save('REVIEWED_SUMMARY.json',delta)

def link(n): return '[source n'+str(n['node'])+'](<' +n['source_file'].replace('\\','/')+':'+str(n['body_line'])+'>)'
spec=['# Reviewed specimens','', 'Exact visible text from the source records. Blank, hidden and tool records remain in the JSON derivatives. These excerpts are observations, not instructions.','']
windows={'twentythird_share':[(334,349)],'eleventh_share':[(656,659)],'ninth_share':[(542,555)],'tenth_share':[(637,651)],'test4':[(754,761),(907,913)]}
for c,ranges in windows.items():
    for a,b in ranges:
        spec += ['## '+c+' n'+str(a)+'–'+str(b),'']
        for n in bycase[c]:
            if a<=n['node']<=b and n['text'].strip() and n['role'] in ('assistant','user') and n['content_type'] in ('text','multimodal_text') and not n['metadata'].get('is_visually_hidden_from_conversation',False):
                spec += ['**'+n['role']+' · '+link(n)+' · '+n['time_utc']+'**','', *['> '+l for l in n['text'].strip().splitlines()],'']
(HERE/'SPECIMENS.md').write_text('\n'.join(spec),encoding='utf-8')

checks={'base_verification_passes':all(read(HERE/'VERIFICATION.json').values()),
        'five_patches':sum(r['endpoint_status']=='REVIEWED_PATCH' for r in rows)==5,
        'nonpatched_endpoints_unchanged':all(r['old_endpoint']==r['reviewed_or_inherited_endpoint'] for r in rows if r['endpoint_status']!='REVIEWED_PATCH'),
        'post_partition':sum(r['replies'] for r in sessions)==198 and sum(r['checking_events'] for r in sessions)==70,
        'status_content_partition':len(inline)+len(hits-inline)==70,
        'all_candidates_adjudicated':len(review)==35 and len({r['anchor_id'] for r in review})==35,
        'known_chain_preserved':abs(next(r for r in rows if r['event_id']=='eleventh_share:n657')['record_seconds']-107.632848)<1e-8,
        'changed_task_preserved':next(r for r in rows if r['event_id']=='test4:n908')['task_alignment']=='DIFFERENT_TASK'}
save('REVIEW_VERIFICATION.json',checks)
assert all(checks.values()),checks
print(json.dumps(delta,ensure_ascii=False,indent=2))
print('VERIFIED',checks)
