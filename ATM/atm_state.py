from abc import ABC, abstractmethod

from bank_service import BankService
from card import Card
from cash_dispenser import CashDispenser
from exceptions import (
    CardAlreadyExistException,
    CardDoesNotExistException,
    InsertPinException,
    InvalidCardException,
    InvalidPinException,
    OperationNotSupportedException,
    PinAlreadyInsertedException,
)
from operation import CheckBalance, DepositCash, Operation, WithdrawCash


class ATMState(ABC):
    @abstractmethod
    def insert_card(self, card_number: str) -> "ATMState":
        pass

    @abstractmethod
    def enter_pin(self, pin: str) -> "ATMState":
        pass

    @abstractmethod
    def select_operation(self, op: Operation) -> "ATMState":
        pass

    @abstractmethod
    def eject_card(self) -> "ATMState":
        pass


class IdleState(ATMState):
    def __init__(self, bank_service: BankService, cash_dispenser: CashDispenser):
        self._bank_service = bank_service
        self._cash_dispenser = cash_dispenser

    def insert_card(self, card_number: str) -> "ATMState":
        if card_number not in self._bank_service._cards:
            raise InvalidCardException()
        card = self._bank_service._cards[card_number]
        return HasCardState(self._bank_service, card, self._cash_dispenser)

    def enter_pin(self, pin: str) -> "ATMState":
        raise CardDoesNotExistException()

    def select_operation(self, op: Operation) -> "ATMState":
        raise CardDoesNotExistException()

    def eject_card(self) -> "ATMState":
        raise CardDoesNotExistException()


class HasCardState(ATMState):
    def __init__(
        self, bank_service: BankService, card: Card, cash_dispenser: CashDispenser
    ):
        self._bank_service = bank_service
        self._card = card
        self._cash_dispenser = cash_dispenser

    def insert_card(self, card_number: str) -> "ATMState":
        raise CardAlreadyExistException()

    def enter_pin(self, pin: str) -> "ATMState":
        if self._card.pin == pin:
            return HasAuthenticatedState(
                self._bank_service, self._card, self._cash_dispenser
            )
        raise InvalidPinException()

    def select_operation(self, op: Operation) -> "ATMState":
        raise InsertPinException()

    def eject_card(self) -> "ATMState":
        print("card removed")
        return IdleState(self._bank_service)


class HasAuthenticatedState(ATMState):
    def __init__(
        self, bank_service: BankService, card: Card, cash_dispenser: CashDispenser
    ):
        self._bank_service = bank_service
        self._card = card
        self._cash_dispenser = cash_dispenser

    def insert_card(self, card_number: str) -> "ATMState":
        raise CardAlreadyExistException()

    def enter_pin(self, pin: str) -> "ATMState":
        raise PinAlreadyInsertedException()

    def select_operation(self, op: Operation) -> "ATMState":
        account = self._bank_service.get_account(self._card.account_id)
        if not account:
            raise InvalidCardException()
        if isinstance(op, CheckBalance):
            print(f"show balance: {account.balance}")
        elif isinstance(op, DepositCash):
            account.deposit(op.amount)
        elif isinstance(op, WithdrawCash):
            account.withdraw(op.amount)
            self._cash_dispenser.dispense(op.amount)
        else:
            raise OperationNotSupportedException()
        return self

    def eject_card(self) -> "ATMState":
        print("card removed")
        return IdleState(self._bank_service, self._cash_dispenser)
