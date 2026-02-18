'''
    Practice problems to work on visibility and properties.

    In general we want to enforce the conventions that:
    * the class creator is responsible for attributes
    * the object creator calls methods and doesn't mess with attributes

    Write a class to represent a winter olympian. Your class should have attributes
    for:
    - country (str)
    - sport (str)
    - medals (list of strings)

    All of your attributes should be internal, i.e., have a leading underscore (_)

    For each of the first two attributes, write a @poperty and a @xx.setter
    The setters should validate the new values, however you wish. Raise a value
    error in case of an invalid value.

    Write a add_medal method that takes in a string (gold, silver, bronze) and adds
    to the list of medals. 
    
    Implement the __len__ method to return the number of medals the athlete has won.
'''

class Olympian:
    ''' class to represent a winter olympic athlete '''