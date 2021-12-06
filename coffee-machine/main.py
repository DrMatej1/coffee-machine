from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

mymm = MoneyMachine()
mycm = CoffeeMaker()
mymenu = Menu()
mycm.report()
mymm.report()

is_on = True

while is_on:
    options = mymenu.get_items()
    choice = input(f"what would you like? {options}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        mycm.report()
        mymm.report()
    else:
        drink = mymenu.find_drink(choice)
        if mycm.is_resource_sufficient(drink):
            if mymm.make_payment(drink.cost):
                mycm.make_coffee(drink)