'''
    Finished code from class on 3/11/26

    We have a Donut class and a PremiumDonut(Donut) class

    Today we added to the Donut class:
    * Override __lt__, so that d1 < d2 works, and sorted(lstofdonuts) works
    * Override __hash__, so that we can put our objects into a set or dictionary keys
        - in __hash__, we call hash() and pass in a tuple of immutable attributes
        - those immutable attributes are the same ones we use in __eq__
    
    We also created a new class: BagOfDonuts
    * A container to hold Donut objects
    * Now we don't just ahve indv objects, but a container of them
    * We overrode __iter__, so we can iterate over an object of this type
'''
from __future__ import annotations
from collections.abc import Hashable, Iterable, Iterator

class DonutException(Exception):
    ''' make our own exception for donuts '''
    def __init__(self, msg: str = "Error making the donuts :("):
        super().__init__(msg)

class Donut(Hashable):
    ''' class to represent a sweet treat at dunkin donuts '''
    _menu = ["glazed", "jelly", "boston cream"]
    _type = "donut"

    def __init__(self, flavor: str, price: float):
        ''' initialize a donut '''
        self.flavor = flavor
        self.price = price

    @property
    def flavor(self) -> str:
        ''' return the flavor of the donut '''
        return self._flavor

    @flavor.setter
    def flavor(self, flave: str) -> None:
        ''' set the flavor of the donut to the given string
            Raises: donut error if invalid flavor
          '''
        if flave.lower() not in type(self)._menu:
            raise DonutException("No such flavor on the menu")
        self._flavor = flave

    @property
    def price(self) -> float:
        ''' return the price of the donut '''
        return self._price

    @price.setter
    def price(self, price: float) -> None:
        ''' set the price of the donut to the given float.
            raises: donut error if invalid price 
        '''
        if price < 1:
            raise DonutException("Price too low for profit margins :(")
        self._price = price

    def __str__(self) -> str:
        ''' print-friendly string to rep the donut '''
        return f"{self.flavor} donut, ${self.price}"

    def __eq__(self, other: object) -> bool:
        ''' are these two donuts the same? Yes if they have the same flavor and price'''
        if not isinstance(other, Donut):
            return False
        return self._flavor == other._flavor and self._price == other._price

    def __lt__(self, other: object) -> bool:
        ''' return boolean indicating if self < other '''
        if not isinstance(other, Donut):
            return NotImplemented
        return self.flavor < other.flavor

    def __hash__(self) -> int:
        ''' hash a donut object by passing in a tuple of immutable attributes '''
        return hash((self.flavor, self.price))

    @classmethod
    def from_menu(cls, index: int = 0, price: float = 1.99) -> Donut:
        ''' alt to init, using from_menu to create a donut given an index instead of a flavor '''
        try:
            return cls(cls._menu[index], price) # calling the regular init
        except IndexError as e:
            raise DonutException("could not make donut with that flavor") from e

    @staticmethod
    def is_valid_code(code: str) -> bool:
        ''' static method to determine whether a coupon code is valid '''
        return code.upper().startswith("DONUT") and code[5:].isdigit()

    @staticmethod
    def get_type_static() -> str:
        ''' what type of donut am I? '''
        return Donut._type

    @classmethod
    def get_type_class(cls) -> str:
        ''' what type of donut am I'''
        return cls._type

    @classmethod
    def get_menu(cls) -> list[str]:
        ''' return the menu of possible flavors (make a copy so we 
            don't have a mutability problem) 
        '''
        return cls._menu.copy()

class PremiumDonut(Donut):
    ''' a premium donut IS-A donut '''
    _menu = ["pride vanilla", "matcha", "truffle"]
    _type = "Premium Donut"

class BagOfDonuts(Iterable[Donut]):
    ''' make a bag of donuts '''
    def __init__(self, donuts: set[Donut]):
        ''' make a bag of donuts '''
        self.bag = donuts

    def __iter__(self) -> Iterator[Donut]:
        ''' what to look for "next" in the middle of a for loop '''
        return iter(self.bag)

    def get_total_cost(self) -> float:
        ''' sum up total price of all my donuts int he bag '''
        return sum([d.price for d in self.bag])
