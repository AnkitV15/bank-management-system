# bank.py

from account import Account

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, owner_name, initial_deposit=0):
        if account_number not in self.accounts:
            new_account = Account(account_number, owner_name, initial_deposit)
            self.accounts[account_number] = new_account
            print(f"Account created for {owner_name} with account number {account_number}.")
        else:
            print("Account number already exists.")

    def find_account(self, account_number):
        return self.accounts.get(account_number, None)

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)

        if from_account and to_account:
            if from_account.get_balance() >= amount:
                from_account.withdraw(amount)
                to_account.deposit(amount)
                print(
                    f"Transferred {amount} from {from_account_number} to {to_account_number}.")
            else:
                print("Insufficient balance for transfer.")
        else:
            print("One or both account numbers are invalid.")

    def print_transaction_history(self, account_number):
        account = self.find_account(account_number)
        if account:
            print(
                f"\nTransaction history for account number {account_number}:")
            transaction_history = account.get_transaction_history()
            if not transaction_history:
                print("No transactions yet.")
            else:
                for transaction in transaction_history:
                    print(transaction)
        else:
            print("Account not found.")

    def all_transaction_history(self):
        if self.accounts:

            for account_number, acc in self.accounts.items():

                print(f"Transaction for Account Name :{acc.owner_name} and Number:{account_number}")

                transaction_history = acc.get_transaction_history()

                if not transaction_history:
                    print("No transactions recorded yet!")
                else:
                    for transaction in transaction_history:
                        print(transaction)
