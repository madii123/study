from services.parking_spot import ParkingSpot


class ParkingFloor:
    def __init__(self):
        self.spots: list[ParkingSpot] = []

    def add_spot(self, spot: ParkingSpot):
        self.spots.append(spot)
