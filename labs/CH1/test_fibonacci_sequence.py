import sys
import unittest
import random
from fibonacci_sequence import fibonacci

sys.setrecursionlimit(1000000)


class TestFibonacci(unittest.TestCase):

    def test_edge_case(self) -> None:
        'Testing edge cases'
        self.assertEqual(1, fibonacci(1))
        self.assertEqual(0, fibonacci(0))

    def test_invalid_inputs(self) -> None:
        'Testing with invalid inputs (-ve numbers)'
        try:
            self.assertEqual(None, fibonacci(-10))
            self.assertEqual(None, fibonacci(-33))
        except RecursionError as err:
            raise RuntimeError('Failed for -ve input')

    def fibonacci(self, n: int) -> int:
        num_1 = 0
        num_2 = 1
        if n == 0:
            return num_1
        elif n == 1:
            return num_2
        for _ in range(2, n+1):
            num_3 = num_1+num_2
            num_1, num_2 = num_2, num_3
        return num_2

    def test_results(self) -> None:
        'Testing for correct results'
        for _ in range(33):
            random_number = random.randint(0, 40)
            self.assertEqual(
                self.fibonacci(random_number),
                fibonacci(random_number)
            )
