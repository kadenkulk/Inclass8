# Main menu for the CLI app
from taskManager import TaskManager

def main_menu():
    task_manager = TaskManager()
    while True:
        print("Task Manager Menu")
        print("1. Add a task")
        print("2. List tasks")
        print("3. Delete a task")
        print("4. Mark a task as complete")
        print("5. Exit")
        choice = input("Enter your choice (1, 2, 3, 4, 5, 6): ")

        if choice == '1':
            task_manager.add_task()
        elif choice == '2':
            task_manager.display_tasks()
        elif choice == '3':
            task_manager.delete_task()
        elif choice == '4':
            task_manager.mark_complete()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main_menu()