                         main.py
                            │
                            ▼
                     ┌─────────────┐
                     │ TaskService │
                     └──────┬──────┘
                            │
              ┌─────────────┼──────────────┐
              ▼             ▼              ▼
        TaskRepository  HistoryService  Strategies
                            │
                            ▼
                  HistoryRepository

                     ReminderService
                            │
                            ▼
                      TaskService