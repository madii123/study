from enums import SpotType, VehicleType
from services.parking_floor import ParkingFloor
from services.parking_lot import ParkingLot
from services.parking_spot import ParkingSpot
from services.vehicle import Vehicle
from strategy.parking_strategy import ExactFit
from strategy.pricing_strategy import Regular

print("hello")
# lot
lot = ParkingLot(ExactFit(), Regular())

# floor
floor = ParkingFloor()
floor.add_spot(ParkingSpot(1, SpotType.BIKE))
floor.add_spot(ParkingSpot(2, SpotType.CAR))
floor.add_spot(ParkingSpot(3, SpotType.TRUCK))
lot.add_floor(floor)

car = Vehicle("KA01AB1234", VehicleType.CAR)
ticket = lot.park(car)
if ticket:
    print("Parked at:", ticket.spot.id)
    fee = lot.exit(car.number)
    print("Fee:", fee)


bike = Vehicle("KA01AB6543", VehicleType.BIKE)
ticket = lot.park(bike)
if ticket:
    print("Parked at:", ticket.spot.id)
    fee = lot.exit(bike.number)
    print("Fee:", fee)
