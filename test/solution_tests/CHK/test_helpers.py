from lib.solutions.utils import checkout_helpers


class TestCheckoutHelpers:
    def test_split_sku_str_number(self) -> None:
        result = checkout_helpers.split_sku_str_number("3AB2C")
        assert result[0][1] == 3




