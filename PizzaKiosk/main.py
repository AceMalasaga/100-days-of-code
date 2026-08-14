from data import MENU
from pizza_over import MakePizza
from transaction import PaymentTerminal

make_pizza = MakePizza()
payment_terminal = PaymentTerminal()
is_kiosk_open = True

while is_kiosk_open:
    chosen_pizza = input("What pizza would you like? (margherita/pepperoni/veggie_supreme): ")
    if chosen_pizza in MENU:
        pizza_ingredient = MENU[chosen_pizza]
        pizza_cost = MENU[chosen_pizza]["cost"]
        pizza_name = chosen_pizza
        if make_pizza.has_ingredients(pizza_ingredient):
            if payment_terminal.make_payment(pizza_cost):
                make_pizza.bake_pizza(pizza_name,pizza_ingredient)
    elif chosen_pizza == "off":
        is_kiosk_open = False
    elif chosen_pizza == "report":
        make_pizza.inventory_report()
        payment_terminal.transaction_report()
    else:
        print("Not a valid choice")