class BobaMaker:

    def __init__(self):
        self.ingredients = {
            "tea": 30,  # ounces of brewed tea
            "tapioca_pearls": 20,  # scoops of boba pearls
            "milk": 25,  # ounces of milk
            "syrup": 15,  # shots of sugar syrup
        }

    def boba_report(self):
        print(f"Tea: {self.ingredients['tea']} ounces of brewed tea"
              f"\nTapioca Pearls: {self.ingredients['tapioca_pearls']} scoops of boba pearls"
              f"\nMilk: {self.ingredients['milk']} ounces of milk"
              f"\nSyrup: {self.ingredients['syrup']} shots of sugar syrup")

    def is_resource_sufficient(self, drink_recipe):
        is_resource_sufficient = True
        for ingredient in drink_recipe["ingredients"]:
            if drink_recipe["ingredients"][ingredient] > self.ingredients[ingredient]:
                print(f"{ingredient} is not sufficient")
                return False
        return is_resource_sufficient

    def make_boba(self, drink_name, drink_ingredients):
        ingredients = drink_ingredients["ingredients"]
        for ingredient in ingredients:
            self.ingredients[ingredient] -= ingredients[ingredient]
        print(f"Enjoy you {drink_name}, and have a nice day!")