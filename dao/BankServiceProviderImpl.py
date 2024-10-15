import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from dao.ICustomerServiceProvider import ICustomerServiceProvider
from dao.IBankServiceProvider import IBankServiceProvider
from dao.CustomerServiceProviderImpl import CustomerServiceProviderImpl
from util.DBUtil import DBUtil

class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider):
    def __init__(self, branch_name: str, branch_address: str):
        super().__init__()
        self.accountList = []  # To store the account objects
        self.branchName = branch_name
        self.branchAddress = branch_address
        self.DBUtil = DBUtil()

    def create_account(self, customer, account_number, account_type, balance):
        """
        Create a new bank account for the given customer and add it to accountList.
        """
        # We use the CustomerServiceProviderImpl to create the account in the database
        conn = self.DBUtil.getDBConn()
        cursor = conn.cursor()

        # Insert Customer
        cursor.execute('''
            INSERT INTO Customers (first_name, last_name, DOB, email, phone_number, address)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (customer.first_name, customer.last_name, customer.dob, customer.email, customer.phone_number, customer.address))
        customer_id = self.get_customer_id(cursor,customer.first_name)
        
        # Insert Account
        cursor.execute('''
            INSERT INTO Accounts (customer_id, account_type, balance)
            VALUES (?, ?, ?)
        ''', (customer_id, account_type, balance))
        account_id = self.get_account_id(cursor,customer.customer_id)

        # Add account object to accountList
        self.accountList.append({
            "account_id": account_id,
            "account_type": account_type,
            "balance": balance
        })

        conn.commit()
        conn.close()
        print(f"Account {account_number} created for {customer.first_name} {customer.last_name}")

    def list_accounts(self):
        """
        List all accounts in the bank.
        """
        if len(self.accountList) == 0:
            print("No accounts available.")
        else:
            for account in self.accountList:
                print(f"Account ID: {account['account_id']}, Type: {account['account_type']}, Balance: {account['balance']}")

    def calculate_interest(self, account_number: int):
        """
        Calculate the interest for a specific account (only for savings accounts).
        """
        account = next((acc for acc in self.accountList if acc['account_id'] == account_number), None)

        if account and account['account_type'] == 'Savings':
            interest_rate = 4.5  # Assuming a fixed interest rate
            interest = account['balance'] * (interest_rate / 100)
            print(f"Interest calculated for account {account_number}: {interest}")
            return interest
        else:
            raise Exception("Interest calculation is only applicable for savings accounts.")


    def get_customer_id(self,cursor, first_name):
    # Clear the cursor if necessary
        

        query = "SELECT customer_id FROM Customers WHERE first_name = ?"
        cursor.execute(query, (first_name,))

        customer_id = cursor.fetchone()
        if customer_id:
            return customer_id[0]
        else:
            return 1


    def get_account_id(self,cursor, customer_id):
    # Clear the cursor if necessary
        

        query = "SELECT account_id FROM Accounts WHERE customer_id = ?"
        cursor.execute(query, (customer_id,))

        account_id = cursor.fetchone()
        if account_id:
            return account_id[0]
        else:
            return 1

    