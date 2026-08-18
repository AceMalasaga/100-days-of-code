class Product:

    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def display_info(self):
        """Display information about the product"""
        print(
            f"Product ID: [{self.product_id}]\n"
            f"Name: {self.name}\n"
            f"Price: ₱{self.price:,.2f}\n"
            f"Stock: {self.stock}\n"
        )
    def reduce_stock(self, quantity):
        if quantity <= 0:
            print("Not enough stock")
            return False
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        else:
            print("Not enough stock")
            return False

    def add_stock(self, quantity):
        if quantity <= 0:
            print("Not enough stock")
        self.stock += quantity

    def __str__(self):
        return f"Product ID: {self.product_id}, \nName: {self.name}, \nPrice: {self.price:,.2f}, \nStock: {self.stock}"


# product = Product(1, name="Mechanical Keyboard", price=10, stock=5)
# product.display_info()
# product.reduce_stock(5)
# product.add_stock(5)
# product.display_info()