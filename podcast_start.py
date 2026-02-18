

'''
   Class to represent a podcast


   Starter code for lecture on 2/18/26


   The starter code:
   * has a constructor to instantiate a Podcast object
            (including three internal attributes (_) and one private attribute (__))
   * has @property to get the _title attribute from outside the class
   * has @title.setter to set the _title attribute from outside the class
   * has _validate_duration (a helper method, _ meaning for internal use)
   * has __str__ method to return a nicely formatted version of the podcast


   We'll add:
   * streamline the constructor to work with validation we're already doing
   * @property and @host.setter for the _host attribute
   * our own __len__  to return the number of episodes so far via len()
   * add_episode method so we can add episodes to the podcast
'''


class Podcast:
    ''' Class for a podcast, which has a title, host, episodes, and total duration '''

    def __init__(self, title: str, host: str):
        ''' Initialize a podcast with title and host
        
        Parameters:
            title: The podcast title
            host: The podcast host names
        '''
        if not title or not host:
            raise ValueError("title and host can't be empty string")
        self._title = title 
        self._host = host
        self._episodes: list[str] = []
        self.__total_duration = 0

    @property
    def title(self) -> str:
        ''' return title of the podcast, a string '''
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        ''' validate and set the title of the podcast 
        
            parameters: value (str), the new title

            returns: none

            raises: ValueError if string is empty
        '''
        if not value:
            raise ValueError("Title must be a non-empty string")
        self._title = value



    def _validate_duration(self, duration: int) -> None:
        ''' validate that duration is a postive number

            parameters: duration, an int, duration of a single episode in minutes

            returns: none

            raises: value error if single-ep duration is not positive
        '''
        if duration <= 0:
            raise ValueError("Episode duration must be a positive number")
   
    def __str__(self) -> str:
        ''' Return string representation of the podcast ''' 
        return str(f"{self._title} hosted by {self._host}, with "
                   f"{len(self)} total episodes, and "
                   f"total duration {self.__total_duration}")
