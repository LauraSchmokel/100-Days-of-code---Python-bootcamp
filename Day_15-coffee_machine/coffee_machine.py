# Day 15 - Project: Coffee Machine
# Topics: match/case statements, function composition, resource management, change calculation
# What I learned: how to use match/case and organize complex logic into well-defined functions

import art
import configuration

OPTIONS = ["espresso", "latte", "cappuccino", "off", "report"]

def checkResources(answer):
    problem = ""
    if configuration.menu[answer]["ingredients"]["water"] > configuration.resources["water"]:
        problem = "water"

    elif configuration.menu[answer]["ingredients"]["milk"] > configuration.resources["milk"]:
        problem = "milk"

    elif configuration.menu[answer]["ingredients"]["coffee"] > configuration.resources["coffee"]:
        problem = "coffee"

    if problem:
        print(f"Sorry, there is not enough {problem}.")
        return False
    
    return True

def checkCoins():
    quarters = int(input("How many quarters will you insert? "))
    dimes = int(input("How many dimes will you insert? "))
    nickles = int(input("How many nickles will you insert? "))
    pennies = int(input("How many pennies will you insert? "))

    return (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

def checkValue(answer, value):
    if configuration.menu[answer]["cost"] > value:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
    elif configuration.menu[answer]["cost"] < value:
        print(f"Here is ${value - configuration.menu[answer]["cost"]} dollars in change.")
        configuration.money["value"] += configuration.menu[answer]["cost"]
        return True

    else:
        configuration.money["value"] += configuration.menu[answer]["cost"]
        return True
    
def subtractResources(answer):
    print(f"Here is your {answer}")
    configuration.resources["water"] -= configuration.menu[answer]["ingredients"]["water"]
    configuration.resources["milk"] -= configuration.menu[answer]["ingredients"]["milk"]
    configuration.resources["coffee"] -= configuration.menu[answer]["ingredients"]["coffee"]
    
print(art.logo)

answer = ""

while answer != "off":

    answer = input("What would you like? (espresso/latte/cappuccino) ")

    while answer.lower() not in OPTIONS:
        answer = input("Please, choose one of the following options: (espresso/latte/cappuccino) ")

    match answer.lower():
        case "espresso":
            if checkResources(answer):
                inserted_value = checkCoins()
                if checkValue(answer, inserted_value):
                    subtractResources(answer)

        case "latte":
            if checkResources(answer):
                inserted_value = checkCoins()
                if checkValue(answer, inserted_value):
                    subtractResources(answer)

        case "cappuccino":
            if checkResources(answer):
                inserted_value = checkCoins()
                if checkValue(answer, inserted_value):
                    subtractResources(answer)

        case "off":
            print("Turning off the coffee machine...")

        case "report":
            print(
                f"\nCurrent machine's resource values:\n\nWater: {configuration.resources["water"]}"
                f"\nMilk: {configuration.resources["milk"]}\nCoffee: {configuration.resources["coffee"]}"
                f"\nMoney: {configuration.money["value"]}"
                
                )
     