import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from entity.customer import Customer
from entity.bank import Bank
from dao.ICustomerServiceProvider import ICustomerServiceProvider
from dao.IBankServiceProvider import IBankServiceProvider
from dao.CustomerServiceProviderImpl import CustomerServiceProviderImpl
from dao.BankServiceProviderImpl import BankServiceProviderImpl
from util.DBUtil import DBUtil

def main():
    bank_service = BankServiceProviderImpl(branch_name="SBI Main Branch", branch_address="BHOPAL")

    while True:
        print("\n--- Banking System Menu ---")
        print(f"Branch: {bank_service.branchName}, Address: {bank_service.branchAddress}")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Get Account Balance")
        print("6. Get Account Details")
        print("7. List All Accounts")
        print("8. Calculate Interest (Savings Accounts Only)")
        print("9. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            dob = input("Enter date of birth (YYYY-MM-DD): ")
            email = input("Enter email: ")
            phone_number = input("Enter phone number: ")
            address = input("Enter address: ")
            customer = Customer(first_name, last_name, dob, email, phone_number, address)
            
            account_type = input("Enter account type (savings/current/zero-balance): ")
            balance = float(input("Enter initial balance: "))
            account_number = len(bank_service.accountList) + 1001  # Generate account number
            bank_service.create_account(customer, account_number, account_type, balance)
        
        elif choice == 2:
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to deposit: "))
            bank_service.deposit(account_number, amount)
        
        elif choice == 3:
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to withdraw: "))
            bank_service.withdraw(account_number, amount)
        
        elif choice == 4:
            from_account = int(input("Enter from account number: "))
            to_account = int(input("Enter to account number: "))
            amount = float(input("Enter amount to transfer: "))
            bank_service.transfer(from_account, to_account, amount)
        
        elif choice == 5:
            account_number = int(input("Enter account number: "))
            bank_service.get_account_balance(account_number)

        elif choice == 6:
            account_number = int(input("Enter account number: "))
            bank_service.get_account_details(account_number)

        elif choice == 7:
            bank_service.list_accounts()

        elif choice == 8:
            account_number = int(input("Enter account number: "))
            bank_service.calculate_interest(account_number)
        
        elif choice == 9:
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
