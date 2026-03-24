'''
    Class to represent SpotifyContent

    Podcast, Album, and AUdio Book could all inherit from this class

    In class on 2/26 -- making this class abstract!
    * we can no longer instantiate objects of this type
    * any methods we label as abstractmehod MUST be implemented by subclasses
    * otherwise, attributes and methods get inherited by subclasses just like normal
'''

from abc import ABC, abstractmethod

class SpotifyError(Exception):
    ''' create our own exception for spotify_content class '''
    def __init__(self, message: str = "spotify error occurred"):
        super().__init__(message)

class SpotifyContent(ABC):
    ''' Abstract class for Spotify content (podcasts, albums, audio books, etc.) '''

    def __init__(self, title: str, creator: str):
        ''' Initialize Spotify content with title and creator
        
        Parameters:
            title: The content title
            creator: The content creator (host, artist, etc.)
        '''
        self.title = title
        self.creator = creator
        self.__total_duration = 0

    @property
    def title(self) -> str:
        ''' return title of the content '''
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        ''' validate and set the title '''
        if not value:
            raise SpotifyError("Title must be a non-empty string")
        self._title = value

    @property
    def creator(self) -> str:
        ''' return the creator name '''
        return self._creator

    @creator.setter
    def creator(self, new_name: str) -> None:
        ''' validate and set the creator name '''
        if not new_name:
            raise SpotifyError("Creator must be a non-empty string")
        self._creator = new_name

    def _add_to_total_duration(self, duration: int) -> None:
        ''' update the total duration after validation '''
        self._validate_duration(duration)
        self.__total_duration += duration

    def _validate_duration(self, duration: int) -> None:
        ''' validate that duration is a postive number
            parameters: duration, an int, duration in minutes
            returns: none
            raises: value error if duration is not positive
        '''
        if duration <= 0:
            raise SpotifyError("Episode duration must be a positive number")

    def __repr__(self) -> str:
        ''' return a formatted string for the object (also makes it so we can print a list of these)'''
        return str(f"{self._title} by {self._creator}")

    @abstractmethod
    def __str__(self) -> str:
        ''' return a nicely formatted version of the object as a string
            all sublcasses must now implement their own __str__ '''

    @abstractmethod
    def __len__(self) -> int:
        ''' return the length of this object (all subclasses must implement) '''

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        ''' return a bool indicating if self, other are the same '''
