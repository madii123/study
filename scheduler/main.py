import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI

from routes.add_task import enque_task_router
from services.intake import IntakeService
from services.lobby import LobbyService
from services.prescribe import PrescribeService
from services.review import ReviewService


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start the event loop for processing queues
    loop = asyncio.get_event_loop()

    lobby_service = LobbyService()
    intake_service = IntakeService()
    prescribe_service = PrescribeService()
    review_service = ReviewService()

    tasks = [
        loop.create_task(lobby_service.process_queue()),
        loop.create_task(intake_service.process_queue()),
        loop.create_task(review_service.process_queue()),
        loop.create_task(prescribe_service.process_queue()),
    ]

    # deliver control to the FastAPI app
    yield

    # shutdown the event loop and cancel all tasks
    for task in tasks:
        task.cancel()

    # wait for all tasks to finish
    await asyncio.gather(*tasks, return_exceptions=True)


app = FastAPI(lifespan=lifespan)
app.include_router(enque_task_router, prefix="/task")
