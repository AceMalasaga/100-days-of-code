class Account:

    def __init__(self, account_number, account_pin, account_name, account_balance):
        self.account_number = account_number
        self.account_pin = account_pin
        self.account_name = account_name
        self.account_balance = account_balance
        self.account_transaction = [f"Account opened with initial balance: ${account_balance:.2f}"]

    def __str__(self):
        return f"Account[{self.account_number}]: {self.account_pin} | Name: {self.account_name}, | Balance: ${self.account_balance:.2f}"

    def deposit(self, amount) -> bool:
        if amount <= 0:
            print("You cannot deposit negative amounts")
            return False
        self.account_balance += amount
        self.account_transaction.append(f"Deposited: {amount}")
        return True

    def withdraw(self, amount) -> bool:
        if amount <= 0:
            print("You cannot withdraw negative amounts")
            return False
        if self.account_balance >= amount:
            self.account_balance -= amount
            self.account_transaction.append(f"Withdrawn: {amount}")
            return True
        else:
            print("Not enough money")
            self.account_transaction.append(f"Not enough balance: {amount} \nNew balance: {self.account_balance:.2f}")
            return False

    def bank_statement(self):
        print("=======Bank Statement========")
        for transaction in self.account_transaction:
            print(f"Transaction: {transaction}")
        print(f"\n\nCurrent balance: {self.account_balance:.2f}")

# account = Account("1002", "5678", "Ace Malasaga", 1000)
# account.deposit(100)
# account.withdraw(1600)
# account.bank_statement()