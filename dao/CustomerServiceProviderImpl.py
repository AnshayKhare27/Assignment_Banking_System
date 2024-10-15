import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dao.ICustomerServiceProvider import ICustomerServiceProvider
from exception.invalidAcctExcp import InvalidAccountException
from util.DBUtil import DBUtil

class CustomerServiceProviderImpl(ICustomerServiceProvider):

    def __init__(self):
        self.DBUtil = DBUtil()

    
    def get_account_balance(self, account_number: int):
        """
        Retrieve the balance of an account given its account number.
        """
        conn = self.DBUtil.getDBConn()
        cursor = conn.cursor()

        cursor.execute('SELECT balance FROM Accounts WHERE account_id=?', (account_number,))
        account = cursor.fetchone()

        if account is None:
            raise InvalidAccountException("Account not found")
        
        conn.close()
        return account[0]

    def deposit(self, account_number: int, amount: float):
        """
        Deposit the specified amount into the account.
        """
        conn = self.DBUtil.getDBConn()
        cursor = conn.cursor()

        cursor.execute('UPDATE Accounts SET balance = balance + ? WHERE account_id=?', (amount, account_number))
        conn.commit()

        cursor.execute('SELECT balance FROM Accounts WHERE account_id=?', (account_number,))
        new_balance = cursor.fetchone()[0]

        conn.close()
        return new_balance

    def withdraw(self, account_number: int, amount: float):
        """
        Withdraw the specified amount from the account.
        """
        conn = self.DBUtil.getDBConn()
        cursor = conn.cursor()

        cursor.execute('SELECT balance FROM Accounts WHERE account_id=?', (account_number,))
        account = cursor.fetchone()

        if account is None:
            raise InvalidAccountException("Account not found")

        balance = account[0]
        if balance >= amount:
            cursor.execute('UPDATE Accounts SET balance = balance - ? WHERE account_id=?', (amount, account_number))
            conn.commit()

            cursor.execute('SELECT balance FROM Accounts WHERE account_id=?', (account_number,))
            new_balance = cursor.fetchone()[0]
            conn.close()
            return new_balance
        else:
            conn.close()
            raise Exception("Insufficient Balance")

    def transfer(self, from_account: int, to_account: int, amount: float):
        """
        Transfer money from one account to another.
        """
        self.withdraw(from_account, amount)
        self.deposit(to_account, amount)

    def get_account_details(self, account_number: int):
        """
        Retrieve account and customer details for the given account number.
        """
        conn = self.DBUtil.getDBConn()
        cursor = conn.cursor()

        cursor.execute('''
            SELECT c.first_name, c.last_name, c.email, c.phone_number, a.account_type, a.balance
            FROM Customers c
            JOIN Accounts a ON c.customer_id = a.customer_id
            WHERE a.account_id=?
        ''', (account_number,))
        account_details = cursor.fetchone()

        if account_details is None:
            raise InvalidAccountException("Account not found")

        conn.close()
        return account_details
