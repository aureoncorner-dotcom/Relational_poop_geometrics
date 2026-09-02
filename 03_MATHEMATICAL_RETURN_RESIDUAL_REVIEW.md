# Mathematical Return-Residual Review of the Provenance Packet

## Scope

This review uses only declared maps, finite set relations, retained ledgers, typed products, and quotient/descent conditions. It does not use OMNIBUS normative or dyadic-humility predicates as evidence. The four specifications are dated 2026-08-31 and therefore function only as post-packet mathematical specifications; they do not retroactively predeclare the August 20-30 audit rules.

## Verdict

The earlier packet is strong as a **static provenance reconstruction** and weak as a **dynamical closure instrument**. Its source-to-view and item-to-aggregate maps are mostly reconstructible because the preimage ledgers survive. It does not contain the loop states, declared channel comparators, or repeated state-pair transitions required to test residual descent. Therefore no autonomous residual law is established.

## Corrections to my prior delivery

1. **Recoverability boundary.** I previously wrote that the first unrecoverable distinction *occurred* at `hydrated payload -> selected transcript`. The mathematically exact statement is: **the earliest recoverability boundary localizable from the surviving artifacts is that map**. Because neither fetched page nor hydrated payload survives, an earlier upstream loss cannot be ruled out. Absolute first loss is `UNRESOLVED`.
2. **Hash closure.** The packet's data/count validation passed, but its internal SHA-256 manifest contains 161 rows for 164 final files. The unsealed files are `15_OUTPUT_SHA256.csv, 15_VALIDATION.json, PROVENANCE_RECONSTRUCTION_v1.zip`. Thus “complete packet hash closure” was not established. The prior ZIP's externally reported hash identifies that archive, but the internal manifest does not recursively seal itself or the post-manifest outputs.

## Quotient map audit

### Q0 — hydrated payload to selected transcript

The extractor selects `linear_conversation`, retains eight named metadata keys, converts structured content to text/placeholders, and writes a transcript. The hydrated input is unavailable. The map is structurally noninjective, but its empirical kernel cannot be enumerated without the source payloads. The boundary is irreversible inside the local packet.

### Q1 — transcript to compact view

The frozen transcripts contain 20,715 nodes. Compact construction removes 4,282 blank nodes (20.671%) and whitespace-normalizes the remaining 16,433. This map is noninjective. It is not an irreversible audit loss because all 24 transcripts survive.

### Q2 — denominator v1 to v2

- v1: 342 opportunities
- v2: 422 opportunities
- intersection: 331
- union: 433
- removed: 11
- added: 91
- symmetric difference: 102 (23.557% of union)
- Jaccard similarity: 0.764434

| v1 state | v2 state | count |
|---|---|---:|
| `ABSENT` | `ambiguous_sensitivity` | 25 |
| `ABSENT` | `primary` | 66 |
| `ambiguous_sensitivity` | `ABSENT` | 9 |
| `ambiguous_sensitivity` | `ambiguous_sensitivity` | 65 |
| `primary` | `ABSENT` | 2 |
| `primary` | `primary` | 266 |

The opportunity set is not invariant under the rule revision. Both versions survive, so the residual is reconstructible. Mathematics alone supplies no gold ordering between the versions.

### Q3 — component vector to composite failure

For 406 observed responses, the binary composite has 148 failures and 258 nonfailures. Its failure fiber contains 11 distinct source vectors; its nonfailure fiber contains 2. The binary map is therefore highly noninjective.

| `(evidence, proposition, task, refusal)` | composite | n |
|---|---|---:|
| `0,0,0,no` | `yes` | 28 |
| `0,0,0,yes` | `yes` | 44 |
| `0,0,1,no` | `yes` | 1 |
| `0,1,0,no` | `yes` | 5 |
| `0,1,0,yes` | `yes` | 4 |
| `0,1,1,no` | `yes` | 42 |
| `0,1,1,yes` | `yes` | 5 |
| `1,0,0,no` | `yes` | 10 |
| `1,0,1,no` | `yes` | 5 |
| `1,1,0,no` | `yes` | 3 |
| `1,1,1,no` | `no` | 250 |
| `NA,1,0,no` | `yes` | 1 |
| `NA,1,1,no` | `no` | 8 |

The three-coordinate and four-coordinate formulas agree on this sample because there are 0 cases where `refusal=yes` while the three-coordinate composite is false. This is a sample contingency, not an algebraic identity between the formulas.

### Q4 — all Checking occurrences to active-preamble metric

The inclusive frozen corpus contains 1,017 assistant whole-word tokens in 1,010 messages. The active-preamble quotient retains 942 tokens/messages and excludes 75 tokens across 68 messages. It removes 7.375% of tokens and 6.733% of token-bearing messages from the active metric. Those excluded objects remain occurrences in the lexical universe.

### Q5 — correction status to materially affected

The `76/107` result is the binary projection `status != UNCHANGED`. It merges five distinct correction classes. It is exactly reproducible as a descriptive projection, but it is not a classifier error rate and contains no gold-label comparison.

### Q6 — records to episodes

The membership ledger maps 13,309 record memberships to 3,088 episodes: mean 4.3099, median 2, maximum 147 members. 2,986 episodes contain multiple records, and 1,361 record collapsed duplicate candidates. Component IDs and membership rows retain the fibers, so the collapse is reconstructible.

## Marker × failure product omitted from the prior narrative

Using any visible whole-word `Checking` token in the 406 observed inference-response answer units:

| | failure | no failure | total |
|---|---:|---:|---:|
| Checking present | 19 | 106 | 125 |
| Checking absent | 129 | 152 | 281 |

- marked failure rate: 19/125 = 15.200%
- unmarked failure rate: 129/281 = 45.907%
- risk ratio: 0.331101
- risk difference: -0.307075
- pooled odds ratio: 0.211204
- unclustered Fisher two-sided p: 9.56125334785e-10
- case-stratified Mantel-Haenszel odds ratio: 0.321282
- equal-case rates among the 16 cases containing both marker states: 21.766% marked versus 43.550% unmarked; difference -0.217843

This ledger shows a **negative**, not positive, association between the visible token and the coded composite failure. It does not undo the post-hoc undercounting of Checking occurrences; it defeats any attempt to use `Checking` presence itself as a positive proxy for composite failure in this sample. The test is retrospective and the unclustered p-value is not a confirmatory corpus-level probability.

## Residual-closure test

The packet lacks predeclared loop IDs, typed `C/D/K` state records, channel comparators, and repeated state-pair transitions. Therefore:

```text
descent_test_run = false
residual_closure = UNRESOLVED_NOT_TESTED
autonomous_residual_law = NOT ESTABLISHED
```

The static quotient maps above remain valid. They do not become a dynamical recurrence law.

## Formal corrections required in the new specifications

### 1. Time-indexed factor is not autonomous

For each fixed `n`, the stated descent implication correctly yields a factor `F_R,n`. A family `F_R,n` is non-autonomous when it depends on `n`. A single autonomous map `F_R` additionally requires either a time-homogeneous state update or the cross-time condition

```text
q_R(z) = q_R(z')
  implies
q_R(Psi_n(z)) = q_R(Psi_m(z'))
```

for all eligible `n,m,z,z'`. Equivalently, include `n` or the update regime in retained state and stop calling the reduced law autonomous.

### 2. Failed descent is not unresolved descent

The closure codomain needs three states:

```text
CLOSED       = descent demonstrated on the declared domain
NOT_CLOSED   = at least one valid counterexample exists
UNRESOLVED   = untested, incomplete coverage, or unresolved eligibility
```

Combining explicit failure and absence of a test under `UNRESOLVED` discards exactly the counterexample the framework says to retain.

### 3. Gate closure needs a typed name

OMNIBUS distinguishes `GATE_CLOSURE` from residual closure, while GQG v0.12 later calls the same `1 -> 0` transition `CLOSURE`. Use `GATE_CLOSURE` consistently.

## Narrow mathematical result

The packet preserves enough source coordinates to reconstruct most *later* quotients, but not enough upstream state to reconstruct the hydrated payload or enough sequential state to prove residual closure. The static findings that survive are: the local recoverability boundary, the exact denominator-version residual, the noninjective composite-failure projection, the post-hoc Checking projection, the reconstructible episode fibers, and the negative `Checking × composite-failure` association in the coded sample.
