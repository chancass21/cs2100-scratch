'''
    Class to represent a podcast, this time inherited from SpotifyContent


'''

from spotify_content import SpotifyContent

class Podcast(SpotifyContent):
    ''' Class for a podcast, which has a title, host, episodes, and total duration '''

    def __init__(self, title: str, host: str):
        ''' Initialize a podcast with title and host
        
        Parameters:
            title: The podcast title
            host: The podcast host names
        '''
        super().__init__(title, host)
        self._episodes: list[str] = []

    @property
    def host(self) -> str:
        ''' return the superclass's creator attribute '''
        return self.creator

    @host.setter
    def host(self, value: str) -> None:
        ''' update the host name, after validating, via the superclass '''
        self.creator = value

    def add_episode(self, ep_name: str, length: int) -> None:
        ''' add an episode by name and duration '''
        self._add_to_total_duration(length)
        self._episodes.append(ep_name)

    def __len__(self) -> int:
        ''' return the number of episodes '''
        return len(self._episodes)

    def __str__(self) -> str:
        ''' Return string representation of the podcast ''' 
        return str(f"{self._title} hosted by {self.host}, with "
                   f"{len(self)} total episodes")

    def __eq__(self, other: object) -> bool:
        ''' return True if self, other are same, other False 
            (this implements pd1 == pd2)
        '''
        if isinstance(other, Podcast):
            if self.title == other.title and self.host == other.host:
                return True
        return False
