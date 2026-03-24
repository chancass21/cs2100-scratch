'''
   CS2100
   Spring 2026

    This is the Runner class we defined in class on 1/26 (mon)

    In lecture on 1/28, we'll
    * test this code
    * create objects out of this class
'''


class Runner:
    ''' class to define a runner '''
    def __init__(self, name: str, filename: str):
        ''' constructor for a runner class, takes a runner's name (str),
            and a filename (str) to read their data from, and creates
            empty dictionaries [str, float] as attributes '''
        self.name = name
        self.file = filename
        self.miles: dict[str, float] = {}
        self.stats: dict[str, float] = {}

    def gather_mileage_input(self) -> None:
        ''' read mileage input from a file, stores in miles attr,
            overwriting if miles already existed

            parameters: none (uses self.file as filename, and self.miles as mileage dictionary)

            returns: none

            raises:
              IOError if file reading generates no content
              FileNotFoundError if file doesn't exist

        '''
        with open(self.file, 'r', encoding='utf-8') as file:
            content = file.readlines()
            if not content:
                raise IOError("File reading unsuccessful")

        dates = content[0].strip().split(",")
        miles = content[1].split(",")
        self.miles = {date : float(mile) for date, mile in zip(dates, miles)}


    def generate_mileage_stats(self) -> None:
        ''' compute basic stats from a mileage list: total, avg daily
            and stores in stats attribute, overwriting these keys if they already existed

            parameters: none
            
            returns: None

            raises: Value Error if any miles in dictionary values are negative
                        
        '''
        if any(mileage < 0 for mileage in self.miles.values()):
            raise ValueError("Miles can't be negative :(")
        self.stats["total miles"] = sum(self.miles.values())
        self.stats["avg daily"] = sum(self.miles.values()) / len(self.miles.values())

    def print_summary(self) -> None:
        ''' print a summary of the stats in the given dictionary 
        
            parameters:
                none, uses attributes
            returns:
                none, just prints
        '''
        print(f"Running stats for {self.name}:")
        for key, value in self.stats.items():
            print(f"{key}...{value}")
        print()

    def __str__(self) -> str:
        ''' returns a nicely formatted string to rep the object, for the user '''
        return f"Runner {self.name} ran {self.stats['total miles']} miles, great job!"

    def __repr__(self) -> str:
        ''' returns an informative,  detailed string to rep the object, for the programmer '''
        s = "here is info for you on the Runner object...\n"
        s += f"\tname - {self.name}\n"
        s += f"\tfilename - {self.file}\n"
        s += f"\tmileage dict - {self.miles}\n"
        return s
