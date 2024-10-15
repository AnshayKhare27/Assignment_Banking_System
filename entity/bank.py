import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from entity.account import Account
from entity.customer import Customer
from util.DBUtil import DBUtil
from dao.BankServiceProviderImpl import BankServiceProviderImpl
from exception.invalidAcctExcp import InvalidAccountException

class Bank:
    def __init__(self):
        self.service_provider = BankServiceProviderImpl()

    def create_account(self, customer, account_type, initial_balance):
        """
        Creates a new bank account for the given customer.
        """
        account_id = self.service_provider.create_account(customer, account_type, initial_balance)
        print(f"Account created successfully with Account ID: {account_id}")
    
    def get_account_balance(self, account_number):
        """
        Retrieves the balance of a specific account.
        """
        try:
            account = self.service_provider.get_account_details(account_number)
            print(f"Account Balance: {account['balance']}")
        except InvalidAccountException as e:
            print(e)
    
    def deposit(self, account_number, amount):
        """
        Deposit a specific amount into an account.
        """
        try:
            self.service_provider.deposit(account_number, amount)
            print(f"Deposited {amount} successfully.")
        except InvalidAccountException as e:
            print(e)

    def withdraw(self, account_number, amount):
        """
        Withdraw a specific amount from an account.
        """
        try:
            self.service_provider.withdraw(account_number, amount)
            print(f"Withdrew {amount} successfully.")
        except Exception as e:
            print(e)

    def transfer(self, from_account, to_account, amount):
        """
        Transfer funds from one account to another.
        """
        try:
            # Withdraw from the source account
            self.withdraw(from_account, amount)
            # Deposit into the target account
            self.deposit(to_account, amount)
            print(f"Transferred {amount} from account {from_account} to account {to_account}.")
        except Exception as e:
            print(e)

    def get_account_details(self, account_number):
        """
        Retrieves and prints details of a specific account.
        """
        try:
            account = self.service_provider.get_account_details(account_number)
            print(f"Account Details: {account}")
        except InvalidAccountException as e:
            print(e)
