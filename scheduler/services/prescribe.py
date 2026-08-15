from models import Step
from queues import prescribe_queue, review_queue
from services.base import BaseService


class PrescribeService(BaseService):
    def __init__(
        self,
    ):
        step1 = Step(
            name="prescribe-first-step",
            description="prescribe first step",
        )
        step2 = Step(name="prescribe-second-step", description="prescribe second step")
        step1.next = step2

        super().__init__(prescribe_queue, review_queue, 2, step1)

    async def process_queue(self):
        await super().process_queue()
