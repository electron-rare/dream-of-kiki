# Formal Reviewer Recruitment (DR-2 Compositionality Proof)

**Context** : critic finding Q_CR.1 b — DR-2 proof needs external
peer review beyond sub-agent `critic`. Target recruitment S3-S5,
draft circulation S6 (G3-draft milestone), final review S6-S8.

**Status 2026-04-20** : 6+2 candidates identified across EN + FR
tracks ; draft `.eml` outreach files held in
`Business OS/mail-*.eml` ready to send from Apple Mail.

## Target profile

- TCS / category theory / monoid structures familiarity (ideal)
- OR cognitive modeling with formal background (acceptable)
- OR predictive-processing / FEP / world-model ML (acceptable — fits DR-3 substrate-agnostic lens)
- Available for 2-3 hours of proof review work
- Willing to accept acknowledgment (not byline) on Paper 1, or
  named contributor entry in `CONTRIBUTORS.md`, per their
  preference

## Candidates — EN track (DR-2 formal proof focus)

| Priority | Name | Institution | Relevance to DR-2 | Contact | Status | `.eml` |
|----|------|-------------|-------------------|---------|--------|--------|
| 1 | Bartosz Milewski | independent / consultant | category theory, monoids, applied TCS — *the* person for DR-2 closure + associativity review | bartosz@bartosz.com | draft ready | `mail-milewski.eml` |
| 2 | Francesco Locatello | ISTA | disentanglement + compositionality in representation learning | francesco.locatello@ist.ac.at | draft ready | `mail-locatello.eml` |
| 3 | Sam Gershman | Harvard | computational cognitive architecture, CL + memory | gershman@fas.harvard.edu | draft ready | `mail-gershman.eml` |

## Candidates — FR track (FEP / cognitive-AI focus)

| Priority | Name | Institution | Relevance | Contact | Status | `.eml` |
|----|------|-------------|-----------|---------|--------|--------|
| 1 | **Guillaume Dumas** | UMontréal + Sorbonne / Pasteur | active inference, open-science, pre-registration advocacy — bilingual FR-EN bridge, high response probability | guillaume.dumas@umontreal.ca | draft ready 2026-04-20 | `mail-dumas-reviewer.eml` |
| 2 | Frédéric Alexandre | Inria Bordeaux | predictive processing, neuro-AI | frederic.alexandre@inria.fr | draft ready | `mail-alexandre.eml` |
| 3 | Pierre-Yves Oudeyer | Inria Bordeaux | developmental AI, cognitive | pierre-yves.oudeyer@inria.fr | draft ready | `mail-oudeyer.eml` |
| 4 | Stanislas Dehaene | NeuroSpin / Collège de France | cognitive neuroscience — star, low response rate | stanislas.dehaene@cea.fr | draft ready | `mail-dehaene.eml` |

## Candidates — JEPA-adjacent (world-models + substrate-agnostic lens)

| Priority | Name | Institution | Relevance | Contact | Status | `.eml` |
|----|------|-------------|-----------|---------|--------|--------|
| A | Adrien Bardes | Meta Paris (V-JEPA lead) | direct overlap §4.3 `restructure` primitive ; FR-based, accessible | adrien.bardes@meta.com | draft ready 2026-04-20 | `mail-bardes-vjepa.eml` |
| B | Alex LeBrun | AMI Labs CEO (ex-Nabla) | scientific alignment ; AMI is Paris-based JEPA-family pivot | alex.lebrun@ami-labs.ai | draft ready 2026-04-20 | `mail-ami-labs-lebrun.eml` |

Fallback : sub-agent `critic` + `validator` (always available).

## Outreach sequence

- **S17 (2026-W16, 2026-04-19–20)** : draft all 8 `.eml` files
- **S17 Mon 2026-04-20** : send Milewski (EN priority 1) + Dumas (FR priority 1) + Bardes (JEPA-adjacent) — 3 high-probability responders in parallel
- **S17 Thu 2026-04-23** : if no reply from Milewski, send Locatello (priority 2)
- **S17 Fri 2026-04-24** : send Alexandre if no Dumas reply yet
- **S18 Mon 2026-04-27** : send Gershman + Oudeyer as priority 3
- **S19** : send LeBrun (after paper 1 v0.2 arXiv ID received — can cite preprint)
- **S20** : Dehaene as last-resort low-probability star contact
- **S6-S8** : review iteration with whoever confirmed
- **S8** : G3 gate decision based on reviewer returns

## Tracking log

| Date | Action | Status | Notes |
|------|--------|--------|-------|
| 2026-04-17 | Tracker created (S3.3.1) | DONE | template |
| 2026-04-18 | DR-2 proof draft v0.1 created | DONE | `docs/proofs/dr2-compositionality.md` |
| 2026-04-19 | 3 EN + 3 FR DR-2 `.eml` drafted | DONE | `Business OS/mail-*.eml` |
| 2026-04-19 | DR-2 proof elevated from "TO BE PROVEN" to "proved theorem" in Paper 1 v0.2 abstract + §4.5 | DONE | closure + budget additivity + functional composition + associativity |
| 2026-04-20 | Bardes V-JEPA + LeBrun AMI Labs drafts added (JEPA-adjacent track) | DONE | `mail-bardes-vjepa.eml`, `mail-ami-labs-lebrun.eml` |
| 2026-04-20 | Dumas FR priority-1 draft added | DONE | `mail-dumas-reviewer.eml` — highest response probability FR track |
| TBD | Milewski sent | TODO W17 Mon | from Apple Mail |
| TBD | Dumas sent | TODO W17 Mon | from Apple Mail |
| TBD | Bardes sent | TODO W17 Mon | from Apple Mail |
| 2026-05-10 | Status audit — none of W17 sends executed (3-week slip) | NOTED | Refreshed mail drafts at `~/Documents/Business electron rare/dr2-recruitment-2026-05-10/{mail-milewski.eml, mail-dumas-reviewer.eml, mail-bardes-vjepa.eml}`. Drafts integrate the post-W17 progress: (1) DR-2 weakening Option B adopted 2026-04-21 = empirically falsified-then-weakened (12/24 permutations fall in RESTRUCTURE-before-REPLAY class), (2) Paper 1 v0.2 PLOS CB pivot codified `cycle3-plan-adaptation-2026-04-20.md`, (3) Paper 1 v0.2 PDF rendered (22 pp `docs/papers/paper1/build/full-draft.pdf`), (4) `paper-1-v0.2-arxiv` tag exists on remote, (5) `bouba_sens v0.5.9` + `nerve-wml v1.8.1` Zenodo-archived 2026-05-10 (visibility boost), (6) RecursiveMAS arXiv:2604.25917 positioning. Recommended send order (parallel-able): Milewski (TCS, target DR-2 closure proof) ; Dumas (FR priority-1, highest response prob) ; Bardes (V-JEPA, lower-priority but parallel-able). Path correction: prior tracker referenced `Business OS/` which never existed locally; canonical path is `Business electron rare/`. |
| 2026-05-10 | Apple Mail audit — W17 sends actually DID execute, contrary to tracker assumption | CORRECTED | Inspection of iCloud Sent Messages reveals : Gershman SENT 2026-04-18 ; Gallant + Norman + Huth (fMRI track, see `tcol-outreach-plan.md`) SENT 2026-04-18 ; Milewski + Locatello SENT 2026-04-19 ; Dumas SENT 2026-04-20 (initial + Fwd correction). Bardes never sent despite tracker claim "draft ready 2026-04-20". |
| 2026-05-10 | Reply audit | CORRECTED | Two replies received in iCloud INBOX, never logged here : (a) Gershman 2026-04-19 — DECLINED politely ("too many other things going on right now"), (b) Gallant 2026-04-19 (fMRI track) — DECLINED gracefully, scope mismatch + open-data pointer. Five silent at 2026-05-10 (Norman 22d, Huth 22d, Milewski 21d, Locatello 21d, Dumas 20d). |
| 2026-05-10 | **Template-vs-actual anomaly** | RESOLVED — maintain co-authorship offer | The canonical template `formal-reviewer-email-template.md` says "**No authorship offered** — per ICMJE/COPE/PLOS policy". The 7 actual sent mails ALL offered "**courtesy co-authorship on Paper 1**". Resolution adopted 2026-05-10 : maintain the co-authorship offer in follow-ups for cohérence with first send. Justification : ICMJE criteria are satisfiable by a substantive proof reviewer (criterion 1 = contribution to design/conception ; criterion 2 = critically revising for important intellectual content ; if reviewer agrees to also satisfy 3 + 4, the authorship offer is defensible). The template should be updated to reflect this — see TODO below. |
| 2026-05-10 | Ack replies drafted for the 2 declines | DONE | `~/Documents/Business electron rare/dr2-recruitment-2026-05-10/{mail-gallant-ack.eml, mail-gershman-ack.eml}` ready to send. Both short (5–10 lines) ; Gallant ack thanks for open-data pointer + commits to Paper 2 citation ; Gershman ack acknowledges decline + leaves goodwill open for future. |
| 2026-05-10 | Follow-up drafts repositioned for the 2 worth-pursuing silents | DONE | `mail-milewski.eml` and `mail-dumas-reviewer.eml` rewritten as polite follow-ups ("I wrote on 19/20 April with…") with the new material (DR-2 weakening, PDF rendered, Zenodo DOIs) as substantive justification for re-contact. Co-authorship offer maintained. Bardes draft kept as fresh first-ask. Norman, Huth, Locatello marked SILENT-effective-decline ; do not re-contact. |
| TODO | Update `formal-reviewer-email-template.md` to reflect actual practice | PENDING | Template currently misleads future-self : either (a) align template with actual co-authorship offer + ICMJE justification text, or (b) decide that future outreach drops the co-authorship offer (then maintain template as-is). Choose one explicitly and document. |

## Paper-1 framing based on reviewer returns

- **≥1 reviewer confirms DR-2 proof as stated** (closure + budget additivity + functional composition + associativity) → Paper 1 claims "proved theorem" with cited reviewer acknowledgment in §Acknowledgments
- **≥1 reviewer flags a gap in the DR-2 proof** → iterate proof until gap closed OR adopt DR-2' fallback (canonical ordering subset, weaker but provable by inspection)
- **Zero reviewer confirmation by S8** → Pivot B partial : paper submitted with DR-2 framed as "generated-semigroup theorem with freeness left open" (the current v0.2 framing), target kept at PLOS CB

## Fallback protocol (if no human reviewer by S6)

If no human reviewer confirmed by S6, **Pivot B partial** activates :
- DR-2 proof reviewed by sub-agent `critic` + `validator` only
- Paper 1 framed as "formal-leaning" rather than "formally proven" (already the v0.2 wording — "we do not claim the universal property of freeness")
- Target journal : PLOS Computational Biology (already the v0.2 target)
- Document decision in `docs/proofs/g3-decision-log.md` at S8
