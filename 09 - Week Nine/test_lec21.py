'''
    Test our static and class methods for Donut and PremiumDonut classes
'''

import unittest
from lec21_class_methods import Donut, PremiumDonut, DonutException

class TestDonuts(unittest.TestCase):
    ''' test the Donut class with new static and class methods '''
    def setUp(self) -> None:
        ''' set up a donut from the regular init '''
        self.d1 = Donut("jelly", 1.19)
        self.pd1 = PremiumDonut("matcha", 4.19)

    def test_invalid_init(self) -> None:
        ''' these examples should fail because the flavors don't exist, or price is too low '''
        with self.assertRaises(DonutException):
            Donut("noflavor", 1.10)
        with self.assertRaises(DonutException):
            Donut("", 1.10)
        with self.assertRaises(DonutException):
            Donut("jelly", .50)
        with self.assertRaises(DonutException):
            Donut("noflavor", 0.1)

    def test_change_flavor_price_valid(self) -> None:
        ''' test that we can see and modify price and flavor, as long as the 
            new values are valid 
        '''
        self.assertEqual("jelly", self.d1.flavor)
        self.d1.flavor = "boston cream"
        self.assertEqual("boston cream", self.d1.flavor)

        self.assertEqual(1.19, self.d1.price)
        self.d1.price = 1.50
        self.assertEqual(1.5, self.d1.price)

    def test_change_flavor_price_invalid(self) -> None:
        ''' test that if we try to make price/flavor invalid values, exceptions are raised'''
        with self.assertRaises(DonutException):
            self.d1.flavor = "no flavor"
        with self.assertRaises(DonutException):
            self.d1.price = -1.0
        with self.assertRaises(DonutException):
            self.d1.price = 0.50

    def test_class_method(self) -> None:
        ''' test that we can create donuts via our class method (valid cases) '''
        d2 = Donut.from_menu(0, 1.99)
        self.assertEqual("glazed", d2.flavor)
        self.assertEqual(1.99, d2.price)

    def test_class_method_invalid(self) -> None:
        ''' test that attempts to make invalid donuts from class method fail '''
        with self.assertRaises(DonutException):
            Donut.from_menu(5, 1.99)
        with self.assertRaises(DonutException):
            Donut.from_menu(-5, 1.99)
        with self.assertRaises(DonutException):
            Donut.from_menu(0, .99)

    def test_static_method(self) -> None:
        ''' test that I can call my static method to validate a coupon '''
        valid = "DONUT20"
        self.assertTrue(Donut.is_valid_code(valid))

        invalid = "DNT345"
        self.assertFalse(Donut.is_valid_code(invalid))
        invalid = "DONUTTHREE"
        self.assertFalse(Donut.is_valid_code(invalid))

    def test_eq(self) -> None:
        ''' test that the eq method works as expected '''
        d2 = Donut("jelly", 1.19)
        self.assertEqual(self.d1, d2)

        d3 = PremiumDonut("matcha", 4.19)
        self.assertEqual(self.pd1, d3)

        self.assertNotEqual(d2, self.pd1)

if __name__ == "__main__":
    unittest.main()
