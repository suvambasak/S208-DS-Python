import math
import sys
import unittest

from factorial import fact

sys.setrecursionlimit(1000000)


class TestFactorial(unittest.TestCase):

    def test_edge_case(self) -> None:
        'Testing edge cases'
        self.assertEqual(1, fact(1))
        self.assertEqual(1, fact(0))

    def test_invalid_inputs(self) -> None:
        'Testing with invalid inputs (-ve numbers)'
        try:
            self.assertEqual(None, fact(-10))
            self.assertEqual(None, fact(-33))
        except RecursionError as err:
            raise RuntimeError('Failed for -ve input')

    def test_results(self) -> None:
        'Testing for correct results'
        for i in range(1000):
            self.assertEqual(math.factorial(i), fact(i))
