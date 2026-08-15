import asyncio

from models import QueueItem

lobby_queue: asyncio.PriorityQueue[QueueItem] = asyncio.PriorityQueue()
intake_queue: asyncio.PriorityQueue[QueueItem] = asyncio.PriorityQueue()
prescribe_queue: asyncio.PriorityQueue[QueueItem] = asyncio.PriorityQueue()
review_queue: asyncio.PriorityQueue[QueueItem] = asyncio.PriorityQueue()
