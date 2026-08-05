from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_machine = True
coffee_maker = CoffeeMaker() #class
money_machine = MoneyMachine()
menu = Menu()

while is_machine:
    option = menu.get_items()
    #only altered one based on the course
    choice = input(f"What would you like? {option}").lower()
    if choice == "off":
        is_machine = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report() #method
    else:
        drink = menu.find_drink(choice)
        coffee_cost = drink.cost #attribute
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(coffee_cost):
                coffee_maker.make_coffee(drink)

# My first code
# while is_machine_on:
#     coffee_drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
#     if coffee_drink == "report":
#         coffee_maker.report()
#         money_machine.report()
#     elif coffee_drink == "off":
#         is_machine_on = False
#     else:
#         if coffee_drink in menu.get_items():
#             drink_menu = menu.find_drink(coffee_drink)
#             coffee_cost = drink_menu.cost
#             if coffee_maker.is_resource_sufficient(drink_menu):
#                 if money_machine.make_payment(coffee_cost):
#                     coffee_maker.make_coffee(drink_menu)


