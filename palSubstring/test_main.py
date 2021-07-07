# Run: pytest test_main.py

from main import Solution
import pytest

class TestLongestPalindrome:
    def setup(self):
        self.soln = Solution()
    
    def test_longest(self):
        input = "abcdefghaa"
        table = self.soln.buildHashTable(input)
        head = self.soln.buildSortedListNodes(table)
        assert self.soln.getLongestPalindrome(head, input) == "aa"

    def test_longest2(self):
        input = "a"
        table = self.soln.buildHashTable(input)
        head = self.soln.buildSortedListNodes(table)
        assert self.soln.getLongestPalindrome(head, input) == "a"

    def test_longest3(self):
        input = "abcdefgfedcbazzzzzzzzzzzzzzzzzzzz"
        table = self.soln.buildHashTable(input)
        head = self.soln.buildSortedListNodes(table)
        assert self.soln.getLongestPalindrome(head, input) == "zzzzzzzzzzzzzzzzzzzz"

    def test_longest4(self):
        input = "zzzzzzz2345abbbba5432zzbbababa"
        table = self.soln.buildHashTable(input)
        head = self.soln.buildSortedListNodes(table)
        assert self.soln.getLongestPalindrome(head, input) == "zz2345abbbba5432zz"
