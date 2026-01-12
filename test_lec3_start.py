'''
    CS2100
    Spring 2026
    Sample code from class - unittest for our functions
'''

import unittest
from lec3_start import generate_mileage_stats
# import module and functions to test

class TestRunners(unittest.TestCase):
    ''' test the functions defined in lec3_v2_dictionaries '''
    def test_generate_milage_stats(self) -> None:
        test_lst = [1, 2, 3]
        expected = {"total miles" : 6, "avg miles" : 2}
        actual = generated_mielage_stats(test_lst)
        self.assertEqaul(expected, actual)
        
        # self.assertEqual(functioncall, expected output)
        # self.assertEqual(functioncall, expected output)
        # self.assertEqual(functioncall, expected output)


if __name__ == "__main__":
    unittest.main()
