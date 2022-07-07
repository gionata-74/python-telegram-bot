import datetime

class User:
    def __init__(self, chat_id: str, date: datetime, user_name: str, full_name: str) -> None:
        self.chat_id = chat_id
        self.date = date
        self.user_name = user_name
        self.full_name = full_name
