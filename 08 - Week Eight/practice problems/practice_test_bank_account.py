'''
    test the bank account abstract class, with subclasses checking and savings

    Make sure test for:
    * you can't create an object of type BankAccount, because it is abstract
    * create a basic checking account object, savings account object
    * make sure invalid account number, invalid interest rate, invalid overdraft limit
        would all trip exceptions
    * make sure making a deposit updates the balance
    * make sure you can't deposit an invalid amount
    * for a checking account, make sure you can't withdraw more than 
        balance + overdraft limit
    * for a savings account, make sure you can't withdraw more than balance
    * for a savings account, make sure interest is applied correctly
'''