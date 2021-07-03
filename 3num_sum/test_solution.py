# Run: pytest test_solution.py

from solution import Solution
import pytest

class TestThreeSum:
    def setup(self):
        self.soln = Solution()

    def test_three_sum(self):
        a = [1, 2, -1, 0, 0, -2]
        t = 0
        assert self.soln.threeSum(a, t) == [[-2, 0, 2], [-1, 0, 1]]

    def test_three_sum2(self):
        a = [12, 3, 1, 2, -6, 5, -8, 6]
        t = 0
        assert self.soln.threeSum(a, t) == [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

    def test_three_sum3(self):
        a = [1, 2, 3]
        t = 6
        assert self.soln.threeSum(a, t) == [[1, 2, 3]]

    def test_three_sum4(self):
        a = [12, 3, 1, 2, -6, 5, -8, 0, -8, -1, 6]
        t = 0
        assert self.soln.threeSum(a, t) == [[-8, 2, 6], [-8, 3, 5], [-6, 0, 6], [-6, 1, 5], [-1, 0, 1]]

    def test_three_sum5(self):      
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
        t = 5
        assert self.soln.threeSum(a, t) == []