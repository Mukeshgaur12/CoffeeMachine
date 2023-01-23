"""THIS CODE IS FOR COFFEE MACHINE """
"""CREATED BY MUKESH GAUR"""


""""Ingredients of different coffees"""

MENU = { 
    
    "espresso": {
        
        "ingredients" : {
            "water" : 50,
            "coffee" : 18,
        },
        "cost" : 1.0,
    },

    "doppio": {
        "ingredients" : {
            "water" : 100,
            "coffee" : 36,
        },
        "cost": 2.0,
    },

    "latte": {
        "ingredients": {
            "water" : 200,
            "milk" : 150,
            "coffee" : 24,
        },
        "cost": 3.5,
    },

    "cappuccino": {
        "ingredients": {
            "water" : 250,
            "milk" : 100,
            "coffee" : 24,
        },
        "cost": 3.0,
    },

    "cortado": {
        "ingredients" : {
            "water" : 50,
            "milk" : 50,
            "coffee" : 18,
        },
        "cost": 1.5,
    },

    "red eye": {
        "ingredients" : {
            "water" : 350,
            "coffee" : 24,
        },
        "cost": 2.5,
    },

}

"""Current profit"""

profit= 0

"""Resources used"""

resources = {
    "water" : 400,
    "milk" : 200,
    "coffee" : 100,
}


def is_resource_sufficient(order_ingredients):
    """Return true when resource is sufficient else false"""
    for item in order_ingredients :
        if order_ingredients[item] >= resources[item] :
            print(f"Sorry there is enough {item}.")
            return False
    return True


def process_coins():
    """Return the total from the coin inserted"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_sucessful(money_recieved, drink_cost):
    """Return True when the payment is sucessful else false"""
    if money_recieved>=drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"here is ${change} in change.")
        global profit 
        profit += drink_cost
        return True 
    else: 
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredient from resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


is_on = True


"""Runner's Code"""


while is_on :
    choice = input("\n\n\nWhat ☕ would you like? (espresso / latte / cappuccino / doppio / cortado / red eye ):")
    if choice == "off":
        is_on = False
        """for ending the process"""

    elif choice == "report":
        print(f"Water :{resources['water']}ml")
        print(f"Milk :{resources['milk']}ml")
        print(f"Coffee :{resources['coffee']}g")
        print(f"Money :${profit}")
        """for printing report of resources & net profit"""

    else :
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_sucessful(payment,drink["cost"]):
                make_coffee(choice, drink["ingredients"])

"""End of program"""
