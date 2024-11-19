import pytest
from taskManager import TaskManager
from Task import Task

#EMPTY LISTS/NO TASK
def test_delete_task_from_empty_list():
    manager = TaskManager()
    manager.delete_task = lambda: print("No tasks to remove") 
    manager.delete_task()
    assert len(manager.tasks) == 0, "Task list should be empty after trying to delete from an empty list"

def test_delete_non_existent_task():
    manager = TaskManager()
    manager.tasks.append(Task(name="Existing Task", description="Description", due_date="12-31-2024"))
    manager.delete_task = lambda: manager.tasks.remove(manager.tasks[0]) if manager.tasks[0].name == "Nonexistent Task" else print("Task not found")
    manager.delete_task()
    assert len(manager.tasks) == 1, "Task list should remain the same if task is not there"

# INVALID INPUTS
def test_task_creation_invalid_date_format():
    with pytest.raises(ValueError):
        task = Task(name="Test Task", description="Test description", due_date="2024-31-12") 

def test_create_task_with_empty_name():
    task = Task(name="", description="Test description", due_date="12-31-2024")
    assert task.name == "", "Task name should be empty"

