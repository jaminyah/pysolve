import pytest
from solution import Solution

class TestReverseString:
    def setup(self):
        self.soln = Solution()

    def test_reverse(self):
        a = "touch screen tablet   3"
        assert self.soln.reverse(a) == "3   tablet screen touch"
    
    def test_reverse2(self):
        a = "hello, world!"
        assert self.soln.reverse(a) == "world! hello,"
