"""
    Run: pytest test_solution.py
"""

import pytest
from solution import Solution

class TestDuplicate:

    def setup(self):
        self.soln = Solution()

    def test_duplicate(self):
        input = [1, 2, 4, 6, 2, 4, 7]
        assert self.soln.getFirstDuplicate(input) == 2

    def test_duplicate2(self):
        input = [11, 22, 14, 26, 12, 4, 7]
        assert self.soln.getFirstDuplicate(input) == -1
