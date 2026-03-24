'''
    Practice problems for ABC's!

    Create an abstract superclass to represent a bank account.
        It's abstract, because a "real" bank account needs to be either
        checking or savings, it can't be this generic.

    Create two subclasses that inherit from bank acccount,
        one for checking and one for savings

    Bank account's abstract methods, which HAVE TO be implemented by subclasses:
    * withdraw
    * get_account_type
    Bank account's concrete methods, which COULD be overridden by subclasses if you want to:
    * deposit
    * get_balance
    Bank account's attributes, inherited by both subclasses:
    * account_number, a string
    * balance, an int 

    Subclass-specific:
    * checking: attribute for overdraft_limit; impacts how withdrawal works
    * savings: attribute for interest rate; method to apply the interest to current balance

    Feel free to add additional methods/attributes to the subclasses :)
'''