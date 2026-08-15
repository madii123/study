from models import Step
from queues import intake_queue, prescribe_queue
from services.base import BaseService


class IntakeService(BaseService):
    def __init__(
        self,
    ):
        step = Step(
            name="intake-first-step",
            description="intake first step",
        )
        super().__init__(intake_queue, prescribe_queue, 2, step)

    async def process_queue(self):
        await super().process_queue()
