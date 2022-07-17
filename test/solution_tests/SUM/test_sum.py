from lib.solutions.SUM import sum_solution


class TestSum:
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3
        
    def test_sum_negative_integers(self):
        assert sum_solution.compute(-1, 3) == 0


