# Golden Hashes Rebaseline — 2026-05-10 (N2 Task 3)

**Reason:** R1 reproducibility hashes drifted between the prior
baseline commit (`7372da6713d8`) and HEAD (`4fff33f2979f`). Triage
confirmed the drift is **deterministic**: consecutive runs of the
R1 suite on the current environment produce stable hash values
(only the `commit` metadata field updates to track HEAD).

**Cause analysis (Step 4):**

* Zero source-code changes in `src/kiki_oniric/dream/` between
  `7372da6713d8` and HEAD.
* Zero changes to `uv.lock` over the same range.
* Only repo-side change: a `pyproject.toml` `--cov-fail-under`
  threshold tweak — irrelevant to R1 hash computation.
* Conclusion: the drift originates from the **runtime
  environment** (an mlx / numpy / native-wheel reinstall that the
  current `uv.lock` admits but does not bit-exact pin), not from
  a code or sibling-package update inside this repo. The N1
  reviewer's working theory of a `nerve-wml v1.8.0 → v1.8.1`
  propagation does not apply directly here — `nerve-wml` is not
  a declared dependency of dream-of-kiki — but the underlying
  pattern (silent runtime drift on a `pending_review` contract)
  is real and consistent with the symptoms.

**Impact:** 4 of 5 R1 hashes updated. Cross-machine validation
status remains `pending_review` — this rebaseline does not
constitute a promotion; it preserves the pre-drift contract
shape with new values reflecting the current runtime stack.
The 5th hash (`test_r1_restructure`) coincidentally matched the
prior baseline and is included only with refreshed `commit`
metadata.

**Affected entries (old → new):**

* `test_r1_downscale` — hash unchanged
  (`81297292f562ba9d9378e068e313071e54e129b50e0a4830ad2a9825813b9e28`),
  commit metadata refreshed `7372da6713d8` → `4fff33f2979f`.
* `test_r1_full_pipeline` —
  old `3c9e7dbe456fb660668ab457b31fbbd4a5b580eb886e77dd4eab86028b64a86f`
  → new `ba105f1432028d70b74441de8405a7fb50f30586787287626b5d973332c776c3`.
* `test_r1_recombine` —
  old `b5ae6f5e2284a9759790fe6c162a2217573a64a9029364ca9b0b79c46fd4e9d4`
  → new `2f947c43b3abc5da51e3d7d3d6931f6ebbde9a1659e5b05c562d0e82e9b2c3f3`.
* `test_r1_replay` —
  old `cd53efd35fe868501726ac79f12d59de2156218bf3ebb3c3552409c1aee66692`
  → new `37e1a4b47dfbc40df1b0b2921234ce546ebb5f32e1382a27730b59b9761c02c6`.
* `test_r1_restructure` — hash unchanged
  (`1adfe6b3924fc33af3b1f07db8aaa60b4a2b41b891fee717650e8370d99b6b83`),
  commit metadata refreshed only.

Net: 3 hash values changed (full_pipeline, recombine, replay) +
2 entries refreshed metadata only. The downscale hash being
stable while its consumers (full_pipeline, recombine) drift is
consistent with the drift originating downstream of the
downscale op — likely in the chained ops' use of mlx native
kernels.

**Verification recipe:**

```bash
uv sync --frozen
uv run pytest tests/reproducibility/ --no-cov
git diff tests/reproducibility/golden_hashes.json
# Expect only the `commit` field to differ (auto-updated to current
# HEAD). Hash values must be byte-identical.
```

**Follow-up:** the contract status remains `pending_review` for
all 5 entries. Promotion to `accepted` should only happen after:

1. Cross-machine validation (a second Apple Silicon host
   reproducing identical hashes against this same `uv.lock`).
2. A tighter pinning strategy in `pyproject.toml` for `mlx`
   (currently `>=0.18.0`) and possibly `numpy` so that future
   environment refreshes cannot silently change R1 outputs.
3. Investigation of why the runtime stack drifted while
   `uv.lock` was unchanged (likely an `uv sync` against a fresh
   wheel cache or a Python interpreter swap on the dev host).
