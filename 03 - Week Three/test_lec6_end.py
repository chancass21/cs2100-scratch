'''
    CS2100
    Spring 2026
    Sample code from class -- testing data structure conversions, and file I/O

'''

import unittest
import os
from lec6_start import read_file_to_list, list_to_tuples, list_to_sets

class TestDataStructures(unittest.TestCase):
    ''' testing the 2d list to tuple/set conversions '''
    def test_list_to_tuples_basic(self) -> None:
        ''' test conversion from 2d list to list of tuples, easy cases '''
        start_list = [["a"], ["b"], ["c"]]
        expected = [tuple("a"), tuple("b"), tuple("c")]
        actual = list_to_tuples(start_list)
        self.assertEqual(expected, actual)

        start_list1 = [["a", "b", "c"]]
        expected = [("a", "b", "c")]
        actual = list_to_tuples(start_list1)
        self.assertEqual(expected, actual)

        start_list2 = [["a", "b", "c"], ["d", "e", "f"]]
        expected = [("a", "b", "c"), ("d", "e", "f")]
        actual = list_to_tuples(start_list2)
        self.assertEqual(expected, actual)

    def test_list_to_tuples_empty(self) -> None:
        ''' test list_to_tuples conversion if the 2d list is empty or None '''
        self.assertIsNone(list_to_tuples([[]]))
        self.assertIsNone(list_to_tuples(None))

    def test_list_to_sets_basic(self) -> None:
        ''' test conversion from 2d list to dictionary of str: set, easy cases '''
        start_list = [["a"], ["b"], ["c"]]
        expected = {"a" : set(), "b" : set(), "c" : set()}
        actual = list_to_sets(start_list)
        self.assertEqual(expected, actual)

        start_list1 = [["a", "b", "c"]]
        expected = {"a" : {"b", "c"}}
        actual = list_to_sets(start_list1)
        self.assertEqual(expected, actual)

        start_list2 = [["a", "b", "c"], ["d", "e", "f"]]
        expected = {"a" : {"b", "c"}, "d": {"e", "f"}}
        actual = list_to_sets(start_list2)
        self.assertEqual(expected, actual)

    def test_list_to_sets_empty(self) -> None:
        ''' test list_to_sets conversion if the 2d list is empty or None '''
        self.assertIsNone(list_to_sets([[]]))
        self.assertIsNone(list_to_sets(None))


class TestFileIO(unittest.TestCase):
    ''' class to test file reading function '''
    def setUp(self) -> None:
        ''' create test files before testing the file functions '''
        with open("dummy_file_simple.txt", "w", encoding = "utf=8") as f:
            f.write("Date,Jan1\n")

        with open("dummy_file_medium.txt", "w", encoding = "utf-8") as f:
            f.write("Date,Jan1,Jan2\n")
            f.write("Miles,1,3\n")
            f.write("Pace,6.2,4.4\n")

        with open("dummy_file_training.txt", "w", encoding = "utf-8") as f:
            f.write("training groups,a,b,c\n")
            f.write("more groups,b,c\n")

        with open("dummy_file_empty.txt", "w", encoding = "utf-8") as f:
            pass

    def test_read_file_to_list(self) -> None:
        ''' test our function that reads from file to a 2d list '''
        file = "dummy_file_simple.txt"
        expected = [["Date", "Jan1"]]
        actual = read_file_to_list(file)
        self.assertEqual(expected, actual)

        file = "dummy_file_medium.txt"
        expected = [["Date", "Jan1", "Jan2"],
                    ["Miles", "1", "3"],
                    ["Pace", "6.2", "4.4"]]
        actual = read_file_to_list(file)
        self.assertEqual(expected, actual)

        file = "dummy_file_empty.txt"
        actual = read_file_to_list(file)
        self.assertIsNone(actual)


    def tearDown(self):
        ''' clean up test files '''
        test_files = ["dummy_file_simple.txt", "dummy_file_medium.txt",
                      "dummy_file_training.txt", "dummy_file_empty.txt"]

        for file in test_files:
            if os.path.exists(file):
                os.remove(file)



if __name__ == "__main__":
    unittest.main()
