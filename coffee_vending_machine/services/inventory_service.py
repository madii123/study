import threading

from enums.ingredient import Ingredient
from models.inventory import Inventory
from models.recipe import Recipe


class InventoryService:
    LOW_STOCK_THRESHOLD = 10

    def __init__(self, inventory: Inventory):
        self._inventory = inventory
        self._lock = threading.Lock()

    def consume_if_available(
        self,
        recipe: Recipe,
    ) -> None:

        with self._lock:
            if not self._has_enough(recipe):
                raise ValueError(
                    "Insufficient ingredients"
                )

            for ingredient, quantity in recipe.ingredients.items():
                self._inventory.remove_stock(
                    ingredient,
                    quantity,
                )

                self._check_low_stock(ingredient)

    def restore(
        self,
        recipe: Recipe,
    ) -> None:

        with self._lock:
            for ingredient, quantity in recipe.ingredients.items():
                self._inventory.add_stock(
                    ingredient,
                    quantity,
                )

    def add_stock(
        self,
        ingredient: Ingredient,
        quantity: int,
    ) -> None:

        with self._lock:
            self._inventory.add_stock(
                ingredient,
                quantity,
            )

    def get_all_stock(self) -> dict[Ingredient, int]:
        with self._lock:
            return self._inventory.get_all_stock()

    def _has_enough(
        self,
        recipe: Recipe,
    ) -> bool:

        for ingredient, required_quantity in recipe.ingredients.items():
            available_quantity = (
                self._inventory.get_stock(ingredient)
            )

            if available_quantity < required_quantity:
                return False

        return True

    def _check_low_stock(
        self,
        ingredient: Ingredient,
    ) -> None:

        current_stock = self._inventory.get_stock(
            ingredient
        )

        if current_stock <= self.LOW_STOCK_THRESHOLD:
            print(
                f"Low stock: {ingredient.value} "
                f"has only {current_stock} remaining"
            )