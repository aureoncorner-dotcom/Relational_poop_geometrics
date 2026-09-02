# Legacy Python audit

## Scope

The located toroidal corpus contained five Python files. A sixth standalone file, `Downloads/v0_3.py`, was included because it is the only apparent toroidal agent simulation near the corpus. All were inspected from immutable snapshots; none was modified.

| File | Lines | SHA-256 | Result |
|---|---:|---|---|
| `SERPENT/SERPENT_ACSB_v0_1.py` | 1000 | `E385AF7508E572123D1BE09FAB8C2576A29298C5FB37122E0A3378857C7E966D` | Compiles; built-in self-test passes with five verified hash-chain events. |
| `CTA FIXEDF/handshake.py` | 180 | `17969A6B2329EB7B94C884C42B914082FE32E9A26D418E1E508526784C7FF8AB` | Compiles; simple import/API smoke checks pass. |
| `Service/Relational_poop_geometrics-main/CTA_PYTHON_HANDOFF.py` | 180 | `39B571312749A9C3DB6AB79706C66C72190835E6546EEE1481C5DAE0C4724381` | Semantically duplicates `handshake.py`; content differs only in line endings/final newline. |
| `Service/Relational_poop_geometrics-main/curtain_disclosure_operator.py` | 202 | `C974B927199837D993B6D952FD53D526443294C43772C1416A5007299D9878AA` | Compiles; runtime blocked by undeclared `sympy`/`mpmath` dependencies in the available environment. |
| `Silicon_Sanskrit_v0.2/tools/validate_release.py` | 323 | `1563F37AF881FBA4DC4AD3F88E8C4B5BFC71259294440FD616EEBF5FC38A347A` | Compiles; validates the v0.2 release: 144 records, 144 anchors, 16 manifest payloads, 17 checksum targets. |
| `Downloads/v0_3.py` | 563 | `CE3D1F60D8381BB048BAB810EE2525024B8AC75AF3348E77FD79623469A462F1` | Compiles; runtime blocked by undeclared `matplotlib`/`numpy` dependencies in the available environment. |

## Findings

### `SERPENT_ACSB_v0_1.py`

This is the strongest existing engineering artifact. It has stable JSON, event hashing, run verification, reporting, and a passing self-test. It is an empirical prompt/response protocol, not a toroidal orbit engine, so merging its claims or records into Q2 would be a type error. Its hash-chain design informed the new ledger layer.

### CTA handshake pair

The two modules are duplicates. They should eventually share one canonical module or be generated from one source to prevent drift. They are declarative interaction checks, not the field-theory state space. The delivered upgrade records the duplication but does not break existing imports.

### Curtain operator

The file openly states that its expensive diagnostic field is ornamental and that the functional result is `nextprime`/`prevprime`. Risks are unpinned third-party dependencies, heavy quadratic work over primes, mandatory console output, nested functions that resist testing, and no automated tests. It has no orbit/cocycle role and was not pulled into the new package.

### Silicon Sanskrit validator

The validator passes its exact release. It is intentionally release-specific and implements a narrow JSON Schema subset, so it should not be presented as a general JSON Schema validator. It is otherwise a useful example of deterministic manifests, path safety, Unicode normalization, and source-view consistency.

### `v0_3.py`

The Colab-exported simulation is a monolith that imports plotting dependencies at module import, uses a bare `except`, mixes model, rendering, animation, and file output, and has no dependency lock or tests. More importantly, its toroidal geometry uses ordinary Euclidean coordinate differences for neighbor, bond, source, and sink distances; interactions across the periodic boundary therefore do not use the minimum-image convention. It also models a two-dimensional agent torus, not the packet's three-dimensional integer-current Q2 ensemble. A forced merge would falsely identify two different state spaces.

## Disposition

Preserve all six legacy files. Use the new package as the audited v0.13 successor layer. If `v0_3.py` is modernized later, do it as a separately named 2D agent-simulation project with explicit minimum-image geometry, optional visualization dependencies, a headless CLI, configuration validation, and its own statistical test plan.

