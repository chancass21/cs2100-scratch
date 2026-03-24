'''
    Test code for recursion practice problems
'''

import unittest

from practice_recursion_practice import factorial, fib, palindrome, rec_sum, rec_max

class RecursionTest(unittest.TestCase):
    ''' test recursive functions for practice '''
    def test_factorial(self) -> None:
        ''' test the recursive factorial function '''
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(5), 120)

    def test_fib(self) -> None:
        ''' test the recursive fibonacci function '''
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(6), 8)

    def test_pal(self) -> None:
        ''' test the recursive palindrome function '''
        self.assertTrue(palindrome("radar"))
        self.assertTrue(palindrome("a"))
        self.assertTrue(palindrome("racecar"))
        self.assertTrue(palindrome("abba"))
        self.assertFalse(palindrome("abb"))
        self.assertFalse(palindrome("laney"))
        self.assertFalse(palindrome("abca"))

    def test_sum(self) -> None:
        ''' test the recursive sum function '''
        self.assertEqual(rec_sum([]), 0)
        self.assertEqual(rec_sum([1]), 1)
        self.assertEqual(rec_sum([1, 2, 3]), 6)
        self.assertEqual(rec_sum([1, 2, 3, 1]), 7)
        self.assertEqual(rec_sum([1, 2, 3, -1]), 5)

    def test_max(self) -> None:
        ''' test the recursive max function '''
        self.assertEqual(rec_max([1]), 1)
        self.assertEqual(rec_max([1, 2, 3]), 3)
        self.assertEqual(rec_max([1, 2, 3, 1]), 3)
        self.assertEqual(rec_max([5, -1, 0, 5, 2]), 5)

if __name__ == "__main__":
    unittest.main()
