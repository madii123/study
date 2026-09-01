from enums.ingredient import Ingredient


class Inventory:
    def __init__(self):
        self._stock: dict[Ingredient, int] = {}

    def add_stock(
        self,
        ingredient: Ingredient,
        quantity: int,
    ) -> None:
        self._stock[ingredient] = (
            self._stock.get(ingredient, 0) + quantity
        )

    def remove_stock(
        self,
        ingredient: Ingredient,
        quantity: int,
    ) -> None:
        current_stock = self._stock.get(ingredient, 0)

        if current_stock < quantity:
            raise ValueError(
                f"Insufficient stock for {ingredient.value}"
            )

        self._stock[ingredient] = current_stock - quantity

    def get_stock(
        self,
        ingredient: Ingredient,
    ) -> int:
        return self._stock.get(ingredient, 0)

    def get_all_stock(self) -> dict[Ingredient, int]:
        return self._stock.copy()