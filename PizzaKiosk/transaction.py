class PaymentTerminal:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0.0
        self.money_received = 0.0

    def transaction_report(self):
        print(f"Profit: {self.profit}")

    def process_cash(self):
        print("Please insert you coin")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        self.process_cash()
        if self.money_received > cost:
            change = round(self.money_received - cost, 2)
            self.profit += cost
            print(f"Here is your change: {change}")
            return True
        else:
            print(f"Not enough money")
            return False


