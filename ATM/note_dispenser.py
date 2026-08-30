from dataclasses import dataclass


@dataclass
class DispensedAmount:
    success: bool
    count: int
    note_value: int


class NoteDispenser:
    def __init__(self, available_count: int):
        self.available_count = available_count
        self.next: NoteDispenser | None = None

    def dispense(self, amount: int, note: int) -> list[DispensedAmount]:
        count = amount // note
        if self.available_count >= count:
            amount_left = amount - count * note
            dispensed_amounts = []
            if self.next:
                dispensed_amounts: list[DispensedAmount] = self.next.dispense(
                    amount_left
                )
            if not dispensed_amounts or dispensed_amounts[0].success:
                curr = [DispensedAmount(True, count, note)]
                self.available_count -= count
                if dispensed_amounts and dispensed_amounts[0].success:
                    curr.extend(dispensed_amounts)
                return curr
        return [DispensedAmount(success=False, count=0, note_value=note)]


class NoteDispenser100(NoteDispenser):
    def __init__(self, available_count: int):
        super().__init__(available_count)

    def dispense(self, amount: int) -> list[DispensedAmount]:
        return super().dispense(amount, 100)


class NoteDispenser50(NoteDispenser):
    def __init__(self, available_count: int):
        super().__init__(available_count)

    def dispense(self, amount: int) -> list[DispensedAmount]:
        return super().dispense(amount, 50)


class NoteDispenser20(NoteDispenser):
    def __init__(self, available_count: int):
        super().__init__(available_count)

    def dispense(self, amount: int) -> list[DispensedAmount]:
        return super().dispense(amount, 20)


class NoteDispenser10(NoteDispenser):
    def __init__(self, available_count: int):
        super().__init__(available_count)

    def dispense(self, amount: int) -> list[DispensedAmount]:
        return super().dispense(amount, 10)
