from tasks import show_tasks
from storage import save_tasks, load_tasks
from utils import title
from search import search_task
from edit import edit_task
from datetime import datetime
from colorama import Fore, init
from dashboard import show_dashboard
from stats import task_stats
from complete import complete_task
from clear_completed import clear_completed
from productivity import productivity_report


init(autoreset=True)

tasks = load_tasks()


while True:

    title()

    print(Fore.CYAN + "1. Add Task")
    print(Fore.CYAN + "2. View Tasks")
    print(Fore.CYAN + "3. Delete Task")
    print(Fore.CYAN + "4. Complete Task")
    print(Fore.CYAN + "5. Task Statistics")
    print(Fore.CYAN + "6. Clear Completed Tasks")
    print(Fore.CYAN + "7. Productivity Report")
    print(Fore.CYAN + "8. Dashboard")
    print(Fore.CYAN + "9. Exit")

    choice = input("Choose: ")

    if choice == "1":

        task_name = input("Enter Task: ")

        priority = input("Priority (High/Medium/Low): ")

        due_date = input("Due Date (YYYY-MM-DD): ")

        created_date = datetime.now().strftime("%Y-%m-%d")

        task = f"{task_name}|Pending|{priority}|{created_date}|{due_date}"

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
        
        show_dashboard(tasks)

    elif choice == "9":

        print("Goodbye!")

        break

    else:

        print("Invalid Choice")