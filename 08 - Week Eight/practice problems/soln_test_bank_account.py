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

import unittest
from soln_bank_account import BankAccount, CheckingAccount, SavingsAccount

class TestBankAccount(unittest.TestCase):
    ''' Test the abstract BankAccount class '''

    def test_cannot_instantiate_abstract_class(self):
        ''' BankAccount is abstract and cannot be instantiated '''
        with self.assertRaises(TypeError):
            account = BankAccount("fail", 100)


class TestCheckingAccount(unittest.TestCase):
    ''' Test CheckingAccount class -- concrete, can make objects '''

    def setUp(self):
        ''' create checkingaccount object for testing '''
        self.account = CheckingAccount("123")

    def test_invalid_setup(self):
        ''' test we can't create a checking account with an empty or non-digit account number '''
        with self.assertRaises(ValueError):
            CheckingAccount("abc")
        with self.assertRaises(ValueError):
            CheckingAccount("")

    def test_initialization(self):
        ''' test the values of properties after we set up a basic account'''
        self.assertEqual(self.account.account_number, "123")
        self.assertEqual(self.account.balance, 0)
        self.assertEqual(self.account.overdraft_limit, 0)

    def test_checking_account_setter(self):
        ''' change the account number via the setter and confirm '''
        self.account.account_number = "45"
        self.assertEqual(self.account.account_number, "45")

    def test_checking_account_setter_invalid(self):
        ''' test we can't change account number to empty string or non-digits '''
        with self.assertRaises(ValueError):
            self.account.account_number = "abc"
        with self.assertRaises(ValueError):
            self.account.account_number = ""
        with self.assertRaises(ValueError):
            self.account.account_number = "12a"

    def test_checking_overdraft_setter(self):
        ''' change the overdraft amount via the setter and confirm '''
        self.account.overdraft_limit = 50
        self.assertEqual(self.account.overdraft_limit, 50)

    def test_checking_overdraft_setter_invalid(self):
        ''' test we can't change overdraft limit to negative values '''
        with self.assertRaises(ValueError):
            self.account.overdraft_limit = -1

    def test_get_account_type(self):
        ''' ttest that it returns the correct type of account '''
        self.assertEqual(self.account.get_account_type().lower(), "checking account")

    def test_deposit_valid_amount(self):
        ''' Test depositing valid amounts '''
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 50)
        self.account.deposit(100)
        self.assertEqual(self.account.balance, 150)

    def test_deposit_zero(self):
        ''' we should get an error when depositing $0 or $neg'''
        with self.assertRaises(ValueError):
            self.account.deposit(0)
        with self.assertRaises(ValueError):
            self.account.deposit(-1)

    def test_withdraw_valid_amount(self):
        ''' Test withdrawing amount within balance + overdraft '''
        self.account.deposit(100)
        self.account.withdraw(30)
        self.assertEqual(self.account.balance, 70)

        self.account.overdraft_limit = 100
        self.account.withdraw(130)
        self.assertEqual(self.account.balance, -60)

    def test_withdraw_invalid_amount(self):
        ''' Test withdraws that should fail: invalid amount, more than balance, 
            and more than balance + overdraft
        '''
        with self.assertRaises(ValueError):
            self.account.withdraw(-1)
        with self.assertRaises(ValueError):
            self.account.withdraw(0)

        self.account.deposit(100)
        with self.assertRaises(RuntimeError):
            self.account.withdraw(150)

        self.account.overdraft_limit = 100
        with self.assertRaises(RuntimeError):
            self.account.withdraw(500)

    def test_multiple_transactions(self):
        ''' Test series of deposits and withdrawals '''
        self.account.deposit(50)   # $50
        self.account.withdraw(30)  # $20
        self.account.deposit(80)   # $100
        self.account.overdraft_limit = 50
        self.account.withdraw(150) # -50 (withdraw everything + overdraft)
        self.assertEqual(self.account.balance, -50)

class TestSavingsAccount(unittest.TestCase):
    ''' Test SavingsAccount class -- concrete, can make objects '''
    def setUp(self):
        ''' create savingsaccount object for testing '''
        self.account = SavingsAccount("123", 1.0)

    def test_invalid_setup(self):
        ''' test we can't create a savings account with a negative interest rate, 
            or a bad account name
        '''
        with self.assertRaises(ValueError):
            self.account = SavingsAccount("123", -1.0)
        with self.assertRaises(ValueError):
            self.account = SavingsAccount("abc", 1.0)
        with self.assertRaises(ValueError):
            self.account = SavingsAccount("abc", -1.0)

    def test_initialization(self):
        ''' test the values of properties after we set up a basic account'''
        self.assertEqual(self.account.account_number, "123")
        self.assertEqual(self.account.balance, 0)
        self.assertEqual(self.account.interest_rate, 1.0)

    def test_savings_account_setter(self):
        ''' change the account number via the setter and confirm '''
        self.account.account_number = "45"
        self.assertEqual(self.account.account_number, "45")

    def test_savings_account_setter_invalid(self):
        ''' test we can't change account number to empty string or non-digits '''
        with self.assertRaises(ValueError):
            self.account.account_number = "abc"
        with self.assertRaises(ValueError):
            self.account.account_number = ""
        with self.assertRaises(ValueError):
            self.account.account_number = "12a"
    
    def test_savings_interest_setter(self):
        ''' change the interest rate via the setter and confirm '''
        self.account.interest_rate = 2.5
        self.assertEqual(self.account.interest_rate, 2.5)

    def test_savings_interest_setter_invalid(self):
        ''' test we can't change interest rate to negative values '''
        with self.assertRaises(ValueError):
            self.account.interest_rate = -5

    def test_get_account_type(self):
        ''' ttest that it returns the correct type of account '''
        self.assertEqual(self.account.get_account_type().lower(), "savings account")

    def test_deposit_valid_amount(self):
        ''' Test depositing a valid amount '''
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 50)

    def test_deposit_zero(self):
        ''' we should get an error when depositing $0 or $neg'''
        with self.assertRaises(ValueError):
            self.account.deposit(0)
        with self.assertRaises(ValueError):
            self.account.deposit(-1)

    def test_withdraw_valid_amount(self):
        ''' Test withdrawing amount within balance (no overdraft on this type) '''
        self.account.deposit(100)
        self.account.withdraw(30)
        self.assertEqual(self.account.balance, 70)

    def test_withdraw_invalid_amount(self):
        ''' Test withdraws that should fail: invalid amount, more than balance '''
        with self.assertRaises(ValueError):
            self.account.withdraw(-1)
        with self.assertRaises(ValueError):
            self.account.withdraw(0)

        self.account.deposit(100)
        with self.assertRaises(RuntimeError):
            self.account.withdraw(150)

    def test_interest_rate(self):
        ''' test we apply the interest rate correctly '''
        self.account.deposit(100)
        self.account.interest_rate = 0.01
        self.account.apply_interest()
        self.assertAlmostEqual(self.account.balance, 101.0)


if __name__ == "__main__":
    unittest.main()
                               