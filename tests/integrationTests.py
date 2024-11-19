import unittest
from unittest.mock import patch

from src.taskManager import TaskManager


class TestTaskManager(unittest.TestCase):
    @patch('builtins.input', side_effect=["My Task", "This is a test task", "12-31-2024"])
    def test_Integration(self):
        task_manager = TaskManager()
        task_manager.add_task()

        self.assertEqual(len(task_manager.tasks), 1)
        task = task_manager.tasks[0]

        self.assertEqual(task.name, "My Task")
        self.assertEqual(task.description, "This is a test task")
        self.assertEqual(task.due_date, "12-31-2024")
        self.assertEqual(task.completed, False)

        task.mark_as_complete()
        self.assertEqual(task.completed, True)




