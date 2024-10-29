import Task
class TaskManager:
    def __init__(self) -> None:
        self.login_info = None
        self.tasks = []

    def add_task(self):
        task = Task()
    
        task.name = input("Task Name: ")
        task.description = input("Description: ")
        task.due_date = input("Enter Due Date(MM-DD-YYYY): ")
        task.completion_flag = False
    
        self.tasks.append(task)
    
        return None
    
    def delete_task(self):
        task_to_remove = input("Please enter the exact name of the name you want to remove")
        for task in self.tasks:
            if task.name == task_to_remove:
                self.tasks.remove(task)
            else:
                print(f"{task_to_remove} was not found in current tasks")

