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

    Subclass-specific:
    * checking: attribute for overdraft_limit; impacts how withdrawal works
    * savings: attribute for interest rate; method to apply the interest to current balance

    Feel free to add additional methods/attributes to the subclasses :)
'''

from abc import ABC, abstractmethod

class BankAccount(ABC):
    ''' abstract class for a bank account '''
    def __init__(self, acct_number: str):
        ''' create a bank account '''
        self.account_number = acct_number
        self._balance = 0

    @property
    def account_number(self) -> str:
        ''' return the account number '''
        return self._account_number

    @account_number.setter
    def account_number(self, new_num: str) -> None:
        ''' set the account number after validation '''
        if not new_num or not new_num.isdigit():
            raise ValueError("bad account number, can't use")
        self._account_number = new_num

    @property
    def balance(self) -> int:
        ''' property for _balance, returns an int '''
        return self._balance

    def deposit(self, amount: int) -> None:
        ''' Concrete method - all accounts deposit the same way 
            parameters: int, the amount to deposit
            returns: none
            raises: value error if deposit amount is <= 0
        '''
        if amount <= 0:
            raise ValueError("invalid deposit amount, must be positive")
        self._balance += amount

    @abstractmethod
    def withdraw(self, amount: int) -> None:
        ''' Abstract withdraw - different account types have different withdrawal rules '''
        pass

    @abstractmethod
    def get_account_type(self) -> str:
        ''' Abstract account type - each account identifies its type '''
        pass

class CheckingAccount(BankAccount):
    ''' define a checking account, inherits from BankAccount and implements abstract methods '''
    def __init__(self, account_num: str):
        ''' create chcking account from super '''
        super().__init__(account_num)
        self._overdraft_limit = 0

    @property
    def overdraft_limit(self) -> int:
        ''' return the max overdraft allowed on this account '''
        return self._overdraft_limit

    @overdraft_limit.setter
    def overdraft_limit(self, new_limit: int) -> None:
        ''' update the overdraft limit on the checking account,
            raise a value error if amount is negative
        '''
        if new_limit < 0:
            raise ValueError("overdraft limit can't be negative")
        self._overdraft_limit = new_limit

    def withdraw(self, amount: int) -> None:
        ''' implement superclass's abstract method to withdraw
            parameters: int, the amount to withdraw. balance attribute will be updated.
            returns: none
            raises: RuntimeError if amount is greater than balance + overdraft,
                    ValueError if amount to withdraw is 0 or negative
        '''
        if amount > self._balance + self._overdraft_limit:
            raise RuntimeError("insufficient funds :(")
        if amount <= 0:
            raise ValueError("invalid withdrawal amount")
        self._balance -= amount

    def get_account_type(self) -> str:
        ''' return the type of account '''
        return "checking account"

class SavingsAccount(BankAccount):
    ''' define a savings account, inherits from BankAccount and implements abstract methods '''
    def __init__(self, account_num: str, interest_rate: float):
        ''' create savings account from super '''
        super().__init__(account_num)
        self.interest_rate = interest_rate

    @property
    def interest_rate(self) -> float:
        ''' return the interest rate on this savings account '''
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, new_rate: float) -> None:
        ''' update the interest rate on the savibgs account,
            raise a value error if amount is negative
        '''
        if new_rate < 0:
            raise ValueError("interest rate can't be negative")
        self._interest_rate = new_rate

    def withdraw(self, amount: int) -> None:
        ''' implement superclass's abstract method to withdraw
            parameters: int, the amount to withdraw. balance attribute will be updated.
            returns: none
            raises: RuntimeError if amount is greater than balance
                    ValueError if amount is 0 or negative
        '''
        if amount > self._balance:
            raise RuntimeError("insufficient funds :(")
        if amount <= 0:
            raise ValueError("invalid withdrawal amount")
        self._balance -= amount

    def apply_interest(self):
        ''' method specific to savings account, apply interest to current balance '''
        interest = self._balance * self._interest_rate
        self._balance += interest

    def get_account_type(self) -> str:
        ''' return the type of account '''
        return "savings account"
