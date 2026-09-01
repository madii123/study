from coffee_machine import CoffeeMachine
from enums.coffee_type import CoffeeType
from enums.denomination import Denomination
from enums.ingredient import Ingredient
from models.cash_inventory import CashInventory
from models.inventory import Inventory
from models.money import Money


def main():
    # Initialize ingredient inventory
    inventory = Inventory()

    inventory.add_stock(
        Ingredient.COFFEE_BEANS,
        50,
    )
    inventory.add_stock(
        Ingredient.WATER,
        500,
    )
    inventory.add_stock(
        Ingredient.MILK,
        200,
    )
    inventory.add_stock(
        Ingredient.SUGAR,
        100,
    )

    # Initialize cash inventory
    cash_inventory = CashInventory()

    cash_inventory.add_cash(
        Denomination.TEN,
        5,
    )
    cash_inventory.add_cash(
        Denomination.TWENTY,
        5,
    )
    cash_inventory.add_cash(
        Denomination.FIFTY,
        5,
    )
    cash_inventory.add_cash(
        Denomination.HUNDRED,
        2,
    )

    # Initialize coffee machine
    machine = CoffeeMachine(
        inventory=inventory,
        cash_inventory=cash_inventory,
    )

    # Display menu
    machine.display_menu()

    # Display initial cash
    machine.display_cash()

    # Customer pays ₹150
    payment = [
        Money(Denomination.HUNDRED),
        Money(Denomination.FIFTY),
    ]

    # Buy cappuccino for ₹100
    machine.place_order(
        coffee_type=CoffeeType.CAPPUCCINO,
        payment=payment,
    )

    # Display remaining ingredient inventory
    machine.display_inventory()

    # Display remaining cash
    machine.display_cash()


if __name__ == "__main__":
    main()