from lib.solutions.HLO import hello_solution


class TestHello:
    def test_hello(self) -> None:
        assert hello_solution.hello("felix") == "Hello, felix!"

    def test_hello_fail(self) -> None:
        assert hello_solution.hello("") == "None"
