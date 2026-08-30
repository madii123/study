from account import Account
from card import Card


class BankService:
    def __init__(self):
        self._accounts: dict[str, Account] = {}
        self._cards: dict[str, Card] = {}

    def create_account(self, account_id: str, amount: float) -> Account:
        account = Account(account_id, amount)
        self._accounts[account_id] = account
        return account

    def create_card(self, card_id: str, pin: str) -> Card:
        card = Card(card_id, pin)
        self._cards[card_id] = card
        return card

    def authenticate(self, card: Card, pin: str) -> bool:
        return card.pin == pin

    def get_card(self, card_id: str) -> Card | None:
        return self._cards.get(card_id)

    def get_account(self, account_number: str) -> Account | None:
        return self._accounts.get(account_number)

    def get_balance(self, card: Card) -> float:
        card = self._cards[card]
        account = self._accounts[card.account_id]
        return account.balance

    def withdraw(self, card: Card, amount: float) -> bool:
        card = self._cards[card]
        account = self._accounts[card.account_id]
        return account.withdraw(amount)

    def deposit(self, card: Card, amount: float) -> None:
        card = self._cards[card]
        account = self._accounts[card.account_id]
        return account.withdraw(amount)

    def link_card_to_account(self, card: Card, account: Account) -> None:
        card.set_account_id(account.number)
        account.add_card(Card)
