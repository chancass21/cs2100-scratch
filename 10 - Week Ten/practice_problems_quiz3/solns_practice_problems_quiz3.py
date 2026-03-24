'''
    Solutions for practice problems from class on 3/18/26
'''

from collections.abc import Iterable, Iterator, Hashable
from abc import ABC, abstractmethod


################################################################
#
# PROBLEM ZERO  - Write a custom exception, inherited from Exception
# for a Runner
#
################################################################
class RunnerError(Exception):
    def __init__(self, msg: str = "Runner error, watch the lead vehicle :("):
        super().__init__(msg)

################################################################
#
# PROBLEM ONE  - Write a class to represent a Runner. It should
# have attributes name, age, and is_pro, with @property but no
# setters.
# Printing out a runner prints their name, age, and whether they are a pro
# R1 < R2 if they are younger.
# R1 == R2 if they are the same name and same age.
# A Runner should be hashable
#
################################################################
class Runner(Hashable):
    def __init__(self, name: str, age: int, is_pro: bool = False):
        ''' make a runner object '''
        self._name = name
        self._age = age
        self._is_pro = is_pro
    
    @property
    def name(self) -> str:
        ''' return the name attribute '''
        return self._name

    @property
    def age(self) -> int:
        ''' return the age attribute '''
        return self._age
    
    @property
    def is_pro(self) -> bool:
        ''' return the is_pro attribute '''
        return self._is_pro
    
    def __str__(self) -> str:
        ''' nicely formatted string '''
        return f"{self._name}, {self._age}{' *pro' if self._is_pro else ''}"
    
    def __lt__(self, other: object) -> bool:
        ''' is self < other? '''
        if not isinstance(other, Runner):
            return NotImplemented
        return self._age < other._age
    
    def __eq__(self, other: object) -> bool:
        ''' is self == other? '''
        if not isinstance(other, Runner):
            return False
        return self._name == other._name and self._age == other._age

    def __hash__(self) -> int:
        ''' hash the runner '''
        return hash((self._name, self._age))


################################################################
#
# PROBLEM  TWO - Write a container class to hold a field. It should
# have a list of runner objects in sorted order. I should be
# able to add a runner, remove all instances of a runner, 
# and the list stays in sorted order.
# An object of this class should be iterable
#
################################################################
class Field(Iterable[Runner]):
    ''' field container of runner objects '''
    def __init__(self):
        ''' initialize the object '''
        self._runners: list[Runner] = []
    
    def add_runner(self, r: Runner) -> None:
        ''' add a runner to the list, maintain order '''
        self._runners.append(r)
        self._runners.sort()

    def remove_runner(self, r: Runner) -> None:
        ''' remove a runner from the list, maintain order '''
        if r not in self._runners:
            raise RunnerError
        self._runners = [run for run in self._runners if r != run]

    def __iter__(self) -> Iterator[Runner]:
        return iter(self._runners)


################################################################
#
# PROBLEM THREE  - Write a abstract class to represent a footrace. It should 
# have a distance in miles, a name, and a field of runners.
# Keep track of how many Race instances have been created.
# Write a method for a runner to register for this race
# Write an abstract method, youngest, that tells you the youngest (valid) 
# runner in the race
# Write a static method that converts from KM to miles
#
################################################################

class Race(ABC):
    ''' class for a race (abstract)'''
    race_count = 0 

    def __init__(self, name, distance: float):
        self._name = name
        self._distance = distance
        self._field = Field()
        Race.race_count += 1

    def register(self, r: Runner):
        ''' the runner registers for the race '''
        self._field.add_runner(r)

    @abstractmethod
    def youngest(self) -> Runner:
        pass

    @classmethod
    def total_races(cls):
        return cls.race_count
    
    def __str__(self) -> str:
        ''' return a string version of the race '''
        return f"{self._name}, {self._distance} miles"
    
    @staticmethod
    def km_to_miles(km: float) -> float:
        ''' static method to convert distance'''
        return km / 1.60934

################################################################
#
# PROBLEM FOUR  - Write two classes that inherit from Race,
# FiveK and TenK. A 5K is 3.1 miles and a 10K is 6.2 miles.
# No min age to be a valid participant in the 5k.
# A runner has to be at least 13 years old to be a valid participant in the 10k.
# Each of these classes should impelment the inherited youngest() method,
# returning the youngest Runner in the field as long as they are >= the min age.
#
################################################################

class FiveK(Race):
    ''' class for a 5K race '''
    def __init__(self, name):
        ''' create a 5k race given its name '''
        super().__init__(name, round(Race.km_to_miles(5), 2))

    def youngest(self) -> Runner:
        ''' return the youngest runner in the race '''
        if not self._field:
            raise RunnerError("No runners in race")
        return min(self._field)

class TenK(Race):
    ''' class for a 10K race '''
    def __init__(self, name):
        ''' create a 10k race given its name '''
        super().__init__(name, round(Race.km_to_miles(10), 2))
        self._min_age = 13

    def youngest(self) -> Runner:
        ''' return the youngest runner in the race, as long as they are old enough '''
        overage = [r for r in self._field if r.age >= self._min_age]
        if not overage:
            raise RunnerError("No valid runners in race")
        return min(overage)


def main() -> None:
    ''' make some runners and races, un-comment in chunks as you finish the practice '''

    ################################################################
    #
    # UNCOMMENT FOR PROBLEM ONE
    #
    ################################################################

    print("===========Making two Runner objects and printing them out=============")
    laney = Runner("laney s", 47)
    nate = Runner("nate d", 41)
    amy = Runner("amy g", 35, True)
    kid1 = Runner("kid 1", 9)
    kid2 = Runner("kid 2", 5)
    print(laney, nate)

    print("\n==========Putting my runners in a list and sorting=============")
    runner_list = [laney, amy, nate]
    sorted_runners = sorted(runner_list)
    print([str(r) for r in sorted_runners])

    print("\n==========Looking for a Runner in the list, should work if __eq__ is ok!=============")
    print("Laney in list!" if laney in runner_list else ":()")
    print("Kid 1 in list!" if kid1 in runner_list else "kid not in list")

    print("\n==========Putting my runners in a set, should work if eq and hash are ok!=============")
    runner_set = {laney, amy, nate}
    print([str(r) for r in runner_set])



    ################################################################
    #
    # UNCOMMENT FOR PROBLEM TWO
    #     
    ################################################################

    print("\n===========Making a Field of Runners=============")
    field = Field()
    for r in runner_list:
        field.add_runner(r)

    print("\n===========Printing the Field of Runners with Iter=============")
    for f in field:
        print(f)


    ################################################################
    #
    # UNCOMMENT FOR PROBLEMS THREE AND FOUR
    #     
    ################################################################
    print("\n===========Getting my distances right using the static method=============")
    fivek_miles = Race.km_to_miles(5)
    tenk_miles = Race.km_to_miles(10)
    print(f"A 5K is {round(fivek_miles, 2)} miles and a 10K is {round(tenk_miles, 2)}")


    print("\n===========Making a 5k race and a 10k race=============")
    dot_day = FiveK("Dot Day 5k")
    dot_day.register(laney)
    dot_day.register(nate)
    dot_day.register(kid1) # ok for 5k
    dot_day.register(kid2) # too young for 10k
    print(dot_day)
    print(f"Youngest runner in the field... {dot_day.youngest()}")

    pynr = TenK("Pioneers 10k")
    pynr.register(laney)
    pynr.register(nate)
    pynr.register(amy)
    pynr.register(kid1) # ok for 5k
    pynr.register(kid2) # too young for 10k
    print(pynr)
    print(f"Youngest runner in the field... {pynr.youngest()}")

if __name__ == "__main__":
    main()
