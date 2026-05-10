"""micro_kiki substrate package.

Split from monolithic ``micro_kiki.py`` (1188 LOC) by N5 Tasks
4-7 (M2 audit). Public API preserved via the re-exports below ;
existing call sites
``from kiki_oniric.substrates.micro_kiki import X`` keep working.

Task 4 (2026-05-10) — extracted the 4 op-handler factories into
:mod:`.handlers` (as a mixin so ``MicroKikiSubstrate`` still
exposes them as methods, per the DR-3 Conformance Criterion
contract).

Task 5 (2026-05-10) — extracted the OPLoRA projector helper into
:mod:`.oplora`. Tasks 6-7 will peel TIES-Merge and the safetensors
loaders out of :mod:`._legacy` ; until then those helpers + the
substrate class stay in the holding file and are re-exported here.
"""
from __future__ import annotations

# OPLoRA projector (Task 5 — :mod:`.oplora`) and TIES-Merge
# (Task 6 — :mod:`.ties`). Imported BEFORE :mod:`._legacy` so
# the explicit bindings win over the legacy back-compat re-exports.
from kiki_oniric.substrates.micro_kiki.oplora import (  # noqa: F401
    _oplora_projector,
)
from kiki_oniric.substrates.micro_kiki.ties import (  # noqa: F401
    _ties_merge,
)

# Constants + helpers (still in :mod:`._legacy` until Task 7)
from kiki_oniric.substrates.micro_kiki._legacy import (  # noqa: F401
    MICRO_KIKI_SUBSTRATE_NAME,
    MICRO_KIKI_SUBSTRATE_VERSION,
    MicroKikiRecombineState,
    MicroKikiRestructureState,
    MicroKikiSubstrate,
    _REAL_BACKEND_ENV_VAR,
    _REAL_BACKEND_PATH_ENV_VAR,
    _real_backend_enabled,
    _real_backend_path_from_env,
    _try_load_safetensors,
    micro_kiki_substrate_components,
)

# Handler factories (Task 4 — :mod:`.handlers`)
from kiki_oniric.substrates.micro_kiki.handlers import (  # noqa: F401
    MicroKikiHandlersMixin,
)

__all__ = [
    "MICRO_KIKI_SUBSTRATE_NAME",
    "MICRO_KIKI_SUBSTRATE_VERSION",
    "MicroKikiHandlersMixin",
    "MicroKikiRecombineState",
    "MicroKikiRestructureState",
    "MicroKikiSubstrate",
    "_REAL_BACKEND_ENV_VAR",
    "_REAL_BACKEND_PATH_ENV_VAR",
    "_oplora_projector",
    "_real_backend_enabled",
    "_real_backend_path_from_env",
    "_ties_merge",
    "_try_load_safetensors",
    "micro_kiki_substrate_components",
]
