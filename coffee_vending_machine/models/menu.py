from enums.coffee_type import CoffeeType
from models.coffee import Coffee


class Menu:
    def __init__(self):
        self._items: dict[CoffeeType, Coffee] = {}

    def add_item(self, coffee: Coffee) -> None:
        self._items[coffee.coffee_type] = coffee

    def get_item(self, coffee_type: CoffeeType) -> Coffee:
        coffee = self._items.get(coffee_type)

        if coffee is None:
            raise ValueError(
                f"{coffee_type.value} is not available"
            )

        return coffee

    def get_all_items(self) -> list[Coffee]:
        return list(self._items.values())

    def display(self) -> None:
        print("Available coffees:")

        for coffee in self._items.values():
            print(
                f"{coffee.coffee_type.value.capitalize()} "
                f"- ₹{coffee.price}"
            )