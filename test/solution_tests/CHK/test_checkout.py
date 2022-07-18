import pytest
from typing import Tuple, Any
from lib.solutions.CHK import checkout_solution


class TestCheckout:
    @pytest.mark.parametrize("inputs", [("4A2B2E", 275), ("AAA", 130), ("", 0), ("3A2BC2A", 295)])
    def test_checkout_round_1(self, inputs: Tuple[Any, int]) -> None:
        result = checkout_solution.checkout(inputs[0])
        assert result == inputs[1]

    def test_checkout_round_1_fail(self) -> None:
        result = checkout_solution.checkout(123)
        assert result == -1

    def test_split_str_number(self) -> None:
        result = checkout_solution.split_sku_str_number("3AB2C")
        assert result[0][1] == 3

    def test_symbols_input(self) -> None:
        result = checkout_solution.checkout("-")
        assert result == -1


