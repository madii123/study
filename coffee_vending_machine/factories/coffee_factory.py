from enums.coffee_type import CoffeeType
from enums.ingredient import Ingredient
from models.coffee import Coffee
from models.recipe import Recipe


class CoffeeFactory:

    @staticmethod
    def create(coffee_type: CoffeeType) -> Coffee:
        if coffee_type == CoffeeType.ESPRESSO:
            return CoffeeFactory._create_espresso()

        if coffee_type == CoffeeType.CAPPUCCINO:
            return CoffeeFactory._create_cappuccino()

        if coffee_type == CoffeeType.LATTE:
            return CoffeeFactory._create_latte()

        raise ValueError(
            f"Unsupported coffee type: {coffee_type}"
        )

    @staticmethod
    def _create_espresso() -> Coffee:
        recipe = Recipe()

        recipe.add_ingredient(
            Ingredient.COFFEE_BEANS,
            10,
        )
        recipe.add_ingredient(
            Ingredient.WATER,
            30,
        )

        return Coffee(
            coffee_type=CoffeeType.ESPRESSO,
            price=80,
            recipe=recipe,
        )

    @staticmethod
    def _create_cappuccino() -> Coffee:
        recipe = Recipe()

        recipe.add_ingredient(
            Ingredient.COFFEE_BEANS,
            10,
        )
        recipe.add_ingredient(
            Ingredient.WATER,
            30,
        )
        recipe.add_ingredient(
            Ingredient.MILK,
            100,
        )

        return Coffee(
            coffee_type=CoffeeType.CAPPUCCINO,
            price=100,
            recipe=recipe,
        )

    @staticmethod
    def _create_latte() -> Coffee:
        recipe = Recipe()

        recipe.add_ingredient(
            Ingredient.COFFEE_BEANS,
            10,
        )
        recipe.add_ingredient(
            Ingredient.WATER,
            30,
        )
        recipe.add_ingredient(
            Ingredient.MILK,
            150,
        )

        return Coffee(
            coffee_type=CoffeeType.LATTE,
            price=120,
            recipe=recipe,
        )