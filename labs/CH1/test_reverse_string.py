
import sys
import unittest
import random
import string
from reverse_string import reverse_string_recursive

sys.setrecursionlimit(1000000)


class TestReverseString(unittest.TestCase):

    def test_edge_case(self) -> None:
        self.assertEqual('', reverse_string_recursive(''))
        self.assertEqual('1', reverse_string_recursive('1'))

    def test_palindrome_inputs(self) -> None:
        self.assertEqual('DAD', reverse_string_recursive('DAD'))
        self.assertEqual('MOM', reverse_string_recursive('MOM'))
        self.assertEqual('madam', reverse_string_recursive('madam'))

    def generate_random_text(self, length: int) -> str:
        return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation + ' ', k=length))

    def reversed_text(self, text: str) -> str:
        return ''.join(reversed(text))

    def test_results(self) -> None:
        for _ in range(50):
            random_text = self.generate_random_text(random.randint(5, 500))
            self.assertEqual(
                reverse_string_recursive(random_text),
                self.reversed_text(random_text)
            )
