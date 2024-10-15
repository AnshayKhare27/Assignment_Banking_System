import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from entity.account import Account

class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 1000  # Assuming $1000 overdraft limit for current accounts

    def __init__(self, account_number, balance):
        super().__init__(account_number, "Current", balance)

    def withdraw(self, amount):
        if self.balance - amount >= -self.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
        else:
            raise Exception(f"Overdraft limit exceeded! Cannot withdraw {amount}.")
