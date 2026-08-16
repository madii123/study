from enums import VehicleType


class Vehicle:
    def __init__(self, number: str, type: VehicleType):
        self.number = number
        self.type = type
