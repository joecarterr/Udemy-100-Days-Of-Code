from Games.Day10.Coffees import MENU
from Games.Day10.Coffees import resources
import time

global total


def sufficient_resources():
    """Return total calculated for coins that have been inserted"""
    global total
    total = int(input("How many quarters do you have?:\n")) * 0.25
    total += int(input("How many dimes do you have?:\n")) * 0.10
    total += int(input("How many nickles do you have?:\n")) * 0.05
    total += int(input("How many cent do you have?:\n"))
    return total


global water, milk, coffee


def sufficient_materials():
    global water, milk, coffee
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]


def report():
    print("Water:", resources["water"], "ml")
    print("Milk:", resources["milk"], "ml")
    print("Coffee:", resources["coffee"], "mg")


def purchase(water_total, milk_total, coffee_total):
    global water, coffee, milk
    continue_purchase = True
    while continue_purchase:
        # user input:
        drink = input("\nWould you like to buy a espresso, latte or cappuccino?:\n").lower()

        # espresso:
        if drink == "espresso":
            sufficient_resources()
            sufficient_materials()
            if water >= MENU["espresso"]["ingredients"]["water"]:
                if coffee >= MENU["espresso"]["ingredients"]["coffee"]:
                    if total >= MENU["espresso"]["cost"]:
                        water_total -= MENU["espresso"]["ingredients"]["water"]
                        coffee_total -= MENU["espresso"]["ingredients"]["coffee"]
                        print(f"£{total}")
                        print(f"Here's your {drink}")
                    elif total < MENU[drink]["cost"]:
                        print("Insufficient funds")
                        print(f"You have been refunded £{total}")
                else:
                    print("Insufficient coffee")
            else:
                print("Insufficient water")
            if total > MENU["espresso"]["cost"]:
                change = total - MENU[drink]["cost"]
                print(f"Your change is {change}")

        # latte:
        elif drink == "latte":
            sufficient_resources()
            sufficient_materials()
            if water >= MENU["latte"]["ingredients"]["water"]:
                if milk >= MENU["latte"]["ingredients"]["milk"]:
                    if coffee >= MENU["latte"]["ingredients"]["coffee"]:
                        if total >= MENU["latte"]["cost"]:
                            water_total -= MENU["latte"]["ingredients"]["water"]
                            milk_total -= MENU["latte"]["ingredients"]["milk"]
                            coffee_total -= MENU["latte"]["ingredients"]["coffee"]
                            print(f"£{total}")
                            print(f"Here's your {drink}")
                        elif total < MENU[drink]["cost"]:
                            print("Insufficient funds")
                            print(f"You have been refunded £{total}")
                    else:
                        print("Insufficient coffee")
                else:
                    print("Insufficient milk")
            else:
                print("Insufficient water")
            if total > MENU["latte"]["cost"]:
                change = total - MENU["latte"]["cost"]
                print(f"Your change is {change}")

        # cappuccino:
        elif drink == "cappuccino":
            sufficient_resources()
            sufficient_materials()
            if water >= MENU["cappuccino"]["ingredients"]["water"]:
                if milk >= MENU["cappuccino"]["ingredients"]["water"]:
                    if coffee >= MENU["cappuccino"]["ingredients"]["coffee"]:
                        if total >= MENU["cappuccino"]["cost"]:
                            # ignore:
                            cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
                            cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
                            cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
                            # linked to above:
                            water_total -= cappuccino_water
                            milk_total -= cappuccino_milk
                            coffee_total -= cappuccino_coffee
                            print(f"£{total}")
                            print(f"Here's your {drink}")
                        elif total < MENU["cappuccino"]["cost"]:
                            print("Insufficient funds")
                            print(f"You have been refunded £{total}")
                    else:
                        print("Insufficient coffee")
                else:
                    print("Insufficient milk")
            else:
                print("Insufficient water")
            if total > MENU["cappuccino"]["cost"]:
                change = total - MENU["cappuccino"]["cost"]
                print(f"Your change is {change}")

        # user requests how much is left:
        elif drink == "report":
            report()

        # user turns off machine:
        elif drink == "off":
            print("Turning off machine...")
            time.sleep(.3)
            continue_purchase = False


purchase(milk_total=resources["milk"], water_total=resources["water"], coffee_total=resources["coffee"])
