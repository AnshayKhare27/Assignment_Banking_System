import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from entity.account import Account

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate=4.5):
        super().__init__(account_number, "Savings", balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * (self.interest_rate / 100)
