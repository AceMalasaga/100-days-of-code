class PaymentProcessor:
    CURRENCY = "₱"

    PESO = {
        "Piso": 1,
        "Singko": 5,
        "Diyes": 10,
        "Bente": 20
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def profit_report(self):
        print(f"Money: {self.profit}")

    def process_cash(self):
        print("Please Insert Money")

        for coin in self.PESO:
            self.money_received += int(input(f"How many {coin}?: ")) * self.PESO[coin]
        return self.money_received

    def make_payment(self,cost):
        self.process_cash()

        if self.money_received >= cost:
            change = self.money_received - cost
            self.profit += cost
            self.money_received = 0
            print(f"Payment Successful! Here is your {change}")
            return True
        else:
            print(f"Not enough money! Refunded {self.money_received}")
            return False