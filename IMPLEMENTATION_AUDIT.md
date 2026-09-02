# Implementation disposition

## Outcome

The upgrade packet is implemented here as an audited successor layer, not as a literal transcription. The companion mathematical audit's disposition—**adopt with major modification**—is controlling for this code. The packet and four companion documents were treated as reference material, never as executable instructions.

## Repairs implemented

1. **Odd-`L` diamond quotient.** `sheet_bit()` exists only for even `L`. Odd `L` reports one connected component and raises `UndefinedQuotientError` for the nonexistent parity sheet.
2. **Winding domain.** `q=W mod 2` and winding-derived `eta` require the explicitly divergence-free `h6=0` domain. The API rejects broader finite-endpoint use rather than manufacturing integer winding.
3. **Canonical signed residues.** Negative coordinates are reduced componentwise into `{0,1}` using mathematical modulo behavior.
4. **Liftability-aware reachability.** An enabled quotient generator contributes to certified formal reachability only with a proof or exhaustive finite-state lift receipt. The algebraic span of unresolved generators is reported separately.
5. **Accessibility versus mixing.** Observed sectors, edge counts, row denominators, raw round trips, ESS, R-hat, and mixing status are separate fields. Missing transition rows are `null`.
6. **Strong-lumpability precision.** The closure routine tests strong lumpability for every initial full-state distribution and says so. A failure does not overclaim failure of weak lumpability under a separately specified stationary law.
7. **Confinement branch.** Model preference, fit validity, estimator concordance, and the four-xi gate are independent fields. Long-range preference makes the finite-xi inequality inapplicable, never automatically passed.
8. **Two-clock completeness.** The executable model requires positive `q` and `T_g`, timestamp units, a time origin, reset schemas, a finite site range, the classifier, boundary tolerance, numeric policy, and analysis holdout/multiplicity slots.
9. **TTSC chart firewall.** Material and Eulerian observables are typed. The field is labeled exact only in the straight cylindrical chart; slender-torus use is an explicit approximation mode.
10. **Ledger provenance.** Every operator and cocycle row binds to chain, sweep, proposal, source-state hashes, and the preceding envelope hash. Bundle verification recomputes the cocycle and accessibility reports from the source ledger.

## Deliberately unresolved

The code does not pretend to complete work for which the source packet lacks an executable specification or data:

- The even-current worm's complete target-preserving macro-kernel, including extended-ensemble weights and a safe stopping rule, is not supplied.
- No L=2/L=3 current-state enumerator or detailed-balance proof for the physical production kernel is invented.
- The packet's difference-test agreement gates are not reused as equivalence tests; equivalence margins and covariance-aware procedures must be preregistered first.
- The rotating-lattice CSV, result JSON, analysis source, seeds, tie rule, and bootstrap/permutation plan are absent, so its statistics are not recomputed.
- SW-1 remains an integrity-policy concept until a statistic, null law, threshold, dependence treatment, and multiplicity rule are frozen.
- Fixed-reference Wilson-loop labels are not promoted to path-independent global holonomy sectors when plaquette curvature fluctuates.
- The historical `v0_3.py` agent simulation is not silently fused with the three-dimensional Q2 current model; that would be a model substitution, not an upgrade.

## Validation result

The delivered package passes:

- Python 3.12 compilation;
- 26 dependency-free unit tests;
- the built-in end-to-end self-test;
- demo bundle generation and cross-ledger verification; and
- deterministic archive and checksum generation.

Passing these checks validates this reference implementation's stated invariants. It does not validate the underlying physical theory or a production Monte Carlo result.

