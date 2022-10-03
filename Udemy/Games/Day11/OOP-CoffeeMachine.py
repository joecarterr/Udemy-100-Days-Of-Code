from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_machine_on = True

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

while is_machine_on:
    options = menu.get_items()
    choice = input(f"\nWould you like {options}?:\n").lower()
    if choice == "off":
        is_machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        else:
            money_machine.make_payment(drink.cost)
