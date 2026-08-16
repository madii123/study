from abc import ABC, abstractmethod
from datetime import datetime

from enums import SpotType


class PricingStrategy(ABC):
    def base_fee(
        self, entry_time: datetime, exit_time: datetime, spot_type: SpotType
    ) -> int:
        duration = exit_time - entry_time
        hours = max(1, duration.total_seconds() / 3600)
        rates = {SpotType.BIKE: 20, SpotType.CAR: 30, SpotType.TRUCK: 40}
        return hours * rates[spot_type]

    @abstractmethod
    def calculate(
        self, entry_time: datetime, exit_time: datetime, spot_type: SpotType
    ) -> int:
        pass


class Regular(PricingStrategy):
    def calculate(
        self, entry_time: datetime, exit_time: datetime, spot_type: SpotType
    ) -> int:
        return super().base_fee(entry_time, exit_time, spot_type)


class Offer(PricingStrategy):
    def calculate(
        self, entry_time: datetime, exit_time: datetime, spot_type: SpotType
    ) -> int:
        return super().base_fee(entry_time, exit_time, spot_type) * 0.9


class HighDemand(PricingStrategy):
    def calculate(
        self, entry_time: datetime, exit_time: datetime, spot_type: SpotType
    ) -> int:
        return super().base_fee(entry_time, exit_time, spot_type) * 1.5
