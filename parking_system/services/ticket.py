from datetime import datetime, timezone

from services.parking_spot import ParkingSpot
from services.vehicle import Vehicle


class Ticket:
    def __init__(self, vehicle: Vehicle, spot: ParkingSpot):
        self.vehicle: Vehicle = vehicle
        self.spot: ParkingSpot = spot
        self.entry_time: datetime = datetime.now(timezone.utc)
        self.exit_time: datetime = None
