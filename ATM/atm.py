import threading

from account import Account
from atm_state import ATMState, IdleState
from bank_service import BankService
from card import Card
from cash_dispenser import Dispenser
from note_dispenser import (
    NoteDispenser10,
    NoteDispenser20,
    NoteDispenser50,
    NoteDispenser100,
)
from operation import Operation


class ATM:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        self._bank_service = BankService()
        self._current_card: Card | None = None
        self._transaction_counter = 0

        # setup dispenser chain
        c1 = NoteDispenser100(10)
        c2 = NoteDispenser50(20)
        c3 = NoteDispenser20(40)
        c4 = NoteDispenser10(80)
        c1.next = c2
        c2.next = c3
        c3.next = c4
        c4.next = None
        self._cash_dispenser = Dispenser(c1)

        self._current_state = IdleState(self._bank_service, self._cash_dispenser)
        self._initialized = True

    @classmethod
    def get_instance(cls):
        return cls()

    @property
    def current_card(self):
        return self._current_card

    @property
    def bank_service(self):
        return self._bank_service

    def change_state(self, new_state: ATMState):
        self._current_state = new_state

    def insert_card(self, card: Card):
        self._current_state = self._current_state.insert_card(card)

    def enter_pin(self, pin: str):
        self._current_state = self._current_state.enter_pin(pin)

    def select_operation(self, operation: Operation):
        self._current_state = self._current_state.select_operation(operation)

    def eject_card(self):
        self._current_state = self._current_state.eject_card()

    def create_account(self, account_number: str, init_amount: int) -> Account:
        return self._bank_service.create_account(account_number, init_amount)

    def create_card(self, card_number: str, pin: str, account: Account) -> Card:
        card = self._bank_service.create_card(card_number, pin)
        self._bank_service.link_card_to_account(card, account)
        return Card
