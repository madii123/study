from models import Step
from queues import intake_queue, lobby_queue
from services.base import BaseService


class LobbyService(BaseService):
    def __init__(self):
        step = Step(
            name="lobby-first-step",
            description="lobby first step",
        )
        super().__init__(lobby_queue, intake_queue, 10000, step)

    async def process_queue(self):
        await super().process_queue()
