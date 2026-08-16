from datetime import datetime, timezone
from threading import Lock

from enums import SpotType
from services.parking_floor import ParkingFloor
from services.parking_spot import ParkingSpot
from services.ticket import Ticket
from services.vehicle import Vehicle
from strategy.parking_strategy import ParkingStrategy
from strategy.pricing_strategy import PricingStrategy


class ParkingLot:
    def __init__(
        self, parking_strategy: ParkingStrategy, pricing_strategy: PricingStrategy
    ):
        self.floors: list[ParkingFloor] = []
        self.parking_strategy: ParkingStrategy = parking_strategy
        self.pricing_strategy: PricingStrategy = pricing_strategy
        self.lock = Lock()
        self.available_spots = {
            SpotType.BIKE: set(),
            SpotType.CAR: set(),
            SpotType.TRUCK: set(),
        }
        self.active_tickets: dict[str, Ticket] = {}

    def add_floor(self, floor: ParkingFloor):
        self.floors.append(floor)
        for spot in floor.spots:
            self.available_spots[spot.type].add(spot)

    def find_spot(self, vehicle: Vehicle) -> ParkingSpot | None:
        allowed = self.parking_strategy.allowed_types(vehicle.type)
        for spot_type in allowed:
            spots = self.available_spots[spot_type]
            if spots:
                return next(iter(spots))
        return None

    def park(self, vehicle: Vehicle) -> Ticket | None:
        with self.lock:
            spot = self.find_spot(vehicle)
            if spot is None:
                return None
            spot.vehicle = vehicle
            self.available_spots[spot.type].remove(spot)
            ticket = Ticket(vehicle, spot)
            self.active_tickets[vehicle.number] = ticket
            return ticket

    def exit(self, vehicle_number: str):
        with self.lock:
            ticket = self.active_tickets[vehicle_number]
            del self.active_tickets[vehicle_number]
            spot = ticket.spot
            spot.vehicle = None
            self.available_spots[spot.type].add(spot)

            ticket.exit_time = datetime.now(timezone.utc)

            fee = self.pricing_strategy.calculate(
                ticket.entry_time, ticket.exit_time, spot.type
            )

            return fee
