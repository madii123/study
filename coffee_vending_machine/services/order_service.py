from enums.coffee_type import CoffeeType
from models.menu import Menu
from models.money import Money
from services.cash_service import CashService
from services.coffee_maker import CoffeeMaker
from services.inventory_service import InventoryService


class OrderService:

    def __init__(
        self,
        menu: Menu,
        cash_service: CashService,
        inventory_service: InventoryService,
        coffee_maker: CoffeeMaker,
    ):
        self._menu = menu
        self._cash_service = cash_service
        self._inventory_service = inventory_service
        self._coffee_maker = coffee_maker

    def place_order(
        self,
        coffee_type: CoffeeType,
        payment: list[Money],
    ) -> list[Money]:

        # 1. Find selected coffee.
        coffee = self._menu.get_item(coffee_type)

        # 2. Reserve ingredients atomically.
        self._inventory_service.consume_if_available(
            coffee.recipe
        )

        try:
            # 3. Process payment and calculate change.
            change = self._cash_service.process_payment(
                payment=payment,
                price=coffee.price,
            )

        except Exception:
            # 4. Payment failed.
            # Restore the reserved ingredients.
            self._inventory_service.restore(
                coffee.recipe
            )

            raise

        # 5. Payment succeeded.
        # Prepare and dispense coffee.
        self._coffee_maker.make(coffee)

        # 6. Return change to the caller.
        return change