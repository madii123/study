from abc import ABC, abstractmethod

from enums import SpotType, VehicleType


class ParkingStrategy(ABC):
    @abstractmethod
    def allowed_types(self, vehicle_type: VehicleType) -> list[SpotType]:
        pass


class LooseFit(ParkingStrategy):
    def allowed_types(self, vehicle_type: VehicleType) -> list[SpotType]:
        allowed = {
            VehicleType.BIKE: {
                SpotType.BIKE,
                SpotType.CAR,
                SpotType.TRUCK,
            },
            VehicleType.CAR: {
                SpotType.CAR,
                SpotType.TRUCK,
            },
            VehicleType.TRUCK: {
                SpotType.TRUCK,
            },
        }
        return allowed[vehicle_type]


class ExactFit(ParkingStrategy):
    def allowed_types(self, vehicle_type: VehicleType) -> list[SpotType]:
        return [vehicle_type]
