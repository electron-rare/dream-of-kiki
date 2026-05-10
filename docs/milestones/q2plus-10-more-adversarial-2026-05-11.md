# Q2+ — Conformance Criterion negative tests, 10 more adversarial substrates

**Date pre-registered:** 2026-05-11 (BEFORE Q2+ sweep launch)
**Spec source:** HYPNEUM-PLANS/2026-05-11-niveau9-scaling-experiments.md
**N8 cross-reference:** Q2 verdict `ge_3_FP_reformulate` (15/15 substrates pass structural-invariant layer ; commit dream-of-kiki 6ff8320 2026-05-10).
**Status:** Pre-registered, not yet executed.

## H0 (to refute)

The structural-invariant layer of the Conformance Criterion remains 100% FP-vulnerable when extended with 10 more adversarial substrates from new categories not covered by N8 Q2 (Cat A trivial / B adversarial / C statistical). Specifically, ≥24/25 cumulative substrates pass the structural-only audit.

## Methodology

- 10 NEW substrates across 3 new categories (extending N8's A/B/C):
  - **Cat D — modular-arithmetic obfuscation (4)**: Mod7Cycler, Mod13Hasher, BinaryGray, AffineModN
  - **Cat E — replay-loop violators (4)**: ReplayHistorySpoof, BetaPermutationLeak, AlphaInfiniteRecycle, GammaSnapshotRollback
  - **Cat F — asymmetric-channel violators (2)**: AsymReplayHeavy, AsymRecombineEmpty
- Each implements `SubstrateAdapter` Protocol (per N5 architecture, mirrors N8 Cat A/B/C structure)
- Run through same `scripts/run_q2_conformance_audit.py` with N=1 (Cat D, E single trial) and N=100 (any statistical Cat F variants if applicable)
- Cumulative pool: N8 15 + N9 10 = 25 substrates total
- Launch on **grosmac** local (no GPU needed, audit harness CPU-only ~10s per substrate)

## Decision criteria (pre-stated)

- **Structural-layer-100%-FP-vulnerable:** all 10 new substrates pass → 25/25 total → C2 absolutely required, Paper 1 §5.8 strengthened with "validated against 25 adversarial substrates from 6 categories".
- **Some-discrimination:** 7-9 of 10 new pass (22-24/25 total) → §5.8 nuanced "structural layer catches some categories but not others ; C2 required for full coverage".
- **Strong-discrimination:** ≤6 of 10 new pass (≤21/25 total) → §5.8 substantially refined "structural layer has more discriminative power than N8-Q2 sample suggested ; C2 required only for specific category-X failures" — would require Paper 1 v0.3 plan.
