'''
    CS2100
    Spring 2026
    Sample code from class - unittest for our runner-mileage functions

    To end on 1/12, and to start class on 1/14, we have:
    * testing generate stats function with basic info (miles are 1, 2, 3 or 1, 1, 1)
    * testing generate stats function with zeroes for mileage (miles are 0, 0, 0, or just 0)
    
    We need to add on:
    * testing generate stats function on an empty input or None (should return None)
    * testing generate stats function on negative mileage (should raise an error)

    We also want to try testing another function in the starter file,
    which prints a summary. The function prints, and doesn't return anything,
    but we still need to test it :)
'''

import unittest
from lec4_start import generate_mileage_stats

class TestRunners(unittest.TestCase):
    ''' test the functions defined in lec3_start '''
    def test_generate_stats_basic(self) -> None:
        ''' test your everyday basic mileage '''
        test_dct = {"a" : 1.0, "b" : 2.0, "c" : 3.0}
        expected = {"total miles" : 6, "avg daily" : 2}
        
        actual = generate_mileage_stats(test_dct)
        self.assertEqual(expected, actual)

        test_dct["b"] = 1.0
        test_dct["c"] = 1.0
        expected["total miles"] = 3
        expected["avg daily"] = 1
        self.assertEqual(expected, generate_mileage_stats(test_dct))

    def test_generate_stats_zeroes(self) -> None:
        ''' given a dictionary with zeroes for mileage, we should return 0 for stats '''
        expected = {"total miles" : 0, "avg daily" : 0}
        self.assertEqual(expected, generate_mileage_stats({"1" : 0.0}))
        self.assertEqual(expected, generate_mileage_stats({"a" : 0.0, "b" : 0.0}))
    
    def test_generate_stats_empty(self) -> None:
        ''' given an empty dictionary for mileage or None, we should return None '''
        pass
                         
    def test_generate_stats_negative(self) -> None:
        ''' given a dictionary with negative miles, we should raise an error '''
        pass
    



if __name__ == "__main__":
    unittest.main()
