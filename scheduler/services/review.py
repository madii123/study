from queues import review_queue
from services.base import BaseService, Step


class ReviewService(BaseService):
    def __init__(
        self,
    ):
        step = Step(name="review-second-step", description="review second step")
        super().__init__(review_queue, None, 2, step)

    async def process_queue(self):
        await super().process_queue()
