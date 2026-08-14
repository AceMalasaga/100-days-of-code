from tkinter import Menu

from stock import MENU, resources
from smoothie_maker import Smoothie
from transaction import Transaction

smoothie_maker = Smoothie()
transaction = Transaction()

machine_on = True
while machine_on:
    smoothie = input("What would you like? (berry_boost / tropical_banana / power_smoothie): ").lower()
    if smoothie in MENU:
        drink_chosen = MENU[smoothie]
        print(f"You chose {drink_chosen}")
        cost_drink = MENU[smoothie]['cost']
        if smoothie_maker.is_resource_sufficient(drink_chosen):
            if transaction.make_payment(cost_drink):
                smoothie_maker.make_coffee(smoothie,drink_chosen)
    elif smoothie == "off":
        machine_on = False
    elif smoothie == "report":
        smoothie_maker.report()
        transaction.report()
