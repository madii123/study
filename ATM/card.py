class Card:
    def __init__(self, card_number: str, pin: str):
        self._card_number = card_number
        self._pin = pin
        self._account_id = None

    @property
    def account_id(self) -> str | None:
        return self._account_id

    @property
    def number(self) -> str:
        return self._card_number

    @property
    def pin(self) -> str:
        return self._pin

    def set_account_id(self, account_id) -> str:
        self._account_id = account_id
