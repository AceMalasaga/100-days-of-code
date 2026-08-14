class MenuItem:
    def __init__(self, name, cost, banana, berries, yogurt, milk):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "banana": banana,
            "berries": berries,
            "yogurt": yogurt,
            "milk": milk
        }
