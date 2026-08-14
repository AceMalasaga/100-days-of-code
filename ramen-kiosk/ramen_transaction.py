class Transaction:

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

    def coin_process(self):
        print("Please insert coins")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost_drink):
        self.coin_process()
        if self.money_received >= cost_drink:
            change = float(self.money_received - cost_drink)
            self.profit += cost_drink
            print(f"Here is your change {change}")
            return True
        else:
            self.money_received = 0
            print(f"Not enough money")
            return False

