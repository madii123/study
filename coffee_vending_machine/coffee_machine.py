from enums.coffee_type import CoffeeType
from factories.coffee_factory import CoffeeFactory
from models.cash_inventory import CashInventory
from models.inventory import Inventory
from models.menu import Menu
from models.money import Money
from services.cash_service import CashService
from services.coffee_maker import CoffeeMaker
from services.inventory_service import InventoryService
from services.order_service import OrderService


class CoffeeMachine:

    def __init__(
        self,
        inventory: Inventory,
        cash_inventory: CashInventory,
    ):
        self._inventory = inventory
        self._cash_inventory = cash_inventory

        # Menu
        self._menu = Menu()
        self._initialize_menu()

        # Services
        self._inventory_service = InventoryService(
            inventory
        )

        self._cash_service = CashService(
            cash_inventory
        )

        self._coffee_maker = CoffeeMaker()

        self._order_service = OrderService(
            menu=self._menu,
            cash_service=self._cash_service,
            inventory_service=self._inventory_service,
            coffee_maker=self._coffee_maker,
        )

    def _initialize_menu(self) -> None:
        for coffee_type in CoffeeType:
            coffee = CoffeeFactory.create(coffee_type)
            self._menu.add_item(coffee)

    def display_menu(self) -> None:
        self._menu.display()

    def place_order(
        self,
        coffee_type: CoffeeType,
        payment: list[Money],
    ) -> None:

        change = self._order_service.place_order(
            coffee_type=coffee_type,
            payment=payment,
        )

        print("Change:")

        for money in change:
            print(
                f"₹{money.denomination} "
                f"x {money.quantity}"
            )

    def display_inventory(self) -> None:
        stock = self._inventory_service.get_all_stock()

        print("\nCurrent inventory:")

        for ingredient, quantity in stock.items():
            print(
                f"{ingredient.value}: {quantity}"
            )

    def display_cash(self) -> None:
        cash = self._cash_inventory.get_all_cash()

        print("\nCash inventory:")

        for denomination, quantity in sorted(
            cash.items(),
            reverse=True,
        ):
            print(
                f"₹{denomination}: {quantity}"
            )