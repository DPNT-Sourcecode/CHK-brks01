from lib.solutions.CHK import checkout_solution


class TestCheckout:
    def test_checkout_round_1(self) -> None:
        result = checkout_solution.checkout("2A3C")
        assert result == 160

    def test_checkout_round_1_fail(self) -> None:
        result = checkout_solution.checkout("2A3C")
        assert result == -1
