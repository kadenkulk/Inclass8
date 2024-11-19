import Task
class TaskManager:
    def __init__(self) -> None:
        self.login_info = None
        self.tasks = []

    def add_task(self):
        task = Task()

        task.name = input("Task Name: ")
        task.description = input("Description: ")
        task.completion_flag = False

        date_valid = False
        while date_valid == False:
            task.due_date = input("Enter Valid Due Date(MM-DD-YYYY): ")
            date_check = task.due_date.split("-")
            for date in date_check:
                if not (isinstance(date, int)):
                    print("Date not Valid.")
                    break
                else:
                    if date is date_check[-1] and isinstance(date, int):
                        date_valid = True
                        break
                    else:
                        continue
                        
        self.tasks.append(task)
        return None
                    
    
    def delete_task(self):
        task_to_remove = input("Please enter the exact name of the name you want to remove")
        for task in self.tasks:
            if task.name == task_to_remove:
                self.tasks.remove(task)
            else:
                print(f"{task_to_remove} was not found in current tasks")
    
    def display_tasks(self):
        display = input("Please enter how you want it displayed (completed, pending or all)")
        if display.lower() == "completed":
            for task in self.tasks:
                if task.completion_flag == True:
                    print(f"Name: f{task.name}")
        elif display.lower() == "pending":
            for task in self.tasks:
                if task.completion_flag == False:
                    print(f"Name: f{task.name} Due Date: {task.due_date}")
        elif display.lower() == "all":
            for task in self.tasks:
                print(f"Name: f{task.name} Due Date: {task.due_date}")
        else :
            print("Invalid Command")
    
    def mark_complete(self):
        task_name = input("Please enter the exit task name")
        for task in self.tasks:
            if task_name == task.name:
                if task.completion_flag != True:
                    task.completion_flag = True
                else:
                    print("This task is already complete.")
        print("This task does not exist.")

