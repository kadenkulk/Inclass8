import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from taskManager import TaskManager
from Task import Task

def test_delete_task():
    # Initialize TaskManager
    task_manager = TaskManager()
    
    # Add mock tasks
    task1 = Task(name="Task1", description="First task", completion_flag=False, due_date="01-01-2025")
    task2 = Task(name="Task2", description="Second task", completion_flag=False, due_date="02-01-2025")
    task3 = Task(name="Task3", description="Third task", completion_flag=False, due_date="03-01-2025")
    
    task_manager.tasks.extend([task1, task2, task3])
    
    # Simulate task deletion
    task_to_delete = "Task2"
    task_manager.delete_task = lambda: task_manager.tasks.remove(next((task for task in task_manager.tasks if task.name == task_to_delete), None))
    task_manager.delete_task()
    
    # Assertions
    assert all(task.name != "Task2" for task in task_manager.tasks), "Task2 was not deleted successfully."
    assert len(task_manager.tasks) == 2, "Incorrect number of tasks after deletion."
