''' 
    CS2100
    Spring 2026
    Test code for the Runner class

    We have:
    - setUp() to create dummy files and a copule of Runner objects
    - tearDown() to remove the dummy files
    - test_runner_creation() to check the values of the attributes
        after calling the Runner constructor
    - test_runner_mileage()  to check the contents of the miles
        dictionary after reading in a file with mileage data
    - test_runner_stats() to check the contents of the stats
        dictionary after reading in a file and computing the stats
    - test_print_summary() to verify the output from the print method
'''

import unittest
import os
from unittest.mock import patch
from unittest.mock import MagicMock
from io import StringIO
from runner import Runner

class TestRunner(unittest.TestCase):
    ''' Test cases for the Runner class. '''
    def setUp(self) -> None:
        ''' create Runner objects and files for testing '''
        with open("dummy_file_simple.txt", "w", encoding = "utf=8") as f:
            f.write("Jan1\n")
            f.write("1\n")

        with open("dummy_file_empty.txt", "w", encoding = "utf-8") as f:
            pass

        self.r1 = Runner("one run", "dummy_file_simple.txt")
        self.r2 = Runner("empty runner", "dummy_file_empty.txt")

    def test_runner_creation(self) -> None:
        ''' Test basic runner object creation. '''
        pass


    def test_runner_mileage(self) -> None:
        ''' test the runner mileage after file read. '''
        pass

    def test_runner_stats(self) -> None:
        ''' Test the basic runner stats '''
        pass


    @patch("sys.stdout", new_callable = StringIO)
    def test_print_summary(self, mock_stdout: MagicMock) -> None:
        ''' test the print_summary function which prints but does not return '''
        self.r1.gather_mileage_input()
        self.r1.generate_mileage_stats()
        self.r1.print_summary()

        output = mock_stdout.getvalue()
        self.assertIn("Running stats for one run:\ntotal miles...1.0\n"
                      "avg daily...1.0", output)

    def tearDown(self) -> None:
        ''' clean up test files '''
        test_files = ["dummy_file_simple.txt", "dummy_file_empty.txt"]
        for file in test_files:
            if os.path.exists(file):
                os.remove(file)


if __name__ == "__main__":
    unittest.main()
