# account.py

from transaction import Transaction

class Account:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        print(f"Deposited {self.balance}. New balance: {self.balance}")
        self.transaction_history = []
        self.transaction_history.append(Transaction("Deposit", self.balance, self.balance))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(Transaction("Deposit", amount, self.balance))
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(Transaction("Withdraw", amount, self.balance))
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history
