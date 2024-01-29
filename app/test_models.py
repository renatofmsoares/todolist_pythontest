from .tasks_module.models import Task

class TestTask(Task):
    def __init__(self, title, description="", test_attribute=None):
        super().__init__(title, description)
        self.test_attribute = test_attribute

