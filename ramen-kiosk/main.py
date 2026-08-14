from data import resources, MENU
from ramen_maker import RamenMaker
from ramen_transaction import Transaction

ramen_maker = RamenMaker()
ramen_transaction = Transaction()

is_ramen_open = True
while is_ramen_open:
    ramen_chosen = input("What would you like? (tonkotsu, miso, shoyu) ").lower()
    if ramen_chosen in MENU:
        ramen = MENU[ramen_chosen]
        ramen_cost = MENU[ramen_chosen]['cost']
        if ramen_maker.resource_sufficient(ramen):
            if ramen_transaction.make_payment(ramen_cost):
                ramen_maker.make_ramen(ramen)
    elif ramen_chosen == "off":
        is_ramen_open = False
    elif ramen_chosen == "report":
        ramen_maker.ramen_report()
    else:
        print("Please enter a valid choice")