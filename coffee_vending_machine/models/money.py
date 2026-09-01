from dataclasses import dataclass

from enums.denomination import Denomination


@dataclass(frozen=True)
class Money:
    denomination: Denomination
    quantity: int = 1

    def __post_init__(self):
        if self.quantity <= 0:
            raise ValueError(
                "Quantity must be positive"
            )

    def get_total(self) -> int:
        return (
            self.denomination.value
            * self.quantity
        )