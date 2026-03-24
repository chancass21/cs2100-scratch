'''
    Practice problems with class/static methods, and inheritance


    Create an Animal class with:
    - A class variable for species and sound
    - An init method that takes a name (string)
    - A from_rescue_record, alt to init, a class method that takes a 
        dict with a "name" key
    - A get_species class method
    - An is_valid_name static method that returns False if the name contains non-alpha characters
    - A speak method that returns a string with the animal's name and sound

    Create two sublcasses that inherit from animal: dog and cat
    - they each ahve their own species and sound

    In your main, create a few different objects of each type and call the various methods.
'''

from __future__ import annotations

class Animal:
    ''' class to represent an animal, with some practice on class and static methods 
        and inheritance
    '''
    _sound = "..."
    _species = "unknown"

    def __init__(self, name: str):
        ''' make an animal with a given name '''
        self.name = name

    @classmethod
    def from_rescue_record(cls, record: dict[str, str]) -> Animal:
        ''' class method: create an Animal object from a record instead of a string ''' 
        return cls(record["name"])

    @classmethod
    def get_species(cls) -> str:
        ''' class method: what is the species? Use cls here to dynamically 
            get the right sub/super class 
        '''
        return cls._species

    @staticmethod
    def is_valid_name(name: str) -> bool:
        ''' static method: validate a name; is it all alpha? '''
        return name.isalpha()

    def speak(self) -> str:
        ''' regular method: what noise does the animal make? '''
        return f"{self.name} says {self._sound}"

class Dog(Animal):
    ''' dog inherits from animal and has its own soundn and species '''
    _sound = "woof"
    _species = "Canine"

class Cat(Animal):
    ''' cat inherits from animal and has its own sound and species '''
    _sound = "meow"
    _species = "Feline"

def main() -> None:
    ''' make some animals '''
    # call the regular init method for dog and cat
    dog = Dog("Grizz")
    cat = Cat("Shawna")
    print(dog.speak())
    print(cat.speak())

    # call the alt init method, the from_rescue class method
    rescue_dog = Dog.from_rescue_record({"name": "Carol"})
    rescue_cat = Cat.from_rescue_record({"name": "Rosie"})
    print(rescue_dog.speak())
    print(rescue_cat.speak())

    # class methods — same method, different results!
    print(Dog.get_species())
    print(Cat.get_species())
    print(Animal.get_species())

    # static method -- validate the names
    print(Animal.is_valid_name("Rex"))      # True
    print(Animal.is_valid_name("Rex123"))   # False


if __name__ == "__main__":
    main()