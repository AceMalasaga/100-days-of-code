from boba_maker import BobaMaker
from payment_processor import PaymentProcessor
from data import MENU

boba_maker = BobaMaker()
payment_processor = PaymentProcessor()
is_machine_on = True

while is_machine_on:
    tea_choice = input("What drink would you like? (classic_milk_tea, taro_boba, brown_sugar_latte)").lower()
    if tea_choice == "report":
        boba_maker.boba_report()
        payment_processor.profit_report()
    elif tea_choice == "off":
        is_machine_on = False
    elif tea_choice in MENU:
        recipe = MENU[tea_choice]
        tea_cost = MENU[tea_choice]["cost"]
        if boba_maker.is_resource_sufficient(recipe):
            if payment_processor.make_payment(tea_cost):
                boba_maker.make_boba(tea_choice, recipe)