from models.coffee import Coffee


class CoffeeMaker:

    def make(
        self,
        coffee: Coffee,
    ) -> None:

        print(
            f"Preparing {coffee.coffee_type.value}..."
        )

        print(
            f"{coffee.coffee_type.value.capitalize()} "
            f"is ready."
        )