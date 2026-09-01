from enums.coffee_type import CoffeeType
from models.recipe import Recipe


class Coffee:
    def __init__(
        self,
        coffee_type: CoffeeType,
        price: int,
        recipe: Recipe,
    ):
        self.coffee_type = coffee_type
        self.price = price
        self.recipe = recipe