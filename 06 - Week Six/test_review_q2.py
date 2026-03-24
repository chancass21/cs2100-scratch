'''
    CS2100
    Spring 2026

    Tests for practice problems on 2/11/26

    Once you've written in the function stubs you want,
    test 'em to make sure they work as expected. 

    You can run the entire test file the way you normally do, or...

    You can test one thing at a time by running this in your terminal:
    python -m unittest test_review_q2.TestPracticeProblem[Name]

    e.g.,:
    python3 -m unittest test_review_q2.TestPracticeProblemNormalize
    python3 -m unittest test_review_q2.TestPracticeProblemEmail
    
'''

import unittest
from review_q2 import (create_email,
                       normalize_lst,
                       dedupe,
                       find_common,
                       swap_pairs,
                       has_required,
                       get_seconds,
                       Book)

class TestPracticeProblemEmail(unittest.TestCase):
    ''' tests for the practice problems in prep for quiz 2 '''
    def test_create_email(self) -> None:
        ''' test main cases and edge cases of the create email function '''
        with self.assertRaises(ValueError):
            create_email("")

        expected_def_from = str("From: noreply@northeastern.edu\n"
                                "To: student@northeastern.edu\n"
                                "Subject: hi")
        self.assertEqual(create_email("student@northeastern.edu", subject = "hi"),
                                      expected_def_from)
        expected_def_subj = str("From: hello@northeastern.edu\n"
                                "To: student@northeastern.edu\n"
                                "Subject: No Subject")
        self.assertEqual(create_email("student@northeastern.edu",
                                      sender = "hello@northeastern.edu"),
                                      expected_def_subj)

class TestPracticeProblemNormalize(unittest.TestCase):
    ''' tests for the practice problems in prep for quiz 2 '''
    def test_normalize(self) -> None:
        ''' test main cases and edge cases of the normalize function '''
        with self.assertRaises(ValueError):
            normalize_lst([])
            normalize_lst([1])
            normalize_lst([3, 3, 3, 3])

        expected = [0, .5, 1]
        self.assertEqual(normalize_lst([0, 5, 10]), expected)

        expected = [1, 0, .5]
        self.assertEqual(normalize_lst([10, 0, 5]), expected)

class TestPracticeProblemDedupe(unittest.TestCase):
    ''' tests for the practice problems in prep for quiz 2 '''
    def test_dedupe(self) -> None:
        ''' test main cases and edge case of the dedupe function '''
        with self.assertRaises(ValueError):
            dedupe([])

        self.assertEqual(dedupe([1, 1, 1, 1, 1]), [1])
        self.assertEqual(set(dedupe([1, 2, 3, 4, 5])), set([1, 2, 3, 4, 5]))
        self.assertEqual(set(dedupe(['b', 'c', 'a', 'a', 'b'])), set(['b', 'c', 'a']))

class TestPracticeProblemCommon(unittest.TestCase):
    ''' tests for the practice problems in prep for quiz 2 '''
    def test_find_common(self) -> None:
        ''' test main cases and edge cases of find_common function '''
        with self.assertRaises(ValueError):
            find_common([], [1, 2, 3])
            find_common([], [])
            find_common(['a', 'b'], [])

        self.assertEqual(find_common([1], [2]), set())
        self.assertEqual(find_common(['a', 'b'], ['b', 'a']), {'a', 'b'})
        self.assertEqual(find_common(['a', 'b', 'c'], ['a']), {'a'})

class TestPracticeProblemSwaps(unittest.TestCase):
    ''' tests for the practice problems in prep for quiz 2 '''
    def test_swaps(self) -> None:
        ''' test main cases and edge cases of swap_values function '''
        with self.assertRaises(ValueError):
            swap_pairs([])

        self.assertEqual(swap_pairs([(1, 2)]), [(2, 1)])
        self.assertEqual(swap_pairs([(1, 2), (3, 4)]), [(2, 1), (4, 3)])

class TestPracticeProblemRequired(unittest.TestCase):
    ''' tests for the practice problems in prep for quiz 2 '''
    def test_has_required(self) -> None:
        ''' test main cases and edge cases of has_required function '''
        with self.assertRaises(ValueError):
            has_required(set(), set())
            has_required(set(), {1})
            has_required({1}, set())

        self.assertTrue(has_required({1, 2, 3}, {3, 2}))
        self.assertTrue(has_required({'a', 'b'}, {'b', 'a'}))
        self.assertFalse(has_required({'a', 'b'}, {'b', 'd'}))
        self.assertFalse(has_required({'a', 'b'}, {'d'}))

class TestPracticeProblemConnections(unittest.TestCase):
    ''' tests for the practice problems in prep for quiz 2 '''
    def test_connections(self) -> None:
        ''' test main cases and edge cases of get_seconds function '''
        with self.assertRaises(ValueError):
            get_seconds('', {'a' : ['b', 'c']})
            get_seconds('a', {})

        self.assertEqual(get_seconds('a', {'b' : ['c']}), {'c'})
        self.assertEqual(get_seconds('a', {'b' : ['c'],
                                           'c' : ['d']}), {'d'})
        self.assertEqual(get_seconds('a', {'b' : ['c', 'd', 'e'],
                                           'c' : ['d']}), {'d', 'e'})
        self.assertEqual(get_seconds('a', {'b' : ['c', 'd', 'e'],
                                           'c' : ['d', 'a'],
                                           'f' : ['g', 'b']}), {'d', 'e', 'g'})
class TestPracticeProblemBook(unittest.TestCase):
    ''' tests for the practice problems in prep for quiz 2 '''
    def test_book(self) -> None:
        ''' create a book object and test it '''
        b = Book()
        self.assertEqual(str(b), "Read so far: 0 pages")
        b.increase_pages(5)
        self.assertEqual(str(b), "Read so far: 5 pages")
        b.increase_pages(-1)
        self.assertEqual(str(b), "Read so far: 5 pages")

if __name__ == "__main__":
    unittest.main()
