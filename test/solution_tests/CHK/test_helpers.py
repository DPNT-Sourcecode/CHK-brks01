import pytest
from typing import Tuple, Any
from lib.solutions.utils import checkout_helpers


class TestCheckoutHelpers:
    def test_split_sku_str_number_success(self) -> None:
        result = checkout_helpers.split_sku_str_number("3AB2C")
        assert result[0][1] == 3

    def test_get_sku_price_success(self) -> None:
        assert checkout_helpers.get_sku_price("A") == 50
