# Q2 — Framework C Conformance Criterion negative tests

**Date pre-registered:** 2026-05-10 (BEFORE building adversarial substrates)
**Spec source:** HYPNEUM-PLANS/specs/2026-05-10-three-innovation-experiments-design.md
**Plan source:** HYPNEUM-PLANS/2026-05-10-niveau8-three-experiments.md (Task 5)
**Status:** Pre-registered, not yet executed.

## H0 (to refute)

The Conformance Criterion is false-positive-safe: no adversarial
substrate constructed to satisfy the axioms passes the criterion.

## Methodology

15 adversarial substrates across 3 categories, each implementing the
`SubstrateAdapter` Protocol (per N5 Task 4 architecture):

- **Cat A (5) — trivial accidents:** Identity, RandomNoise, Lookup,
  FrozenZeros, Constant
- **Cat B (7) — adversarial accidents:** ShapePreservingNoise,
  BudgetGaming, PermutedReplay, OverloadRecombine, StatelessAccident,
  CommutativityViolator, BoundaryCheater
- **Cat C (3) — statistical accidents (N=100 trials each):**
  RandomCoinFlip, ShapeDistributionDependent, SeedDependentSubstrate

Each substrate is run through the full conformance suite
(`tests/conformance/axioms/` + `tests/conformance/invariants/`).
Cat C uses N=100 trials per substrate to measure FP rate.

## Decision criteria (pre-stated)

- **0 FP across 15 substrates** → claim "executable axiom" tient ;
  PR-ready ; Paper 1 §4 defendable as-is
- **1-2 FP** → strengthen affected DR-X with additional invariant ;
  document in §4.5 limitations
- **≥3 FP** → criterion needs reformulation before submit ; scope §4
  narrower (e.g., "candidate executable axiom requiring further
  refinement") ; may need Paper 1 v0.3 plan
