from datetime import datetime

class Task:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        self.created_at = datetime.now()
