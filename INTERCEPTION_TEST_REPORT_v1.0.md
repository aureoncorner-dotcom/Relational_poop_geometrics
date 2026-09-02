# Moving-Lattice Interception Test — 21-Call Holdout

## Verdict

**Not robustly confirmed.**

One narrow result crossed the nominal corrected threshold on assistant-message `create_time`, but it did not survive the planned robustness checks. The input-side test missed the threshold; the output-side result disappeared when Audit_12 was removed and did not reproduce on `update_time`. The input and output winners also required different lattice parameters.

The defensible conclusion is therefore:

> The 21-call corpus contains a weak, timestamp-surface-dependent concentration of exact `Checking` outputs near one locked q=6 intersection model. It does not establish a stable independently rotating lattice.

## Data actually tested

- 21 native public share records: Audit_1–Audit_17, Casual Greeting Response, Funfunaudit, Mentioning Something Important, and the Long-SRT/Hidden-Quotient follow-up.
- The derivative SRT handoff wrapper was excluded.
- 5,584 visible user-message opportunities, indexed without deleting gaps.
- 121 user opportunities retained as no-output placeholders.
- 6,987 visible nonempty assistant-message outputs, indexed separately.
- 827 input-linked exact-`Checking` turns and 830 exact-`Checking` output messages.
- Assistant-only outputs were retained in the output ledger instead of being forced onto the nearest user turn.
- Native `turn_exchange_id` was the primary user/output join; source adjacency was only a fallback.

The 450 captions embedded inside the Long-SRT prompt were not promoted to native message timestamps. The wrapper/follow-up’s native messages were included, and an exclusion sensitivity was run.

## Frozen geometry

The message increment was fixed at:

\[
\alpha=\varphi^{-2}\approx0.38196601125
\]

For every q in {6, 12, 24}, the test used a clockwise lattice and call-start reset. Period, starting phase, and catch width were selected only from the older corpus, then hashed before new-call phase scoring.

### Input lock

| q | Period T (s) | Relative phase (turns) | Catch width (turns) |
|---:|---:|---:|---:|
| 6 | 4.237852 | 0.015046 | 0.008333 |
| 12 | 152.218511 | 0.021991 | 0.008333 |
| 24 | 47.945826 | 0.015625 | 0.002083 |

SHA-256: `428d3cb4ffde9175051a3f67d48808946e0ef56360ba6ff367777be3a2e54b84`

### Output lock

| q | Period T (s) | Relative phase (turns) | Catch width (turns) |
|---:|---:|---:|---:|
| 6 | 38.054628 | 0.010417 | 0.016667 |
| 12 | 35.918786 | 0.023727 | 0.012500 |
| 24 | 135.611276 | 0.004919 | 0.002083 |

SHA-256: `e07fe5b6b4b4034539a801fd48684112bca1e0a6346ba7e5547769c8b1208b5b`

The old-corpus fit statistics are search-selected and are not evidence by themselves. Because aggregate new-call outcome counts and a small timestamp sample were seen before the matched structural locks were finalized, these locks are **semi-confirmatory**, not pristine preregistrations. No new-call phases were inspected before the locks were hashed.

## Primary results

Each p-value below comes from within-call circular shifts. The primary p-value uses the maximum z across q, so q=6/12/24 selection is already accounted for.

| Analysis | Winning q | Inside risk | Outside risk | Risk ratio | Max z | Max-q p |
|---|---:|---:|---:|---:|---:|---:|
| Input `create_time`, all 21 | 24 | 0.1812 | 0.1442 | 1.2563 | 1.9907 | **0.0629** |
| Output `create_time`, all 21 | 6 | 0.1349 | 0.1148 | 1.1756 | 2.1847 | **0.0488** |
| Input `create_time`, no long-SRT wrapper | 24 | 0.1831 | 0.1459 | 1.2551 | 1.9907 | **0.0638** |
| Output `create_time`, no long-SRT wrapper | 6 | 0.1364 | 0.1168 | 1.1679 | 2.1847 | **0.0497** |
| Output `create_time`, no Audit_12 | 6 | 0.1195 | 0.1025 | 1.1653 | 1.7587 | **0.1190** |
| Input `update_time` sensitivity | 24 | 0.1778 | 0.1470 | 1.2095 | 1.0351 | **0.3913** |
| Output `update_time` sensitivity | 6 | 0.0082 | 0.0078 | 1.0541 | −0.0986 | **0.8686** |

The q=24 input result had an unadjusted q-specific p of 0.0177, but it became 0.0629 after the required maximum-across-q correction. The q=6 output result had an unadjusted q-specific p of 0.0156 and a max-q p of 0.0488.

That output result is not stable enough to carry the hypothesis:

1. Removing Audit_12 changes p from 0.0488 to 0.1190.
2. The `update_time` sensitivity is null.
3. The input and output winners disagree: q=24/T=47.95 s versus q=6/T=38.05 s.
4. `create_time` is known in these voice records to regress relative to source order; the holdout contains 365 input and 169 output create-time regressions.

## Separate outcome lanes

No secondary lane survived Holm correction across lanes.

Notable but non-confirming examples:

- Input missing-output lane: max-q p=0.0604, Holm p=0.3624.
- Input marker-first split: max-q p=0.0707, Holm p=0.3624.
- Output marker-first split: max-q p=0.0238, Holm p=0.1190.
- Output multi-assistant turn: max-q p=0.0566, Holm p=0.2264.
- Visible redaction did not concentrate reliably.

Missing output, exact Checking, bare marker, generic marker, marker-first split, multi-message split, and visible redaction were never collapsed into one post-hoc “failure” variable.

## Null and multiplicity control

- 10,000 circular shifts of each event lane within each call for the main analyses.
- Each call’s length and local event runs were preserved.
- The same shifted label sequence was evaluated against all q values for a lane.
- Primary inference used the maximum statistic across q.
- Secondary lanes received max-q correction and Holm correction across lanes.
- The Long-SRT wrapper exclusion and Audit_12 influence check were reported as robustness analyses, not substituted for the primary result.

## What this does and does not say

This result does **not** rule out every possible relative-phase model. It rejects this frozen implementation as a robust explanation of the 21-call holdout.

Even a stable positive result would establish only an observable timing association. It would not identify a hidden actor, software component, motive, literal rotating object, or causal mechanism.

The older inference/composite-failure lock was not forced onto these calls because the new set does not yet have a frozen, matched inference-opportunity adjudication. No semantic failure labels were inferred from geometry.

## Reproducibility

- Source manifest SHA-256: `136e487f8e5c1a6794e33936cbe3c3a6cc2335b1274218a3230fe1b7c41d7c43`
- Final results SHA-256: `897543e1927680b32dc028887e939020eab8e6002ed3ffd37c35a5f96881a763`
- Workbook SHA-256: `f30c907c7501e5a6f7a6b96de006f2062e8bdc3dbc958f8c83994165d4afff46`

The workbook contains the verdict dashboard, frozen models, call-level source register, all model/lane results, all 5,584 scored input rows, all 6,987 scored output rows, and the method/limitations ledger.
