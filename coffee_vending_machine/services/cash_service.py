import threading

from enums.denomination import Denomination
from models.cash_inventory import CashInventory
from models.money import Money


class CashService:

    def __init__(
        self,
        cash_inventory: CashInventory,
    ):
        self._cash_inventory = cash_inventory
        self._lock = threading.Lock()

    def process_payment(
        self,
        payment: list[Money],
        price: int,
    ) -> list[Money]:

        payment_total = sum(
            money.get_total()
            for money in payment
        )

        if payment_total < price:
            raise ValueError(
                f"Insufficient payment. "
                f"Price: ₹{price}, "
                f"Paid: ₹{payment_total}"
            )

        change_amount = payment_total - price

        with self._lock:

            # Temporarily accept customer's money.
            for money in payment:
                self._cash_inventory.add_cash(
                    money.denomination,
                    money.quantity,
                )

            change = self._find_change(
                change_amount
            )

            if change is None:
                # Roll back customer's payment.
                for money in payment:
                    self._cash_inventory.remove_cash(
                        money.denomination,
                        money.quantity,
                    )

                raise ValueError(
                    "Unable to provide exact change"
                )

            # Remove change from machine.
            for money in change:
                self._cash_inventory.remove_cash(
                    money.denomination,
                    money.quantity,
                )

            return change

    def _find_change(
        self,
        amount: int,
    ) -> list[Money] | None:

        if amount == 0:
            return []

        remaining = amount
        change: list[Money] = []

        denominations = sorted(
            self._cash_inventory.get_all_cash(),
            key=lambda denomination: denomination.value,
            reverse=True,
        )

        for denomination in denominations:

            available = (
                self._cash_inventory.get_quantity(
                    denomination
                )
            )

            quantity = min(
                remaining // denomination.value,
                available,
            )

            if quantity > 0:
                change.append(
                    Money(
                        denomination=denomination,
                        quantity=quantity,
                    )
                )

                remaining -= (
                    denomination.value * quantity
                )

            if remaining == 0:
                break

        if remaining != 0:
            return None

        return change