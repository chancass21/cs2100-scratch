'''
    CS2100
    Spring 2026

    Sample code from class -- runner_driver.py
    This is where main() will live, and create runner objects
'''

from runner import Runner
# from [module] import [classname]

LANEYFILE = "laney_stats.txt"
NATEFILE = "nate_stats.txt"

def main() -> None:
    ''' create a couple of runner objects and try them out '''
    laney = Runner("Laney", LANEYFILE)
    nate = Runner("Nate", NATEFILE)

    laney.gather_mileage_input()
    nate.gather_mileage_input()

    laney.generate_mileage_stats()
    nate.generate_mileage_stats()

    # print out the objects, nicely for the user
    print(laney)
    print(nate)
    print()

    # print out the objects, detailed for the programmer
    print(repr(laney))
    print(repr(nate))

if __name__ == "__main__":
    main()
