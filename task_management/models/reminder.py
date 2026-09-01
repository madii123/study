from datetime import datetime


class Reminder:
    def __init__(self, reminder_id: int, remind_at: datetime):
        self.reminder_id = reminder_id
        self.remind_at = remind_at
