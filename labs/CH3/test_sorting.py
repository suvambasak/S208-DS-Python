import sys
import unittest
import random

from sorting import insertion_sort, selection_sort, merge_sort, quick_sort

sys.setrecursionlimit(1000000)


class TestSearching(unittest.TestCase):

    data_list_1 = [1]
    data_list_2 = [1, 2]
    data_list_3 = [1, 2, 3]

    def edge_case_internal(self, fun) -> None:

        data_list = self.data_list_1[:]
        data_list.reverse()
        fun(data_list)
        self.assertEqual(data_list, self.data_list_1)

        data_list = self.data_list_2[:]
        data_list.reverse()
        fun(data_list)
        self.assertEqual(data_list, self.data_list_2)

        data_list = self.data_list_3[:]
        data_list.reverse()
        fun(data_list)
        self.assertEqual(data_list, self.data_list_3)

    def test_edge_case_insertion_sort(self) -> None:
        self.edge_case_internal(insertion_sort)

    def test_edge_case_selection_sort(self) -> None:
        self.edge_case_internal(selection_sort)

    def test_edge_case_merge_sort(self) -> None:
        data_list = self.data_list_1[:]
        data_list.reverse()
        data_list = merge_sort(data_list, 0, len(data_list))
        self.assertEqual(data_list, self.data_list_1)

        data_list = self.data_list_2[:]
        data_list.reverse()
        data_list = merge_sort(data_list, 0, len(data_list))
        self.assertEqual(data_list, self.data_list_2)

        data_list = self.data_list_3[:]
        data_list.reverse()
        data_list = merge_sort(data_list, 0, len(data_list))
        self.assertEqual(data_list, self.data_list_3)

    def test_edge_case_quick_sort(self) -> None:
        data_list = self.data_list_1[:]
        data_list.reverse()
        quick_sort(data_list, 0, len(data_list))
        self.assertEqual(data_list, self.data_list_1)

        data_list = self.data_list_2[:]
        data_list.reverse()
        quick_sort(data_list, 0, len(data_list))
        self.assertEqual(data_list, self.data_list_2)

        data_list = self.data_list_3[:]
        data_list.reverse()
        quick_sort(data_list, 0, len(data_list))
        self.assertEqual(data_list, self.data_list_3)

    def results_internal(self, fun) -> None:
        for _ in range(10):
            random_list = [random.randint(0, 10000)
                           for _ in range(random.randint(0, 10000))]

            sorted_random_list = random_list[:]
            sorted_random_list.sort()

            fun(random_list)
            self.assertEqual(random_list, sorted_random_list)

    def test_insertion_sort(self) -> None:
        self.results_internal(insertion_sort)

    def test_selection_sort(self) -> None:
        self.results_internal(selection_sort)

    def test_merge_sort(self) -> None:
        for _ in range(10):
            random_list = [random.randint(0, 10000)
                           for _ in range(random.randint(0, 10000))]

            sorted_random_list = random_list[:]
            sorted_random_list.sort()

            random_list = merge_sort(random_list, 0, len(random_list))
            self.assertEqual(random_list, sorted_random_list)

    def test_quick_sort(self) -> None:
        for _ in range(10):
            random_list = [random.randint(0, 10000)
                           for _ in range(random.randint(0, 10000))]

            sorted_random_list = random_list[:]
            sorted_random_list.sort()

            quick_sort(random_list, 0, len(random_list))
            self.assertEqual(random_list, sorted_random_list)
