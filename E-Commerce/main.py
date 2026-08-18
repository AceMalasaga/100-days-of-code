from data import CATALOG_DATA
from store import Store
from cart import Cart


def main():
    store = Store(CATALOG_DATA)
    cart = Cart()

    while True:
        print("=== TECH SHOP KIOSK ===")
        print("1. View Products")
        print("2. Add Item to Cart")
        print("3. Remove Item from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            store.display_products()

        elif choice == "2":
            prod_id = input("Enter Product ID: ")
            product = store.get_product(prod_id)
            if product:
                try:
                    qty = int(input(f"Enter quantity for {product.name}: "))
                    cart.add_item(product, qty)
                except ValueError:
                    print("Invalid quantity input.")
            else:
                print("Product ID not found.")

        elif choice == "3":
            prod_id = input("Enter Product ID to remove: ")
            product = store.get_product(prod_id)
            if product:
                try:
                    qty = int(input(f"Enter quantity to remove: "))
                    cart.remove_item(product, qty)
                except ValueError:
                    print("Invalid quantity input.")
            else:
                print("Product ID not found.")

        elif choice == "4":
            cart.view_total()

        elif choice == "5":
            if not cart.items:
                print("Your cart is empty.")
                continue

            print(f"Total Due: ₱{cart.get_total():,.2f}")
            try:
                payment = float(input("Enter payment amount: ₱"))
                store.checkout(cart, payment)
            except ValueError:
                print("Invalid payment input.")

        elif choice == "6":
            print("Thank you for shopping!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()