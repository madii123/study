import threading

from card import Card


class Account:
    def __init__(self, account_number: str, balance: float):
        self._account_number = account_number
        self._balance = balance
        self._cards: dict[str, Card] = {}
        self._lock = threading.Lock()

    @property
    def number(self) -> dict:
        return self._account_number

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def cards(self) -> dict:
        return self._cards

    def add_card(self, card: Card) -> None:
        self._cards[card.number] = Card

    def deposit(self, amount: int) -> None:
        with self._lock:
            self._balance += amount

    def withdraw(self, amount) -> bool:
        with self._lock:
            if amount <= self._balance:
                self._balance -= amount
                return True
            return False
