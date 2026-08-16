from bank import Bank
from data import ACCOUNTS_DATA
from account import Account
class ATM:

    def __init__(self):
        self.bank = Bank(ACCOUNTS_DATA)
        self.current_account = None

    def login(self):
        acc_num = input("Enter your account number: ")
        acc_pin = input("Enter your account pin: ")

        self.current_account = self.bank.authenticate(acc_num, acc_pin)

    def logout(self):
        print("You have successfully logged out")
        self.current_account = None

    def start(self):
        is_running = True

        while is_running:
            if self.current_account == None:
                print("\n=== WELCOME TO THE ATM ===")
                print("1. Login")
                print("2. Exit")
                choice = int(input("Select choice (1-2): "))

                if choice == 1:
                    self.login()
                elif choice == 2:
                    is_running = False
                    print("Thank you for using our ATM. Goodbye!")
                else:
                    print("Invalid choice. Please try again.")
            else:
                print(f"\n=== ATM MENU ===")
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Transfer")
                print("5. Logout")
                choice = int(input("Select choice (1-5): "))

                if choice == 1:
                    self.current_account.bank_statement()
                elif choice == 2:
                    deposit = float(input("Enter deposit amount: "))
                    self.current_account.deposit(deposit)
                elif choice == 3:
                    withdraw = float(input("Enter withdraw amount: "))
                    self.current_account.withdraw(withdraw)
                elif choice == 4:
                    recipient_acc = input("Enter recipient account number: ")
                    money = float(input("Enter amount to deposit: "))
                    self.bank.transfer(self.current_account, recipient_acc, money)
                elif choice == 5:
                    self.logout()
                else:
                    print("Invalid choice. Please try again.")
