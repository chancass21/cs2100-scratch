'''
   CS2100
   Spring 2026
   Starter code for class on 1/26/26

   here we have the runner functions we've already written,
   and we want to turn them into methods of a class.

   - What attributes should our Runner class have?
   - How should we adapt the functions into methods
'''

from typing import Optional


def gather_mileage_input(filename: str) -> dict[str, float]:
    ''' read mileage input from a file
  
        Parameters:
           filename: str, the name of the file to read from
      
        Returns:
           a dictionary [str, float] where key = date, value = mileage on that date
      
        Raises:
            IOError if attempt to read file returns nothing
            FileNotFoundError if file doesn't exist
    '''
    with open(filename, 'r', encoding='utf-8') as file:
        dates = file.readline()
        miles = file.readline()
        if not dates or not miles:
            raise IOError("File reading unsuccessful")

        dates = dates.strip().split(",")
        miles = miles.split(",")
        dct = {date : float(mile) for date, mile in zip(dates, miles)}
        return dct


def generate_mileage_stats(miles: Optional[dict[str, float]]) -> Optional[dict[str, float]]:
    ''' compute basic stats from a mileage list: total, avg daily
        return a dictionary with stat : value pairs
  
       Parameters:
           miles (list[float]): a list containing a runner's mileage per-day, or None
      
       Returns:
            dict[str, float]: summary stats for total miles and avg daily miles 
            for that runner, or None if none/empty dictionary given
        
        Raises:
            ValueError if any miles are negative
    '''
    if not miles:
        return None
    if any(mileage < 0 for mileage in miles.values()):
        raise ValueError("Miles can't be negative :(")
    stats = {}
    stats["total miles"] = sum(miles.values())
    stats["avg daily"] = sum(miles.values()) / len(miles.values())
    return stats

def print_summary(name: str, stats: dict[str, float]) -> None:
    ''' print a summary of the stats in the given dictionary 
    
        parameters:
            name (str), the name of the runner
            stats (dict of str, float), the stats for the runner's summary
        returns:
            none, just prints
    '''
    print(f"Running stats for {name}:")
    for key, value in stats.items():
        print(f"{key}...{value}")
    print()
