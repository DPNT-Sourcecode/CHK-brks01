import pytest
from typing import Tuple, Any
from lib.solutions.CHK import checkout_solution


class TestCheckout:
    @pytest.mark.parametrize("inputs", [("4A2B2E", 275), ("AAA", 130), ("", 0), ("3A2BC2A", 265)])
    def test_checkout_round_1(self, inputs: Tuple[Any, int]) -> None:
        assert checkout_solution.checkout(inputs[0]) == inputs[1]

    def test_checkout_round_1_fail(self) -> None:
        assert checkout_solution.checkout(123) == -1

    def test_symbols_input(self) -> None:
        assert checkout_solution.checkout("-") == -1



