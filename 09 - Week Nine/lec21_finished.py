'''
    Finished code from class on 3/9/26

    We have a Donut class and a PremiumDonut(Donut) class

    They each have two class variables -- one for flavors, and one for what type of thing you are.
    They have your usual attributes which are intenral (_) and their property and setters
    Super class has __str__ and __eq__, not overridden by sublcass
    Look for type(self), it's the TYPE of thing self is, vs. self is an instance
    Functionally type(self) as cls do the same thing
    
    We added:
    * Class method as alt to the usual init
    * Class method to return the menu (like @property but for a class variable)
    * Static method to validate a coupon code

    Look out for:
    * @classmethod, @staticmethod decorators
    * A class method has cls as its first parameter, instead of self
    * A static method has no cls or self, it looks more like an ordinary function
    * cls._menu -- this is dynamic and helps with inheritance in a class method
    * type(self)._menu -- this is dynamic and helps with inheritance in a regular method!
'''

from __future__ import annotations

class DonutException(Exception):
    ''' make our own exception for donuts '''
    def __init__(self, msg: str = "Error making the donuts :("):
        super().__init__(msg)

class Donut:
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
            type(self) functionally equivalent to doing cls in a class method
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

    @classmethod
    def from_menu(cls, index: int = 0, price: float = 1.99) -> Donut:
        ''' class method example: alternate to init '''
        try:
            return cls(cls._menu[index], price)
        except IndexError as e:
            raise DonutException(f"No such index in menu: {index}") from e

    @staticmethod
    def is_valid_code(code: str) -> bool:
        ''' returns a bool indicating whether given string is a valid coupon '''
        return code.upper().startswith("DONUT") and code[5:].isdigit()

    @classmethod
    def get_menu(cls) -> list[str]:
        ''' return the menu of possible donuts '''
        return cls._menu.copy()

    @classmethod
    def my_type_cls(cls) -> str:
        ''' return the type of donut (class version) '''
        return cls._type

    @staticmethod
    def my_type_static() -> str:
        ''' return the type of donut (static version) '''
        return Donut._type


class PremiumDonut(Donut):
    ''' a premium donut IS-A donut '''
    _menu = ["pride vanilla", "matcha", "truffle"]
    _type = "Premium Donut"
