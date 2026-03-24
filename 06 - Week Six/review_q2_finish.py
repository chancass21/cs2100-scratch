'''
    CS2100
    Spring 2026
    Starter code for class on Wednesday 2/11/26

    These are practice problems! Fill in the function stubs for as many
    or as few as you would like.

    Notice the use of the Any type. That's because these functions will work
    the same no matter what is contained in their list/set/tuple/dictionary :)

    We'll work together on a few them during class, and then run the tests
    in test_review_q2.py to make sure everything works as expected.

    Pick your favorites... (starred ones are MOST relevant for quiz 2)
    1. **create_email (practice with default params and strings)
    2. normalize_lst (normalization with a list instead of a dataframe)
    3. dedupe (practice with data structures)
    4. **find_common (practice with data structures)
    5. swap_pairs (practice with tuples)
    6. has_required (practice with sets)
    7. **get_seconds (practice with lists and dictionaries)
    8. **Book class (practice with classes and objects, __str__, default params)
'''

from typing import Any

def create_email(recipient: str, subject: str = "No Subject",
                 sender: str = "noreply@northeastern.edu") -> str:
    ''' return a string formatted for an email message
    
        parameters:
            recipient (str), the email address to send to (REQUIRED)
            subject (str), optional. the email subject line (default: "No Subject")
            sender (str), optional. the sender's email (default: "noreply@university.edu")
        
        returns:
            str, a formatted email string with items sepaerated by linebreaks
            Ex: "From: noreply@northeastern.edu
                 To: student@northeastern.edu
                 Subject: Subject
        raises:
            ValueError if recipient is empty string
     '''
    if not recipient:
        raise ValueError("Need recipient to send an email")
    return str(f"From: {sender}\n"
               f"To: {recipient}\n"
               f"Subject: {subject}")

def normalize_lst(lst: list[float]) -> list[float]:
    ''' normalize a list of floats using min-max scaling.

        parameters: 
            lst, a list of floats to normalize
        
        returns:
            a list of floats, the normalized values all between 0-1

        raises:
            value error if list has fewer than two elements
            value error if max and min are same value
    '''
    if len(lst) < 2:
        raise ValueError("List too short to normalize")
    mx = max(lst)
    mn = min(lst)
    if mx == mn:
        raise ValueError("Can't normalize a list where max == min")
    return [(x - mn) / (mx - mn) for x in lst ]

def dedupe(lst: list[Any]) -> list[Any]:
    ''' remove duplicates from the given list

        parameters:
            lst, a list of any data type
        
        returns:
            lst, also any data type, with dupes removed
        
        raises:
            value error if list is empty
    '''
    if not lst:
        raise ValueError("Can't dedupe an empty list")
    return list(set(lst))

def find_common(lst1: list[Any], lst2: list[Any]) -> set[Any]:
    ''' find common elements between two lists

        parameters: 
            lst1, lst2, both of type [Any] to find common elements
        
        returns:
            set[Any], the elements that appear in both lists
        
        raises:
            value error if either list is empty
    '''
    if not lst1 or not lst2:
        raise ValueError("Can't find common elements in empty list")
    return set(lst1) & set(lst2)

def swap_pairs(lst: list[tuple[Any, Any]]) -> list[tuple[Any, Any]]:
    ''' swap pairs of tuples in the given list (e.g., [(1, 2), (3, 4)] -> [(2,1), (4,3)]

        parameters:
            lst, a list of pairs of tuples of type Any
        
        returns:
            list of tuple of Any, the same pairs of tuples as we started with,
            but with values swapped
        
        raises:
            value error if the given list is empty
    '''
    if not lst:
        raise ValueError("Can't swap values in an empty list!")
    return [(b, a) for (a, b) in lst]


def has_required(avail: set[Any], req: set[Any]) -> bool:
    ''' determine whether all required elements are available
        ex: {'a', 'b', 'c'}, {'b'} returns True
            {'a', 'b', 'c'}, {'b', 'd'} returns False
    
        parameters:
            avail, req, both sets of type Any
        
        returns: 
            a boolean indicating whether ALL required elements appear in available set
        
        raises:
            value error if either set is empty
    '''
    if not avail or not req:
        raise ValueError("Both sets must be non-empty!")
    return set(req).issubset(avail)


def get_seconds(person: str, connections: dict[str, list[str]]) -> set[str]:
    '''  finds a list of second-level connections for the given person. 
         A second-level connection is someone your connection is connected to,
         but YOU are not connected to.
         A second-level connection cannot be someone you're connected to, or yourself.

         parameters:
            person (str), the name of the person whose second-level connections
                we're looking for
            connections (dict[str, list[str]]), the person's first-level connections (keys)
                and THEIR connections (values)
        
        returns:
            a set of strings, the person's second-level connections 
            (a person cannot be their own second-level connection)
        
        raises:
            valueError if dictionary is empty
            valueError if person is the empty string
    '''
    if not connections or not person:
        raise ValueError("Need the person's name and the dictionary of connections")
    second_level = set()
    for friends in connections.values():
        for connect_2 in friends:
            if connect_2 not in connections and connect_2 != person:
                second_level.add(connect_2)
    return second_level

#     write a class to represent a Book. It should have attributes for
#     title, author, and number of pages read.

#     Its constructor should take in title, author, and number of pages read
#     ALL as default parameters with reasonable default values.
#     (number of pages read should default to 0; the others you can choose)

#     Write a method to increase the number of pages read by a given value.

#     Write the __str__ method to print the title, author, and pages read in the
#     following format: "Read so far: {pages} pages"

class Book:
    ''' class to represent a book '''
    def __init__(self, title: str = "moby dick", author: str = "melville", pages: int = 0):
        ''' create a Book object '''
        self.title = title
        self.author = author
        self.pages_read = pages

    def increase_pages(self, incr: int) -> None:
        ''' increase pages read by the given amount. Do nothing if incr < 1 '''
        if incr >= 1:
            self.pages_read += incr

    def __str__(self) -> str:
        ''' return a string version of the Book object '''
        return f"Read so far: {self.pages_read} pages"
