from collections import defaultdict

from enums.denomination import Denomination


class CashInventory:

    def __init__(self):
        self._cash: dict[Denomination, int] = defaultdict(int)

    def add_cash(
        self,
        denomination: Denomination,
        quantity: int = 1,
    ) -> None:

        self._cash[denomination] += quantity

    def remove_cash(
        self,
        denomination: Denomination,
        quantity: int = 1,
    ) -> None:

        if self._cash[denomination] < quantity:
            raise ValueError(
                f"Insufficient cash for "
                f"₹{denomination.value}"
            )

        self._cash[denomination] -= quantity

    def get_quantity(
        self,
        denomination: Denomination,
    ) -> int:

        return self._cash[denomination]

    def get_all_cash(self) -> dict[Denomination, int]:

        return dict(self._cash)

    def get_total(self) -> int:

        return sum(
            denomination.value * quantity
            for denomination, quantity
            in self._cash.items()
        )