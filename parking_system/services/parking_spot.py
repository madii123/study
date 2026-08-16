from enums import SpotType


class ParkingSpot:
    def __init__(self, id: int, type: SpotType):
        self.id = id
        self.type = type
        self.vehicle = None
