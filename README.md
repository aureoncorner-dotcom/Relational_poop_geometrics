# TOROIDAL v0.13 Beast

This is a dependency-free Python reference engine for the audited orbit-quotient and residual-cocycle upgrade. It turns the packet's exact finite constructions into executable invariants, ledgers, reports, failure witnesses, and command-line tools while leaving every frozen predecessor untouched.

Status: **auditable reference implementation**, not a completed Q2 Monte Carlo production kernel and not evidence that any physical platform instantiates the formal geometry.

## What it does

- Implements canonical signed residues and the exact `W -> q` quotient on the explicitly divergence-free `h6=0` domain.
- Implements the eight-sector Walsh-Hadamard direct/dual transform exactly for rational inputs.
- Validates every transition against the frozen operator-class table.
- Writes hash-chained transition, cocycle, and closure-counterexample ledgers.
- Verifies cocycle telescoping, state-hash continuity, file hashes, and cross-artifact derivation.
- Separates algebraic span, certified liftable reachability, observed accessibility, raw round trips, and unrun mixing diagnostics.
- Emits `null` transition rows when no departures were observed.
- Tests exact strong lumpability and retains every located counterexample.
- Rejects the `(x+y) mod 2` sheet bit on odd-`L` tori.
- Keeps material-streamtube and fixed-Eulerian flux charts typed and separate.
- Supplies an executable two-clock model with units, origins, reset semantics, finite site range, boundary tolerance, and the `T_g/q` unlabelled period.
- Implements the repaired confinement decision branch with model preference, fit validity, estimator concordance, and the scale gate as separate coordinates.

## Quick start

Python 3.11 or newer is sufficient; there are no runtime dependencies.

```text
python -m pip install -e .
toroidal-v013 self-test
python -m unittest discover -s tests -v
toroidal-v013 demo --output demo-run
toroidal-v013 verify-bundle demo-run
```

Without installation:

```text
set PYTHONPATH=src
python -m toroidal_v013 self-test
python -m toroidal_v013 demo --output demo-run
```

The deterministic demo is a formal test fixture, not empirical data. It walks all eight parity sectors through a Gray-code loop and writes the complete artifact bundle.

## Required bundle artifacts

Every analysis bundle contains:

1. `sector_transition_operator_ledger.jsonl`
2. `sector_cocycle_ledger.jsonl`
3. `formal_orbit_report.json`
4. `observed_accessibility_report.json`
5. `q_projection_lumpability_or_descent_report.json`
6. `closure_counterexamples.jsonl`
7. `MANIFEST.json`
8. `SHA256SUMS`

The verifier checks both byte integrity and semantic derivation across the ledgers and reports. Hashes bind bytes and lineage; they do not prove an interpretation true.

## Main commands

```text
toroidal-v013 self-test
toroidal-v013 demo --output PATH
toroidal-v013 analyze LEDGER --output PATH --generator x --generator y --generator z --liftability PROVED --liftability-evidence RECEIPT
toroidal-v013 verify-ledger LEDGER
toroidal-v013 verify-bundle BUNDLE
toroidal-v013 diamond --length 4 --x 3 --y 0
toroidal-v013 two-clock --theta0 0.1 --period 12 --g0 0.2 --order 3 --width 0.05 --timestamp-units seconds --index 8 --timestamp 3.5 --eligible
toroidal-v013 flux --length 16 --u0 2 --epsilon 0.3 --s0 4 --material-radius 1.25 --eulerian-radius 0.75
```

## Claim boundary

This package does not silently repair the packet's unspecified worm kernel, generate absent rotating-lattice source data, validate sector mixing, infer a global holonomy sector from one Wilson-loop representative, or promote a descriptive `q` transition matrix to an autonomous law. Those gates remain unresolved until their required evidence exists.

See [docs/IMPLEMENTATION_AUDIT.md](docs/IMPLEMENTATION_AUDIT.md), [docs/TRACEABILITY.md](docs/TRACEABILITY.md), and [docs/LEGACY_PYTHON_AUDIT.md](docs/LEGACY_PYTHON_AUDIT.md).

