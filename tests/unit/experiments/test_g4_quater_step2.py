"""Smoke + structural tests for the G4-quater Step 2 driver."""
from __future__ import annotations

from pathlib import Path

import pytest

from experiments.g4_quater_test.run_step2_restructure_sweep import (
    ARMS,
    RESTRUCTURE_FACTORS,
    run_pilot,
)

# H3 fix (N2 plan, 2026-05-10): the FMNIST data directory is gitignored
# (raw IDX files; not committed). Convert "data missing" from a hard
# failure into a clean skip so a fresh clone reports green by default
# and surfaces this as a "data prerequisite" rather than a code bug.
_FMNIST_DATA = (
    Path(__file__).resolve().parents[3]
    / "experiments"
    / "g4_split_fmnist"
    / "data"
)
_SKIP_IF_NO_FMNIST = pytest.mark.skipif(
    not _FMNIST_DATA.exists(),
    reason=(
        f"FMNIST raw IDX files not present at {_FMNIST_DATA}; "
        "download the 4 Fashion-MNIST IDX files (train/test, "
        "images/labels) from "
        "https://github.com/zalandoresearch/fashion-mnist/tree/master/data/fashion "
        "into that directory before running this pilot. "
        "The loader at experiments/g4_split_fmnist/dataset.py "
        "expects the standard IDX layout."
    ),
)


def test_constants_match_prereg() -> None:
    assert ARMS == ("baseline", "P_min", "P_equ", "P_max")
    assert RESTRUCTURE_FACTORS == (0.85, 0.95, 0.99)


@_SKIP_IF_NO_FMNIST
def test_run_pilot_smoke(tmp_path: Path) -> None:
    data_dir = _FMNIST_DATA
    out_json = tmp_path / "step2.json"
    out_md = tmp_path / "step2.md"
    registry_db = tmp_path / "registry.sqlite"
    payload = run_pilot(
        data_dir=data_dir,
        seeds=(0,),
        factors=(0.95,),
        out_json=out_json,
        out_md=out_md,
        registry_db=registry_db,
        epochs=1,
        batch_size=64,
        lr=0.01,
        smoke=True,
    )
    assert len(payload["cells"]) == len(ARMS)
    for cell in payload["cells"]:
        assert "run_id" in cell
        assert cell["restructure_factor"] == 0.95
    assert out_json.exists()
    assert out_md.exists()
