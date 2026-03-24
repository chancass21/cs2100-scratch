'''
    Solutions to problems for recursion

    In class, we mostly focused on recursing over trees. 
    A recursive function is a function that calls itself -- 
        and recursive solutions to programming problems can be 
        helpful and easy to write!

    Don't worry about raising errors for these, assume input values 
    are valid.
'''


###########################################################################
#
# Recursion Practice #1
# Write a function to recursively compute n!
# (n! = n * n-1 * n-2 * ... * 1)
# base case: 1! = 1
# recursive step: multiply n * factorial of n-1
#
###########################################################################
def factorial(n: int) -> int:
    ''' compute n! recursively '''
    if n <= 1:
        return 1
    return n * factorial(n - 1)

###########################################################################
#
# Recursion Practice #2
# Write a function to recursively calculate and return  the nth fibonacci number
# nth fibonacci number: (n-1)th + (n-2)th fibonacci number
# 1, 1, 2, 3, 5, 8, 13, 21, 34
# base cases: fib(1) = 1, fib(2) = 1
# recursive step: sum the previous two fib numbers
#
###########################################################################
def fib(n: int) -> int:
    ''' calculate and return the nth fibonacci number '''
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


###########################################################################
#
# Recursion Practice #3
# Write a function to recursively determine if a string is a palindrome
# palindrome == same backwards and forwards
# base case: a string of length 0 or 1 is a palindrome
# recursive step: are first and last characters the same? Then remove
#       them and look at the remaining substring
#
###########################################################################
def palindrome(s: str) -> bool:
    ''' is this string a palindrome? '''
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])

##########################################################################
#
# Recursion Practice #4
# Write a function to recursively sum the elements in a list of ints
# base case: sum of a list of length 0 is 0
# recursive step: sum the first element + rest of list
#
###########################################################################
def rec_sum(lst: list[int]) -> int:
    ''' what is the sum of ints in this list? '''
    if len(lst) == 0:
        return 0
    return lst[0] + rec_sum(lst[1:])

##########################################################################
#
# Recursion Practice #5
# Write a function to recursively find the max in an list of ints
# base case: the max of a list of length 1 is the only element
# (you can assume you never get an empty list here)
# recursive step: find the max of the first element and rest of the list
#
###########################################################################
def rec_max(lst: list[int]) -> int:
    ''' what is the max of ints in this list? '''
    if len(lst) == 1:
        return lst[0]
    return max(lst[0], rec_max(lst[1:]))
