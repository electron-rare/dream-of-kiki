"""Task 1: SubstrateAdapter Protocol + CellRequest dataclass."""

from pathlib import Path

from kiki_oniric.substrates.factory import (
    CellRequest,
    SUBSTRATE_NAMES,
    SubstrateAdapter,
)


def test_cell_request_fields():
    req = CellRequest(
        substrate="mlx_kiki_oniric",
        profile="p_equ",
        seed=7,
        scale="qwen3p6-35b-bf16-local",
        model_path=Path("/fake/path"),
        benchmarks=("mmlu", "hellaswag", "mega_v2"),
    )
    assert req.seed == 7
    assert req.substrate in SUBSTRATE_NAMES


def test_substrate_names_is_3_tuple():
    assert SUBSTRATE_NAMES == (
        "mlx_kiki_oniric",
        "esnn_thalamocortical",
        "micro_kiki",
    )


def test_substrate_adapter_protocol_is_runtime_checkable():
    # Protocol is structural -- any object with the two methods satisfies it.
    class Dummy:
        def execute_profile(self, request):
            return {}

        def teardown(self):
            pass

    d = Dummy()
    # Static check: Protocol methods exist
    assert callable(getattr(d, "execute_profile"))
    assert callable(getattr(d, "teardown"))
    # Import path reachable
    assert SubstrateAdapter is not None
