import unittest
from testing_python_lab1.services.SortService import get_bubble_sorted_list

class TestSortService(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sort_list_of_integers(self):

        """
            Summary: List sorting.
            Unit under test: SortService
            Preconditions: None
            Parameters to test: correct sorting of numbers (int) in ascending order.
            Test scenario:
                Pass a list of integers as an argument of the function under test;
                Compare output with a sample.
        """

        list_to_sort = [56, 34, -1, 9, 0, 18]

        sorted_list = get_bubble_sorted_list(list_to_sort)

        expected_list = [-1, 0, 9, 18, 34, 56]
        self.assertEqual(sorted_list, expected_list)

    def test_sort_empty_list(self):

        """
            Summary: List sorting.
            Unit under test: SortService
            Preconditions: None
            Parameters to test: correct sorting of integers in ascending order.
            Test scenario:
                Pass an empty list as an argument of the function under test;
                Compare output with a sample.
        """

        list_to_sort = []

        sorted_list = get_bubble_sorted_list(list_to_sort)

        expected_list = []
        self.assertEqual(sorted_list, expected_list)

    def test_sort_list_of_strings(self):

        """
            Summary: List sorting.
            Unit under test: SortService
            Preconditions: None
            Parameters to test: correct sorting of integers in ascending order.
           Test scenario:
                Pass an list of integers and strings as an argument of the function under test;
                Compare output with a sample.
        """

        list_to_sort = [67, "banana", "apple", -4, 0, "watermelon"]

        sorted_list = get_bubble_sorted_list(list_to_sort)

        expected_list = [-4, 0, 67]
        self.assertEqual(sorted_list, expected_list)

    def test_sort_list_of_different_datatypes(self):

        """
            Summary: List sorting.
            Unit under test: SortService
            Preconditions: None
            Parameters to test: correct sorting of integers in ascending order.
           Test scenario:
                Pass an list of Boolean, Strings, Floats and Integers as an argument of the function under test;
                Compare output with a sample.
        """

        list_to_sort = [True, -19.03, "18", 0, 57, None, 13]

        sorted_list = get_bubble_sorted_list(list_to_sort)

        expected_list = [0, 13, 57]
        self.assertEqual(sorted_list, expected_list)
