'''
    a class to represent a winter olympian

    class creator - responsible for the attribute 
    object creator - call class methods

    _attrname - internal use, for the class only

    @property - share the value of an attribute
    @xx.setter - change the value of an attribute
'''

# could this live in a better place? we will talk about class variables soon!
VALID_SPORTS = ["skiing", "luge", "hockey", "nordic skiing", "ice skating", "skeleton"]
WINTER_COUNTRIES = ["USA", "Canada", "Norway", "Finland", "Korea", "China", "Mexico"]
MEDALS = ["gold", "silver", "bronze"]

class Olympian:
    ''' represent a winter olympian '''
    def __init__(self, country: str, sport: str):
        ''' initialize an olympian with the given country and sport

            parameters: (strings)
            country, sport
            what country they represent, and their main sport
         '''
        self.sport = sport
        self.country = country
        self._medals: list[str] = []

    def _validate_sport(self, sport: str) -> None:
        ''' validate the given sport
            parameter: sport, a string
            returns: none
            raises: value error if sport not valid, or is empty string 
        '''
        if not sport or sport.lower() not in (sport.lower() for sport in VALID_SPORTS):
            raise ValueError("invalid sport :(")

    def _validate_country(self, country: str) -> None:
        ''' validate the given country
            parameter: country, a string
            returns: none
            raises: value error if country not in winter olympmics, or is empty string 
        '''
        if not country or country.lower() not in (country.lower() for country in WINTER_COUNTRIES):
            raise ValueError("country does not compete in winter olympics")

    @property
    def sport(self) -> str:
        ''' return the _sport attribute
            parameters: none
            returns: string
        '''
        return self._sport

    @sport.setter
    def sport(self, new_sport: str) -> None:
        ''' update the _sport attribute
            parameters: new_sport, a string
            returns: none
            raises: value error if new_sport is not valid
        '''
        self._validate_sport(new_sport)
        self._sport = new_sport

    @property
    def country(self) -> str:
        ''' return the _countryt attribute
            parameters: none
            returns: string
        '''
        return self._country

    @country.setter
    def country(self, new_country: str) -> None:
        ''' update the _country attribute
            parameters: new_country, a string
            returns: none
            raises: value error if new_country is not a winter olympic country
        '''
        self._validate_country(new_country)
        self._country = new_country

    def add_medal(self, medal: str) -> None:
        ''' add the given medal to the list of medals
            parameters: medal, a string
            returns: none
            raises: Value error if medal not valid 
        '''
        if medal.lower() not in (medal.lower() for medal in MEDALS):
            raise ValueError("medal not valid")
        self._medals.append(medal)

    def __len__(self) -> int:
        ''' return the total medals for the athlete '''
        return len(self._medals)


def main() -> None:
    ''' create olympic objects '''
    breezy = Olympian("USA", "skiing")

    # don't do this :(
    # print(breezy._sport)

    # do this instead :):):):)
    print(breezy.sport)

    # don't do this :):(:(:(:(
    # breezy._sport = "luge"

    # do this instead
    breezy.sport = "luge"
    print(breezy.sport)


if __name__ == "__main__":
    main()
