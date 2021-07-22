"""
    Run: pytest test_solution.py
"""

import pytest
from solution import Solution

class TestAllDuplicates:

    def setup(self):
        self.soln = Solution()

    def test_all_duplicates(self):
        input = [1, 2, 4, 6, 2, 4, 7]
        assert self.soln.findAllDuplicates(input) == [2, 4]

    def test_all_duplicates2(self):
        input = [11, 22, 14, 26, 12, 4, 7]
        assert self.soln.findAllDuplicates(input) == [-1]   
