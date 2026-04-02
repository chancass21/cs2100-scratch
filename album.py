'''
    Practice problems for inheritance!

    In class, we created a SpotifyContent class, which could be anything on spotify -- a podcast,
    an album, an audio book, etc. Then we wrote one subclass, Podcast.

    This is another subclass, Album.
'''

from spotify_content import SpotifyContent

# only some genres are available on spotify
VALID_GENRES = ["hip hop", "soul", "rock", "punk", "pop punk", "disco",
                "broadway", "power ballad", "pop", "video game music",
                "thrash metal", "rock/pop", "triphop", "funk fusion",
                "gaming, breakcore, industrial metal", "alternative rock",
                "alternative", "indie folk", "hip-hop/rap", "gaming, electronic, 8-bit",
                "comedy", "gaming", "folk", "jazz", "hip-hop", "rap", "alternative pop"]

class Album(SpotifyContent):
    ''' Class for an album, which has songs and genre but inherits from SpotifyContent'''

    def __init__(self, title: str, artist: str, genre: str):
        ''' Initialize an album with title, artist, and genre '''
        super().__init__(title, artist)
        self._songs: list[str] = []
        self.genre = genre

    @property
    def genre(self) -> str:
        ''' return the genre of the album '''
        return self._genre

    @genre.setter
    def genre(self, g: str) -> None:
        ''' set the genre, after validation '''
        if g.lower() not in [genre.lower() for genre in VALID_GENRES]:
            raise ValueError(f"Genre {g} not valid :(")
        self._genre = g

    @property
    def artist(self) -> str:
        ''' return the artist name (alias for creator) '''
        return self._creator

    @artist.setter
    def artist(self, new_name: str) -> None:
        ''' set the artist name '''
        self.creator = new_name

    def __len__(self) -> int:
        ''' return the number of songs '''
        return len(self._songs)

    def add_song(self, song_name: str, duration: int) -> None:
        ''' Add a song to the album '''
        self._add_to_total_duration(duration)
        self._songs.append(song_name)

    def __str__(self) -> str:
        return (f"{self._title} by {self.artist} ({self._genre}), with "
                f"{len(self)} total songs")

    def __eq__(self, other: object) -> bool:
        ''' return True if self, other are same, other False 
            (this implements a1 == a2)
        '''
        if isinstance(other, Album):
            if self.title == other.title and self.creator == other.creator:
                return True
        return False
