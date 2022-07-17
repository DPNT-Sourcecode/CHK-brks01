from lib.solutions.CHK import checkout_solution


class TestCheckout:
    def test_checkout_round_1(self) -> None:
        result = checkout_solution.checkout("2a3c")
        assert result == 160

    def test_checkout_round_1_fail(self) -> None:
        result = checkout_solution.checkout(123)
        assert result == -1

    def test_split_str_number(self) -> None:
        result = checkout_solution.split_sku_str_number("3AB2C")
        assert result[0][1] == 3


