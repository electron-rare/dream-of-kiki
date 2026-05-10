"""Smoke + structural tests for the G4-quater Step 1 driver."""
from __future__ import annotations

from pathlib import Path

import pytest

from experiments.g4_quater_test.run_step1_deeper import (
    ARMS,
    HIDDEN,
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
        f"FMNIST raw data not present at {_FMNIST_DATA}; "
        "fetch via experiments/g4_split_fmnist/fetch_data.sh "
        "(or equivalent in that experiment dir) before running this pilot."
    ),
)


def test_constants_match_prereg() -> None:
    assert ARMS == ("baseline", "P_min", "P_equ", "P_max")
    assert HIDDEN == (64, 32, 16, 8)


@_SKIP_IF_NO_FMNIST
def test_run_pilot_smoke(tmp_path: Path) -> None:
    data_dir = _FMNIST_DATA
    out_json = tmp_path / "step1.json"
    out_md = tmp_path / "step1.md"
    registry_db = tmp_path / "registry.sqlite"
    payload = run_pilot(
        data_dir=data_dir,
        seeds=(0,),
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
        assert "retention" in cell
    assert out_json.exists()
    assert out_md.exists()
