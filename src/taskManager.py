import Task
class TaskManager:
    def __init__(self) -> None:
        self.login_info = None
        self.tasks = []
    def delete_task(self):
        task_to_remove = input("Please enter the exact name of the name you want to remove")
        for task in self.tasks:
            if task.name == task_to_remove:
                self.tasks.remove(task)

