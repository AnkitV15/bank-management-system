# transaction.py

class Transaction:
    def __init__(self, transaction_type, amount, balance_after_transaction):
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance_after_transaction = balance_after_transaction

    def __str__(self):
        return f"{self.transaction_type}: ${self.amount}, Balance: ${self.balance_after_transaction}"
