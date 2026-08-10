from stock import MENU, resources

def resource_check(stock):
    """Check if the stock is sufficient to make a coffee"""
    #modify in accordance to Dr. Angela Yuu
    for item in stock:
        if stock[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def data_format(data):
    """Format the report data and return it"""
    #AI suggestion only the output format, the code is mine
    formatted_report = (f"Water: {data['water']}ml"
                        f"\nMilk: {data['milk']}ml"
                        f"\nCoffee: {data['coffee']}g"
                        f"\nMoney: ${data['money']}")
    return formatted_report

def process_coin():
    """Calculate the user coins and return the total"""
    print("Please insert you coin: ")

    #Here the input is AI and I change it to float
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickels?: "))
    pennies = float(input("How many pennies?: "))

    #I ask the AI of the format which is give this
    #Total Value(V)= (q*Vq) + (d*Vd) + (n*Vn) + (p*Vp)
    total = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)
    return total

def transaction(cost, user_money):
    """check the user money sufficient or there is a change and return True else False"""
    if user_money >= cost:
        #AI suggestion, the only problem with mine is income = resources['Money']
        #which is wrong
        resources['money'] += cost
        change = user_money - cost
        #AI assisted my first initial thought is elif below if user_money >=
        if change > 0:
            print(f"Here is ${change:.2f} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def coffee_machine(coffee_drink ,ingredient):
    """Update the resource after coffee created"""
    resources["water"] -= ingredient['water']
    resources['coffee'] -= ingredient["coffee"]
    if ingredient.get("milk", 0) > 0:
        resources['milk'] -= ingredient["milk"]
    return f"Here is your {coffee_drink}. Enjoy!"

machine_on = True
while machine_on:
    drink_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    #AI assisted since I created a nested if else then suggested to check the MENU
    if drink_choice in MENU:
        drink = MENU[drink_choice]['ingredients']
        chosen_drink = MENU[drink_choice]['cost']
        #AI suggest to avoid running resource_check twice so I do this
        stock_resources = resource_check(drink)
        if stock_resources:
            money_input = process_coin()
            transact = transaction(chosen_drink, money_input)
            if transact:
                coffee_make = coffee_machine(drink_choice, drink)
                print(coffee_make)
        else:
            print(stock_resources)
    elif drink_choice == "report":
        print(data_format(resources))
    elif drink_choice == "off":
        machine_on = False
    else:
        print("Sorry, that's not a valid choice.")
