from account import Account
from data import ACCOUNTS_DATA

class Bank:

    def __init__(self, raw_data):
        self.accounts = {}
        #Create an object on each account acc_num for the key and info for the value pair
        for acc_num, info in raw_data.items():
            #stored it in self.account format (self.account["1001"]: <account. Account object>)
            self.accounts[acc_num] = Account(acc_num, info["pin"], info["name"], info["balance"])
        # print(self.accounts)

    def authenticate(self, account_number, pin):
        """Authenticate an Account and return an Account"""
        #if account_number is in accounts and account_pin is equal to pin if True print and return True
        if account_number in self.accounts and self.accounts[account_number].account_pin == pin:
            print(f"Welcome, {self.accounts[account_number].account_name}!")
            return self.accounts[account_number]
        else:
            print("Invalid Account Number or PIN.")
            return None

    def transfer(self, sender_account, recipient_acc_num, amount):
        """Transfer an Account from one Account to another"""
        if recipient_acc_num not in self.accounts:
            print("Recipient account not found.")
            return False
        recipient_account = self.accounts[recipient_acc_num]
        if sender_account.withdraw(amount):
            if recipient_account.deposit(amount):
                print(f"Transferred ₱{amount:.2f} to {recipient_account.account_name}")
                return True


# bank = Bank(ACCOUNTS_DATA)
# current_account = bank.authenticate("1002", "5678")
# bank.transfer(current_account, "1001", 200)
# current_account.bank_statement()