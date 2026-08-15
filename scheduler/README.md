# Scheduler

This small `scheduler` package models a simple pipeline of tasks and steps used for simulation and experimentation.

## Overview

When a request arrives at the backend it is turned into a task and enqueued. The simplified flow used by this project is:

- `add_task.py` (backend entrypoint) receives a call and creates a new task
- The task is first enqueued into the **lobby service** (capacity: 10,000; 1 step)
- After the lobby, the task proceeds through the main pipeline:
	- `intake` (1 step, capacity: 2)
	- `prescribe` (2 steps: `look`, `prescribe`, capacity: 2)
	- `review` (1 step, capacity: 2)
- After `review` the task is complete

All pipeline stages after the lobby (`intake`, `prescribe`, `review`) are limited to a capacity of `2` for simulation purposes.

## Simulation details

- Each step in a task includes an artificial delay to simulate processing time; adjust delays in code to test throughput and contention.
- The lobby service represents a high-capacity queue (10k) with effectively no processing constraint other than moving tasks into the pipeline.
- The capacity value indicates the maximum concurrent tasks that stage can process in the simulation.

## Example flow (pseudo)

1. `add_task.py` receives an incoming request and builds a task object with metadata.
2. It enqueues the task into `lobby` (capacity 10000).
3. Lobby immediately enqueues into `intake` when capacity and order permits.
4. `intake` processes the single step (with configured delay), then forwards to `prescribe`.
5. `prescribe` runs two steps in order (`look` then `prescribe`), each with its own delay, then forwards to `review`.
6. `review` runs its single step (with delay) and marks the task complete.

