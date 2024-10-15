class Account:
    def __init__(self, account_number, account_type, balance):
        
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
    
    def deposit(self, amount: float):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def deposit_int(self, amount: int):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    # Overloaded methods for withdraw
    def withdraw(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
        else:
            raise Exception("Insufficient Balance")

    def withdraw_int(self, amount: int):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
        else:
            raise Exception("Insufficient Balance")
