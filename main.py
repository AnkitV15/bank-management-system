# main.py

from bank import Bank
from utils import random_utils

def main():
    bank = Bank()

    while True:
        print("\nBank Management System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transfer")
        print("6. Transaction history")
        print("7. All Transactions")
        print("8. Delete Account")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = str(random_utils.random_num_gen(11))
            print(f"Owner account Number: {account_number}")
            owner_name = input("Enter owner name: ")
            initial_deposit = float(input("Enter initial deposit: "))
            bank.create_account(account_number, owner_name, initial_deposit)

        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            account = bank.find_account(account_number)
            if account:
                account.deposit(amount)
            else:
                print("Account not found.")

        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            account = bank.find_account(account_number)
            if account:
                account.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == "4":
            account_number = input("Enter account number: ")
            account = bank.find_account(account_number)
            if account:
                print(f"Balance: {account.get_balance()}")
            else:
                print("Account not found.")

        elif choice == "5":
            from_account_number = input("Enter from account number: ")
            to_account_number = input("Enter to account number: ")
            amount = float(input("Enter transfer amount: "))
            bank.transfer(from_account_number, to_account_number, amount)

        elif choice == "6":
            account_number = input("Enter account number: ")
            account = bank.print_transaction_history(account_number)

        elif choice == "7":
            bank.all_transaction_history()

        elif choice == "8":
            account_number = input("Enter account number: ")
            bank.delete_account(account_number)
        
        elif choice == "9":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
