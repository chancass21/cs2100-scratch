'''
    Class to represent a podcast

   Completed code from lecture on 2/18/26

   On Monday 2/23, we will
   * call the superclass's init from our init
   * remove attributes that are covered in superclass
   * move _validate_duration to superclass
   *  write our own version of __str__
'''


class Podcast:
    ''' Class for a podcast, which has a title, host, episodes, and total duration '''

    def __init__(self, title: str, host: str):
        ''' Initialize a podcast with title and host
        
        Parameters:
            title: The podcast title
            host: The podcast host names
        '''
        self.title = title # secret function call to the setter; updates self._title
        self.host = host # secret function call to the setter; updates self._host
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

    @property
    def host(self) -> str:
        ''' return the internal attirubte for host, a string '''
        return self._host

    @host.setter
    def host(self, new_name: str) -> None:
        ''' set the host name to new value
            parameters: new host name, a string
            returns: none
            raises: value error if new_name is empty string 
        '''
        if not new_name:
            raise ValueError("Host name cannot be empty")
        self._host = new_name

    def _validate_duration(self, duration: int) -> None:
        ''' validate that duration is a postive number
            parameters: duration, an int, duration of a single episode in minutes
            returns: none
            raises: value error if single-ep duration is not positive
        '''
        if duration <= 0:
            raise ValueError("Episode duration must be a positive number")

    def add_episode(self, ep_name: str, duration: int) -> None:
        ''' add episode to the podcast, validating duration first
            parameters: ep name, a string, and duration an int 
            returns: nothing
        '''
        self._validate_duration(duration)
        self.__total_duration += duration
        self._episodes.append(ep_name)

    def __len__(self) -> int:
        ''' return the length of a podcast, so obj creator can do len(podcast) '''
        return len(self._episodes)

    def __str__(self) -> str:
        ''' Return string representation of the podcast ''' 
        return str(f"{self._title} hosted by {self._host}, with "
                   f"{len(self)} total episodes, and "
                   f"total duration {self.__total_duration}")
