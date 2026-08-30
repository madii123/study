from abc import ABC, abstractmethod

from note_dispenser import DispensedAmount, NoteDispenser


class CashDispenser(ABC):
    def __init__(self, note_dispenser: NoteDispenser):
        self._note_dispenser: NoteDispenser = note_dispenser

    @abstractmethod
    def dispense(amount: int):
        pass


class Dispenser(CashDispenser):
    def __init__(self, note_dispenser: NoteDispenser):
        self._note_dispenser: NoteDispenser = note_dispenser

    def dispense(self, amount: int) -> bool:
        dispensed_amount: list[DispensedAmount] = self._note_dispenser.dispense(amount)
        if dispensed_amount[0].success:
            print(dispensed_amount)
            return True
        else:
            print("failed to dispense")
            return False
