from abc import ABC


class Operation(ABC):
    def __init__(self):
        pass


class CheckBalance(Operation):
    def __init__(self):
        pass


class WithdrawCash(Operation):
    def __init__(self, amount: float):
        self.amount = amount


class DepositCash(Operation):
    def __init__(self, amount: float):
        self.amount = amount
