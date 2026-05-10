# Paper 2 — Outline (post-PLOS-CB pivot, 2026-05-10)

**Target venue** : NeurIPS (primary) / ICML / TMLR (fallbacks).
Cognitive Science journal kept as a secondary track if the
empirical fMRI angle dominates.
**Format** : 9 pages main + supplementary unbounded.
**Word target** : ~5500 words main.
**Re-spec rationale** : the original cycle-2 outline (S27.1) is
superseded. The 2026-04-20 PLOS CB pivot
(`docs/milestones/cycle3-plan-adaptation-2026-04-20.md`) moved
multi-scale empirical work, Norse cross-substrate, fMRI Studyforrest,
and Gate D verdict from cycle-3 closeout into the Paper 2 backlog.
This file rewrites the outline accordingly.

---

## 1. Abstract (200 words target)

Engineering-and-empirical contribution : substrate-agnostic
dream-based consolidation framework with executable Conformance
Criterion, demonstrated across **four substrates** (MLX
`kiki_oniric`, E-SNN thalamocortical, `micro_kiki` MoE-LoRA, Norse
spiking) and **three model scales** (Qwen3.5-1.5B, Qwen3.5-7B,
Qwen3.6-35B-A3B). Key contributions : (1) `SubstrateAdapter`
Protocol unifying divergent substrate ABIs behind one runtime ;
(2) cross-substrate Conformance Criterion validation matrix ;
(3) cross-scale empirical scaling law on H1–H4 hypotheses with
Bonferroni control ; (4) cross-modal validation against
Studyforrest fMRI BOLD via HMM dream-state alignment + CCA. Ground-
truth supervision uses the OSF pre-registered protocol from cycle 1
(amendment 2026-04-23 covers the multi-scale extension).

## 2. Introduction (~1 page)

- Engineering problem : reproducible AI consolidation across
  hardware substrates **and** model scales
- Empirical problem : do `kiki_oniric` profile-chain effects survive
  scale, substrate, and biological cross-modal validation ?
- Practical motivation : enable researchers to validate framework
  claims on their own substrates without re-deriving the theory
- Contribution roadmap (4 numbered items as in §1)

## 3. Background (~0.75 pages)

- Reference Paper 1 (PLOS CB submission, framework C, axioms
  DR-0..DR-4 with the 2026-04-21 DR-2 weakening amendment) for the
  formal foundation. Paper 2 cites Paper 1 by tag, never by
  content.
- Cite SHY (Tononi 2014), FEP (Friston 2010), CLS (McClelland 1995),
  brain-inspired replay (van de Ven 2020).
- **Concurrent work paragraph** (§3.x) : RecursiveMAS
  (Yang et al., arXiv:2604.25917, 2026-04-28) — independent
  derivation of latent-shared-state architecture for heterogeneous
  multi-component systems. Cite as convergent evidence ;
  differentiate by substrate / gating / falsifiability scope.
  See `rebuttal-pocket-recursivemas.md` for the rebuttal-ready
  position statement and the three-axis differentiation table.

## 4. Conformance Criterion in Practice (~1.5 pages)

- 4.1 Three conditions recap (signature typing via
  `SubstrateAdapter` Protocol ; axiom property tests DR-0..DR-4 ;
  BLOCKING invariants S1/S2/S3/I-family enforceable at runtime).
- 4.2 MLX `kiki_oniric` substrate conformance verification.
- 4.3 E-SNN thalamocortical substrate conformance verification
  (G7 LOCKED).
- 4.4 `micro_kiki` substrate conformance verification (G8 LOCKED ;
  MoE-LoRA recombine handler via TIES-merge per `recombine_handler_factory`).
- 4.5 Norse spiking substrate conformance verification (cycle-3
  C3.11/C3.12 wrappers DONE).
- 4.6 Reusable test artefact : `tests/conformance/` as a contract
  any third-party substrate can target.

## 5. Engineering Architecture (~1.5 pages)

- 5.1 `SubstrateAdapter` Protocol unifying four divergent ABIs
  behind a single `DreamRuntime.execute()` entry point
  (commits `9852817` + `428d7a2`).
- 5.2 Operations as composable handlers (replay, downscale,
  restructure, recombine — substrate-specific implementations
  share the canonical signature set).
- 5.3 Swap protocol with S1 retained-eval gating, S2 finite guard,
  S3 topology guard.
- 5.4 Concurrent dream worker (real asyncio, cycle-2 promotion).
- 5.5 Run registry with deterministic R1 contract (32-hex SHA-256
  prefix, multi-artifact support, per-artifact hash
  registration via `register_output_hash`).

## 6. Methodology (~1 page)

- 6.1 OSF pre-registration (cycle-1 hypotheses H1-H4 retained ;
  amendments 2026-04-21 DR-2 weakening + 2026-04-23 multi-scale
  extension).
- 6.2 Statistical pipeline (Welch / TOST / Jonckheere /
  one-sample t with Bonferroni ; cross-scale joint-test pipeline).
- 6.3 mega-v2 stratified retained benchmark (500 items, SHA-256
  frozen, common across scales and substrates).
- 6.4 Cross-substrate measurement protocol via
  `SubstrateAdapter.execute_profile`.
- 6.5 Cross-scale measurement protocol (1.5B → 7B → 35B Qwen
  family + scaling-law fit per `scaling-law-analysis-2026-04-20.md`).
- 6.6 Cross-modal validation : Studyforrest BOLD loader
  (C3.15 DONE), HMM dream-state alignment (C3.16 DONE), CCA between
  artificial and biological consolidation trajectories.

## 7. Results (~2 pages)

- 7.1 MLX `kiki_oniric` substrate ablation (Phase B 1.5B sanity
  GO 3/3 from `pilot-cycle3-real-1p5b.json` + Phase B 7B and 35B
  from C3.8 multi-scale runs).
- 7.2 E-SNN thalamocortical ablation (cycle-2 G9 closeout data).
- 7.3 `micro_kiki` substrate ablation (G8 closeout data + recombine
  handler validation per `[C-v0.10.0+PARTIAL]`).
- 7.4 Norse spiking cross-substrate pilot
  (C3.13 reactivation via `pilot_phase2b_neuromorph.py`, 624 LOC
  driver preserved with deferred-note header).
- 7.5 Cross-substrate consistency matrix (profile chain effect
  size and direction across the four substrates).
- 7.6 Cross-scale scaling-law analysis (1.5B → 7B → 35B effect-size
  fit, Bonferroni-corrected H1–H4 outcomes).
- 7.7 Cross-modal Studyforrest result (C3.18 G10c report).
- 7.8 **Gate D verdict** on H1–H4 (the deferred multi-scale
  decision the cycle-3 plan promised).

## 8. Discussion (~1 page)

- 8.1 Reproducibility validated across four substrates and three
  scales.
- 8.2 Engineering trade-offs (MLX speed vs E-SNN energy vs
  Norse biological fidelity vs micro_kiki MoE deployability).
- 8.3 Cross-modal Studyforrest result interpretation (artificial
  consolidation aligns with which BOLD dream-state HMM clusters ?).
- 8.4 Comparison with Paper 1 theoretical claims (cite Paper 1
  by published tag once the arXiv ID lands).
- 8.5 Position vs. RecursiveMAS — convergence on shared-latent-state
  intuition, divergence on substrate / gating / falsifiability.
- 8.6 Limitations (transformer-only ; no on-line continual setting ;
  Studyforrest is a single dataset).

## 9. Future Work (~0.5 pages)

- 9.1 Additional substrates (true RWKV, state-space S6, on-device
  Foundation Models).
- 9.2 Dynamic profile selection at runtime guided by the
  cross-modal HMM signal.
- 9.3 Continual-learning regime (current pipeline is offline batch).
- 9.4 Multi-subject Studyforrest validation (current C3.18 plan
  focuses on the public BOLD subset).

## 10. References

Inherits from Paper 1 `references.bib` plus :
- `recursivemas2026` (concurrent work, added 2026-05-10)
- `nerve-wml` v1.8.0 Zenodo version-DOI (mintage in flight)
- Norse spiking framework citation
- Studyforrest dataset citation
- HMM + CCA methodological citations
- micro-kiki LoRA-stack citation (parent project tag)

---

## Differentiation from Paper 1

| Aspect | Paper 1 (PLOS CB) | Paper 2 (Eng+Empirical) |
|--------|-------------------|-------------------------|
| Scope | Formal framework C | Engineering+empirical realisation |
| Target venue | PLOS Computational Biology | NeurIPS / ICML / TMLR |
| Audience | Cognitive scientists + theorists | ML engineers + systems researchers + computational neuroscientists |
| Substrates covered | 1 (kiki-oniric MLX, sketched) | 4 (MLX + E-SNN + micro_kiki + Norse) |
| Model scales | 1 (1.5B sanity only) | 3 (1.5B + 7B + 35B Qwen family) |
| Length | ~5000 words | ~5500 words |
| Formal proofs | DR-0..DR-4 in main, DR-2 amended | Reference Paper 1 by tag |
| Reproducibility focus | Pre-registration + R1 contract | Cross-substrate × cross-scale validation matrix |
| Cross-modal validation | Out of scope | In scope via Studyforrest BOLD + HMM + CCA |
| Open-source emphasis | Conceptual | Operational (`SubstrateAdapter` Protocol + 4-substrate Conformance suite) |

---

## Paper 2 deferred backlog (source : cycle-3 plan adaptation)

Per `docs/milestones/cycle3-plan-adaptation-2026-04-20.md`, six
items moved from cycle-3 closeout into Paper 2 :

1. **C3.8** — full multi-scale ablation 1.5B + 7B + 35B
   (PARTIAL : 1.5B done as Phase B, commit `22c58c9`).
2. **C3.9** — Gate D verdict (multi-scale H1–H4).
3. **C3.13** — Norse vs MLX cross-substrate pilot
   (driver `scripts/pilot_phase2b_neuromorph.py`, 624 LOC).
4. **C3.14** — G10a milestone (cross-substrate ordering).
5. **C3.18** — G10c fMRI report (Studyforrest pipeline ready).
6. **C3.19–C3.22** — Paper 2 narrative authoring (this file +
   sections).

Re-spec window opens **after** Paper 1 v0.2 lands its arXiv ID.
The tag `paper-1-v0.2-arxiv` already exists on the remote — the
window is therefore conceptually open as of 2026-05-10.

---

## Reactivation timeline (rough, post Paper 1 submit)

Counting from the day Paper 1 v0.2 submission lands :

- **Week 1** : final paper2/outline.md + abstract.md + paper2-fr/
  mirror reconciled.
- **Weeks 2-4** : C3.8 multi-scale 7B + 35B runs on MacStudio
  (wallclock budget : verify against current Studio allocation
  for eu-kiki + Zacus inference).
- **Week 5** : C3.9 Gate D verdict report.
- **Week 6** : C3.13 Norse pilot reactivation + run.
- **Weeks 7-8** : C3.18 G10c fMRI Studyforrest run + report.
- **Weeks 9-12** : draft sections 4 → 8 with results in hand.
- **Week 13** : pre-submission internal review (critic agent on
  full draft per `feedback_critic_before_ship.md`).
- **Weeks 14-15** : submission window (NeurIPS / ICML / TMLR
  depending on calendar).

---

## Cross-cutting dependencies

- **Paper 1 v0.2 tag** must be on arXiv with a stable ID before
  Paper 2 cites it (per `docs/papers/CLAUDE.md` pinning rule —
  no `HEAD`, only tags).
- **`nerve-wml v1.8.0` Zenodo version-DOI** must be minted before
  Paper 2 cites the cross-substrate measurement (currently
  in-flight ; concept-DOI 10.5281/zenodo.19656342 is a fallback).
- **`bouba_sens` benchmark** : if the §6.6 cross-modal narrative
  references the Amedi B-1 dose-response curve, cite by
  `bouba_sens` Zenodo version-DOI (mintage planned alongside
  TMLR submission).
- **OSF amendment** for cycle-3 multi-scale extension already
  filed as `osf-amendment-bonferroni-cycle3.md` (Bonferroni
  correction adapted for the multi-scale joint test).

---

## Notes

- This outline supersedes the cycle-2 amorçage version (S27.1).
  The original is preserved in git history at the previous
  commit on this file.
- Outline subject to revision based on Paper 1 v0.2 reviewer
  feedback (PLOS CB) and Gate D verdict outcome.
- Paper 3 (provisional banner per `docs/papers/CLAUDE.md`) is
  intentionally out of scope here ; do not flesh out before
  cycle-3 kickoff and Paper 2 closeout.
- EN→FR propagation : every change to this file requires a
  matching update of `docs/papers/paper2-fr/outline.md` in the
  same PR (per `CONTRIBUTING.md`).
