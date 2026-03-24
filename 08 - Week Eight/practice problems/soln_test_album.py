'''
    Test Album classes, inherits from SpotifyContent
'''


import unittest
from soln_album import Album

class TestAlbum(unittest.TestCase):
    ''' test the subclass podcast and all the inheritance components '''
    def setUp(self) -> None:
        ''' set up two podcasts for testing, and make sure the title/host can't be empty '''
        self.a1 = Album(title = "title1", artist = "artist1", genre = "punk")
        self.a2 = Album("t2", "a2", "power ballad")

    def test_bad_init(self) -> None:
        ''' test that we raise an error for a bad call to constructor '''
        with self.assertRaises(ValueError):
            Album("", "a", "b")

        with self.assertRaises(ValueError):
            Album("a", "", "")

        with self.assertRaises(ValueError):
            Album("", "", "")

    def test_artist_names(self) -> None:
        ''' test the artist names are correct and changeable, accessed via the property '''
        self.assertEqual(self.a1.artist, "artist1")
        self.assertEqual(self.a2.artist, "a2")

        self.a1.artist = "artist one"
        self.a2.artist = "artist two"
        self.assertEqual(self.a1.artist, "artist one")
        self.assertEqual(self.a2.artist, "artist two")

    def test_empty_artist_name(self) -> None:
        ''' test I can't change the artist name to empty string '''
        with self.assertRaises(ValueError):
            self.a1.artist = ""

    def test_titles(self) -> None:
        ''' test the titles are correct and changeable, accessed via the property '''
        self.assertEqual(self.a1.title, "title1")
        self.assertEqual(self.a2.title, "t2")

        self.a1.title = "title one"
        self.a2.title = "title two"
        self.assertEqual(self.a1.title, "title one")
        self.assertEqual(self.a2.title, "title two")

    def test_empty_title(self) -> None:
        ''' test I can't change the title to empty string '''
        with self.assertRaises(ValueError):
            self.a1.title = ""
    
    def test_genres(self) -> None:
        ''' test the genres are correct and changeable, accessed via the property '''
        self.assertEqual(self.a1.genre, "punk")
        self.assertEqual(self.a2.genre, "power ballad")

        self.a1.genre = "soul"
        self.a2.genre = "disco"
        self.assertEqual(self.a1.genre, "soul")
        self.assertEqual(self.a2.genre, "disco")

    def test_bad_genre(self) -> None:
        ''' test I can't change the genre to empty string or invalid genre '''
        with self.assertRaises(ValueError):
            self.a1.genre = ""
        
        with self.assertRaises(ValueError):
            self.a1.genre = "fake genre"

    def test_ep_count(self) -> None:
        ''' test episode count before and after adding a song '''
        self.a1.add_song("a", 10)
        self.assertEqual(len(self.a1), 1)

        with self.assertRaises(ValueError):
            self.a2.add_song("b", -1)

if __name__ == "__main__":
    unittest.main()
