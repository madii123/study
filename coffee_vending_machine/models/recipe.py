from enums.ingredient import Ingredient


class Recipe:
    def __init__(self):
        self.ingredients: dict[Ingredient, int] = {}

    def add_ingredient(
        self,
        ingredient: Ingredient,
        quantity: int,
    ) -> None:
        self.ingredients[ingredient] = quantity