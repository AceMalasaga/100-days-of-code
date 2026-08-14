class Smoothie:

    def __init__(self):
        self.resources = {
            "banana": 10,
            "berries": 12,
            "yogurt": 15,
            "milk": 25,
            "money": 00
        }

    def report(self):
        """"""
        print(f"Banana: {self.resources['banana']} units")
        print(f"Berries: {self.resources['berries']} units")
        print(f"Yogurt: {self.resources['yogurt']} scoops")
        print(f"Milk: {self.resources['milk']} oz")

    def is_resource_sufficient(self, drink):
        is_sufficient = True
        for item in drink['ingredients']:
            if drink['ingredients'][item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return is_sufficient

    def make_coffee(self, drink_name,drink):
        for item in drink['ingredients']:
            self.resources[item] -= drink['ingredients'][item]
        print(f"Here is your {drink_name} ☕️. Enjoy!")
        return True