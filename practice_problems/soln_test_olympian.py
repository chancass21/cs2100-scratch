'''
    test the olympian class
'''

import unittest
from olympian import Olympian

class TestPodcast(unittest.TestCase):
    ''' test the podcast class and all the visibility access '''
    def setUp(self) -> None:
        ''' set up two podcasts for testing, and make sure the title/host can't be empty '''
        self.o1 = Olympian("USA", "luge")
        self.o2 = Olympian("Mexico", "skeleton")

    def test_bad_init(self) -> None:
        ''' test that we raise errors in the constructor appropriately '''
        with self.assertRaises(ValueError):
            Olympian("", "a") 
        with self.assertRaises(ValueError):
            Olympian("a", "")
        with self.assertRaises(ValueError):
            Olympian("", "")
        with self.assertRaises(ValueError):
            Olympian("fake country", "hockey")
        with self.assertRaises(ValueError):
            Olympian("Norway", "fake sport")

    def test_country(self) -> None:
        ''' test the country names are correct and changeable, accessed via the property '''
        self.assertEqual(self.o1.country, "USA")
        self.assertEqual(self.o2.country, "Mexico")

        self.o1.country = "Korea"
        self.o2.country = "Norway"
        self.assertEqual(self.o1.country, "Korea")
        self.assertEqual(self.o2.country, "Norway")

    def test_invalid_country(self) -> None:
        ''' test I can't change the country name to empty string, or invalid country '''
        with self.assertRaises(ValueError):
            self.o1.country = ""
            self.o1.country = "not a country"

    def test_sport(self) -> None:
        ''' test the sport is correct and changeable, accessed via the property '''
        self.assertEqual(self.o1.sport, "luge")
        self.assertEqual(self.o2.sport, "skeleton")

        self.o1.sport = "hockey"
        self.o2.sport = "ice skating"
        self.assertEqual(self.o1.sport, "hockey")
        self.assertEqual(self.o2.sport, "ice skating")

    def test_invalid_sport(self) -> None:
        ''' test I can't change the sports to empty string or an invalid sport '''
        with self.assertRaises(ValueError):
            self.o1.sport = ""
        with self.assertRaises(ValueError):
            self.o1.sport = "summer sport"

    def test_medal_count(self) -> None:
        ''' test medal count before and after adding some episodes '''
        self.assertEqual(len(self.o1), 0)
        self.o1.add_medal("gold")
        self.assertEqual(len(self.o1), 1)

    def test_add_medal_invalid(self) -> None:
        ''' make sure we can't add a medal that isn't g/s/b '''
        with self.assertRaises(ValueError):
            self.o2.add_medal("b")

if __name__ == "__main__":
    unittest.main()
