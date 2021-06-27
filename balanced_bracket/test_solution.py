# Run: python test_solution.py

import unittest
from solution import Solution

class BalancedBracketTest(unittest.TestCase):
    def setUp(self):
        self.soln = Solution()

    def test_balanced_1(self):
        input = '{'
        self.assertEqual(self.soln.balancedBrackets(input), False)

    def test_balanced_2(self):
        input = '([])(){}(())()()'
        self.assertEqual(self.soln.balancedBrackets(input), True)

    def test_balanced_3(self):
        input = '()[]{}{'
        self.assertEqual(self.soln.balancedBrackets(input), False)

    def test_balanced_4(self):
        input = ')[]}'
        self.assertEqual(self.soln.balancedBrackets(input), False)

if __name__ == '__main__':
    unittest.main()