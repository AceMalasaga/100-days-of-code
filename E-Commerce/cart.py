class Cart:

    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return False

        if product.reduce_stock(quantity):
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity
            print(f"Added {quantity}x '{product.name}' to cart.")
            return True
        else:
            print(f"Failed to add '{product.name}'. Insufficient stock! (Available: {product.stock})")
            return False

    def remove_item(self, product, quantity):
        if product not in self.items:
            print(f"'{product.name}' is not in your cart.")
            return False

        if quantity <= 0:
            print("Quantity to remove must be greater than zero.")
            return False

        current_qty = self.items[product]
        print(current_qty)
        if quantity >= current_qty:
            product.add_stock(current_qty)
            self.items.pop(product)
            print(f"Removed: {quantity} '{product.name}' from cart.")
            return True
        elif current_qty >= quantity:
            product.add_stock(quantity)
            self.items[product] -= quantity
            print(f"Removed: {quantity} '{product.name}' from cart.")
        else:
            print(f"Failed to remove '{product.name}'. Insufficient stock!")
            return False

    def get_total(self):
        total = 0.0
        for product, qty in self.items.items():
            cost = product.price * qty
            total += cost
        return total

    #this is my code
    def view_total(self):
        total = self.get_total()
        for product, qty in self.items.items():
            print(f"{product}: \nQuantity: {qty}\nGrand Total: {total}")

    #AI
    # def view_cart(self):
    #     if not self.items:
    #         print("Your cart is currently empty.")
    #         return
    #
    #     print("\n=== YOUR CART ===")
    #     for product, qty in self.items.items():
    #         line_total = product.price * qty
    #         print(f"[{product.product_id}] {product.name} x{qty} @ ₱{product.price:,.2f} = ₱{line_total:,.2f}")
    #
    #     print("---------------------------")
    #     print(f"Grand Total: ₱{self.get_total():,.2f}\n")


# cart = Cart()
# mouse = Product("P101", "Wireless Mouse", 450.00, 10)
# keyboard = Product("P102", "Mechanical Keyboard", 2200.00, 5)
#
# cart.add_item(mouse, 5)
# cart.remove_item(mouse, 2)
# cart.get_total()
# cart.view_total()