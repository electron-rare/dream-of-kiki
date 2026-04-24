"""Substrate factory unifying divergent substrate ABIs behind one Protocol.

The three cycle-3 substrates have incompatible handler signatures:

- ``mlx_kiki_oniric``: operates on ``DreamEpisode`` via ``_real`` ops,
  mutates MLX weights in-place.
- ``esnn_thalamocortical``: numpy-native, ``NDArray`` in/out.
- ``micro_kiki``: OPLoRA adapter dicts (stub) or SpikingKiki-V4 real
  backend (env-gated).

This factory wraps each behind a unified ``SubstrateAdapter`` consumable
by ``DreamRuntime.execute()``.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal, Protocol, Sequence


SUBSTRATE_NAMES: tuple[str, ...] = (
    "mlx_kiki_oniric",
    "esnn_thalamocortical",
    "micro_kiki",
)


SubstrateName = Literal["mlx_kiki_oniric", "esnn_thalamocortical", "micro_kiki"]


@dataclass(frozen=True)
class CellRequest:
    """One ablation cell = (substrate, profile, seed, scale, model_path)."""

    substrate: SubstrateName
    profile: str
    seed: int
    scale: str
    model_path: Path
    benchmarks: Sequence[str] = field(
        default_factory=lambda: ("mmlu", "hellaswag", "mega_v2")
    )


class SubstrateAdapter(Protocol):
    """Unified Protocol for all cycle-3 substrates."""

    def execute_profile(self, request: CellRequest) -> dict:
        """Run pre-eval -> dream ops (profile-ordered) -> post-eval.

        Returns raw cell metrics dict.
        """
        ...

    def teardown(self) -> None:
        """Release MLX Metal buffers / close files."""
        ...
