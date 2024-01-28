from datetime import datetime
import hashlib

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.created_at = datetime.now()
        self.id = self.generate_hash()

    def generate_hash(self):
        # Create a hash based on task attributes
        hash_string = f"{self.title}{self.description}"
        hash_object = hashlib.sha256(hash_string.encode())
        return hash_object.hexdigest()
