'''
    Class to represent SpotifyContent

    Podcast, Album, and Audio Book could all inherit from this class

    SpotifyContent includes:
    * title (w/property and setter)
    * creator (w/property and setter)   
    * __str__

    We'll add:
    * _add_to_total_duration
    * _validate_duration
    * __eq__ 
'''

class SpotifyContent:
    ''' Super class for Spotify content (podcasts, albums, audio books, etc.) '''

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
            raise ValueError("Title must be a non-empty string")
        self._title = value

    @property
    def creator(self) -> str:
        ''' return the creator name '''
        return self._creator

    @creator.setter
    def creator(self, new_name: str) -> None:
        ''' validate and set the creator name '''
        if not new_name:
            raise ValueError("Creator must be a non-empty string")
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
            raise ValueError("Episode duration must be a positive number")

    def __str__(self) -> str:
        ''' return a nicely formatted version of the ojbect as a string '''
        return str(f"{self._title} from creator {self._creator} with total duration"
                   f" {self.__total_duration} minutes")
