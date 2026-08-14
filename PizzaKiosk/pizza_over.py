class MakePizza:

    def __init__(self):
        self.inventory = {
            "dough": 10,  # dough balls
            "sauce": 15,  # scoops of sauce
            "cheese": 20,  # portions of mozzarella
            "pepperoni": 30,  # slices
            "veggies": 15,  # portions
        }

    def inventory_report(self):
        print(f"Dough: {self.inventory['dough']}"
              f"\nSauce: {self.inventory['sauce']}"
              f"\nCheese: {self.inventory['cheese']}"
              f"\nPepperoni: {self.inventory['pepperoni']}"
              f"\nVeggies: {self.inventory['veggies']}")

    def has_ingredients(self, pizza_recipe):
        for ingredient in pizza_recipe['ingredients']:
            if pizza_recipe['ingredients'][ingredient] > self.inventory[ingredient]:
                print(f"Sorry, there is not enough {ingredient} ingredient")
                return False
        return True

    def bake_pizza(self, pizza_name, pizza_recipe):
        for ingredient in pizza_recipe['ingredients']:
            self.inventory[ingredient] -= pizza_recipe['ingredients'][ingredient]
        print(f"Enjoy you {pizza_name}")
        return True