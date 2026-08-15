import asyncio

from models import QueueItem, Step


class BaseService:
    def __init__(
        self,
        current_queue: asyncio.PriorityQueue[QueueItem],
        next_queue: asyncio.PriorityQueue[QueueItem],
        capacity: int = 2,
        steps: Step = None,
    ):
        self.current_queue = current_queue
        self.next_queue = next_queue
        self.capacity = capacity
        self.steps = steps
        self.active_tasks_queue: asyncio.PriorityQueue[QueueItem] = (
            asyncio.PriorityQueue()
        )
        self.active_tasks = set()  # Track active tasks by their names

    async def process_active_tasks(self):
        while not self.active_tasks_queue.empty():
            priority, counter, task = await self.active_tasks_queue.get()
            step = task.current_step

            print(
                f"Task {task.name} started processing in {self.__class__.__name__}, steps: {step.name}"
            )
            await asyncio.sleep(5)  # Simulate processing time for the current step
            print(
                f"Task {task.name} completed processing in {self.__class__.__name__}, steps: {step.name}"
            )

            if step.next is not None:
                task.current_step = step.next
                await self.active_tasks_queue.put((priority, counter, task))
            else:
                # If there are no more steps, move the task to the next queue
                self.active_tasks.remove(task.name)  # Remove from active tasks
                if self.next_queue:
                    await self.next_queue.put((priority, counter, task))
                    print(
                        f"Task {task.name} completed processing in {self.__class__.__name__}, queued to next."
                    )
                else:
                    print(f"Task {task.name} completed")

    async def process_queue(self):
        while True:
            # Process active tasks first
            await self.process_active_tasks()

            # check if the service has a capacity limit and if the number of active tasks is less than the capacity
            if len(self.active_tasks) >= self.capacity:
                await asyncio.sleep(1)
                continue

            # pick the next task from the queue, and add it to the active tasks queue
            priority, counter, task = await self.current_queue.get()
            task.current_step = self.steps
            self.active_tasks.add(task.name)
            await self.active_tasks_queue.put((priority, counter, task))
