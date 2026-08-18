from data import CATALOG_DATA
from product import Product
from cart import Cart
class Store:

    def __init__(self, raw_data):
        self.catalog = {}
        for prod_id, info in raw_data.items():
            self.catalog[prod_id] = Product(prod_id, info['name'], info['price'], info['stock'])
        # print(self.catalog['P101'].name)

    def display_products(self):
        print("=== STORE CATALOG ===")
        for item in self.catalog.values():
            item.display_info()

    def get_product(self, prod_id):
        clean_id = prod_id.strip().upper()
        if self.catalog.get(clean_id):
            return self.catalog[clean_id]
        else:
            return None

    # def checkout(self, cart, payment_amount):
    #     if not cart.items:
    #         print("The cart is empty")
    #         return False
    #     total = cart.get_total()
    #     if payment_amount < total:
    #         print("The amount is not enough")
    #         return False
    #     else:
    #         change = payment_amount - total
    def checkout(self, cart, payment_amount):
        if not cart.items:
            print("Cannot checkout: Cart is empty.")
            return False

        total = cart.get_total()
        payment_amount = float(payment_amount)

        if payment_amount < total:
            print(f"Payment insufficient! Needed: ₱{total:,.2f}, Paid: ₱{payment_amount:,.2f}")
            return False

        change = payment_amount - total
        print("\n=== OFFICIAL RECEIPT ===")
        for product, qty in cart.items.items():
            print(f"{product.name} x{qty} - ₱{product.price * qty:,.2f}")
        print("------------------------")
        print(f"Total:   ₱{total:,.2f}")
        print(f"Payment: ₱{payment_amount:,.2f}")
        print(f"Change:  ₱{change:,.2f}")
        print("========================\n")

        cart.items.clear()
        return True


# store = Store(CATALOG_DATA)
# store.display_products()
# store.get_product('p101')
# user_cart = Cart()
