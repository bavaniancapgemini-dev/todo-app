from tasks import show_tasks
from storage import save_tasks, load_tasks
from utils import title
from search import search_task
from edit import edit_task
from datetime import datetime
from colorama import Fore, init
from stats import task_stats
from complete import complete_task
from clear_completed import clear_completed
from productivity import productivity_report


init(autoreset=True)

tasks = load_tasks()


while True:

    title()

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Complete Task")
    print("5. Task Statistics")
    print("6. Clear Completed Tasks")
    print("7. Productivity Report")
    print("8. Exit")

    choice = input("Choose: ")

    if choice == "1":

        task_name = input("Enter task: ")

        priority = input("Priority (Low/Medium/High): ")

        date = input("Enter due date (YYYY-MM-DD): ")

        task = f"{task_name}|Pending|{priority}|{date}"

        tasks.append(task)

        save_tasks(tasks)

        print(Fore.GREEN + "Task Added")

    elif choice == "2":

        show_tasks(tasks)


    elif choice == "3":

        show_tasks(tasks)

        number = int(input("Enter task number to delete: "))

        index = number - 1


        if index >= 0 and index < len(tasks):

            tasks.pop(index)

            save_tasks(tasks)

            print("Task Deleted")

        else:

            print("Invalid Task")
            
    elif choice == "4":

        show_tasks(tasks)

        number = int(input("Enter task number to complete: "))

        index = number - 1
        
        success = complete_task(tasks, index)

        if success:
            
            print(Fore.GREEN + "Task Completed")

        else:

            print(Fore.RED + "Invalid Task")
            
    
    elif choice == "5":

        task_stats(tasks)
        
    elif choice == "6":

        tasks = clear_completed(tasks)

        print(Fore.GREEN + "Completed Tasks Cleared")
        
    elif choice == "7":

        productivity_report(tasks)

    elif choice == "8":

        print("Goodbye!")

        break

    else:

        print("Invalid Choice")