'''
   CS2100
   Spring 2026
   Finished code from class -- 1/12/26

    This program prompts the user for the daily mileage of two runners and compares them.

    In class, we changed a list into a dictionary, where we went from:
    * stats[0] = total mileage
    * stats[1] = avg daily mileage
    to a dictionary with:
    * stats["total miles"] = total mileage
    * stats["avg daily"] = avg daily mileage

    Before posting this code, Laney also changed the othere lists into dictionaries, so we have:
    * laney_stats["date"] = miles on that date
    * nate_stats["date"] = miles on that date

    For testing generate_mileage_stats...
    * basic cases are ok :)
    * how should we handle empty input?
    * how should we handle negative miles?

    For wednesday 1/13, we will consider edge cases of an empty input, or negative miles. 
    We'll also write a function to generate the report, and test that too.
    
    Empty input options...
    * Python raises an error
    **** We raise an error (better error message)
    **** Return zeroes {"total" : 0, "avg" : 0}
    * Return None

    Negative miles options...
    ***** we raise an error
    * return None
    * leave it as-is (do the computation with negatives)
'''

def gather_mileage_input(name: str, dates: list[str]) -> dict[str, float]:
    ''' prompt the user to enter mileage information, validating values >= 0
  
       Parameters:
           name (str): who we're collecting data for
           dates (list: str): list of dates to prompt for
      
       Returns:
           a dictionary [str, float] where key = date, value = mileage on that date
      
    '''
    miles = {}
    for date in dates:
        today_miles = float(input(f"How many miles did {name} run on {date}?\n"))
        while today_miles < 0:
            today_miles = float(input("Enter again, miles can't be negative!\n"))
        miles[date] = today_miles
    return miles


def generate_mileage_stats(miles: dict[str, float]) -> dict[str, float]:
    ''' compute basic stats from a mileage list: total, avg daily
        return a dictionary with stat : value pairs
  
       Parameters:
           miles (list[float]): a list containing a runner's mileage per-day
      
       Returns:
           dict[str, float]: summary stats for total miles and avg daily miles for that runner
    '''
    stats = {}
    stats["total miles"] = sum(miles.values())
    stats["avg daily"] = sum(miles.values()) / len(miles.values())
    return stats


def main() -> None:
    ''' create lists for Laney and Nate's last week of running and compute stats about them '''

    dates = ["JAN 07", "JAN 08", "JAN 09", "JAN 10", "JAN 11"]
    laney_miles = gather_mileage_input("Laney", dates)
    nate_miles = gather_mileage_input("Nate", dates)

    # Compute basic stats about the week of running for each person
    laney_stats = generate_mileage_stats(laney_miles)
    nate_stats = generate_mileage_stats(nate_miles)

    # Report the stats from their dictionaries (repeated code here though :( Maybe a function is better?)
    print("Laney's running stats...")
    for key, value in laney_stats.items():
        print(f"{key}...{value}")
    print("Nate's running stats...")
    for key, value in nate_stats.items():
        print(f"{key}...{value}")

     # follow-up on a specific date, what does the user want to know?
    month, day = input("Which day do you want to know about? Enter as MMM DD\n").upper().split()
    while not month.isalpha() or not day.isdigit():
        month, day = input("Please enter as MMM DD\n").upper().split()

    date = " ".join([month, f"{int(day):02d}"])
    if date not in dates:
        print(f"Sorry, we don't have data for {date}\n")
        return

    print(f"Laney's mileage that day: {laney_miles[date]}")
    print(f"Nate's mileage that day: {nate_miles[date]}")

if __name__ == "__main__":
    main()
