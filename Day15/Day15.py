# COFFEE MACHINE PROGRAM

from data import MENU
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    print("Please input coins.")
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.10
    total += int(input("How many nickles?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Total cost: ${drink_cost}")
        print(f"Your payment: ${money_received}")
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):\n")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drinks = MENU[choice]
        if is_resource_sufficient(drinks["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drinks["cost"]):
                make_coffee(choice, drinks["ingredients"])
