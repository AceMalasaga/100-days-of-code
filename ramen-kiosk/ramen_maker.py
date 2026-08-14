class RamenMaker:

    def __init__(self):
        self.ingredients = {
            "noodles": 15,  # portions
            "broth": 20,  # cups
            "pork": 10,  # slices
            "egg": 12,  # count
        }

    def ramen_report(self):
        print(f"Noodles: {self.ingredients['noodles']} portion"
              f"\nBroth: {self.ingredients['broth']} cups"
              f"\nPork: {self.ingredients['pork']} slices"
              f"\nEgg: {self.ingredients['egg']} count")

    def resource_sufficient(self, ramen_resource):
        is_ramen_enough = True
        for ramen in ramen_resource['ingredients']:
            if ramen_resource['ingredients'][ramen] > self.ingredients[ramen]:
                print(f"Sorry there is not enough {ramen}.")
                return False
        return is_ramen_enough

    def make_ramen(self, user_ramen):
        for item in user_ramen['ingredients']:
            self.ingredients[item] -= user_ramen['ingredients'][item]
        print(f"Here is your hot bowl of ramen. Enjoy!")
        return True


