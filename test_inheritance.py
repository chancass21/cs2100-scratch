'''
    Test Podcast and SpotifyContent classes
'''


import unittest
from spotify_content_end import SpotifyContent
from podcast_end import Podcast

class TestSpotify(unittest.TestCase):
    ''' test the supeclass SpotfiyContent '''
    def setUp(self) -> None:
        ''' set up two generic spotify-contents for testing, 
            and make sure the title/host can't be empty
        '''
        self.sp1 = SpotifyContent("title", "creator")
        self.sp2 = SpotifyContent(title = "t2", creator = "c2")

    def test_bad_init(self) -> None:
        ''' test that we raise an error for a bad call to constructor '''
        with self.assertRaises(ValueError):
            SpotifyContent("", "a")

        with self.assertRaises(ValueError):
            SpotifyContent("a", "")

        with self.assertRaises(ValueError):
            SpotifyContent("", "")

    def test_creator_names(self) -> None:
        ''' test the creator names are correct and changeable, accessed via the property '''
        self.assertEqual(self.sp1.creator, "creator")
        self.assertEqual(self.sp2.creator, "c2")

        self.sp1.creator = "new creator"
        self.sp2.creator = "b"
        self.assertEqual(self.sp1.creator, "new creator")
        self.assertEqual(self.sp2.creator, "b")

    def test_empty_creator_name(self) -> None:
        ''' test I can't change the creator name to empty string '''
        with self.assertRaises(ValueError):
            self.sp1.creator = ""

    def test_titles(self) -> None:
        ''' test the titles are correct and changeable, accessed via the property '''
        self.assertEqual(self.sp1.title, "title")
        self.assertEqual(self.sp2.title, "t2")

        self.sp1.title = "title one"
        self.sp2.title = "title two"
        self.assertEqual(self.sp1.title, "title one")
        self.assertEqual(self.sp2.title, "title two")

    def test_empty_title(self) -> None:
        ''' test I can't change the title to empty string '''
        with self.assertRaises(ValueError):
            self.sp1.title = ""

class TestPodcast(unittest.TestCase):
    ''' test the subclass podcast and all the inheritance components '''
    def setUp(self) -> None:
        ''' set up two podcasts for testing, and make sure the title/host can't be empty '''
        self.p1 = Podcast(host = "host1", title = "title1")
        self.p2 = Podcast(title = "t2", host = "h2")

    def test_bad_init(self) -> None:
        ''' test that we raise an error for a bad call to constructor '''
        with self.assertRaises(ValueError):
            Podcast("", "a")

        with self.assertRaises(ValueError):
            Podcast("a", "")

        with self.assertRaises(ValueError):
            Podcast("", "")

    def test_host_names(self) -> None:
        ''' test the host names are correct and changeable, accessed via the property '''
        self.assertEqual(self.p1.host, "host1")
        self.assertEqual(self.p2.host, "h2")

        self.p1.host = "host one"
        self.p2.host = "host two"
        self.assertEqual(self.p1.host, "host one")
        self.assertEqual(self.p2.host, "host two")

    def test_empty_host_name(self) -> None:
        ''' test I can't change the host name to empty string '''
        with self.assertRaises(ValueError):
            self.p1.host = ""

    def test_titles(self) -> None:
        ''' test the titles are correct and changeable, accessed via the property '''
        self.assertEqual(self.p1.title, "title1")
        self.assertEqual(self.p2.title, "t2")

        self.p1.title = "title one"
        self.p2.title = "title two"
        self.assertEqual(self.p1.title, "title one")
        self.assertEqual(self.p2.title, "title two")

    def test_empty_title(self) -> None:
        ''' test I can't change the title to empty string '''
        with self.assertRaises(ValueError):
            self.p1.title = ""

    def test_ep_count(self) -> None:
        ''' test episode count before and after adding some episodes '''
        self.p1.add_episode("a", 10)
        self.assertEqual(len(self.p1), 1)

        with self.assertRaises(ValueError):
            self.p2.add_episode("b", -1)

    def test_equality(self) -> None:
        ''' test when two Podcasts's are equal, or not '''
        new_pd = Podcast("title1", "host1")
        self.assertTrue(self.p1 == new_pd)
        self.assertFalse(self.p1 == self.p2)


if __name__ == "__main__":
    unittest.main()
