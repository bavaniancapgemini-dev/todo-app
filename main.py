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
from filter import filter_tasks

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
    print(Fore.CYAN + "9. Edit Task")
    print(Fore.CYAN + "10. Filter Task")
    print(Fore.CYAN + "11. Exit")

    choice = input("Choose: ")

    if choice == "1":

        task_name = input("Enter Task: ")

        priority = input("Priority (High/Medium/Low): ")
        
        category = input("Category: ")

        due_date = input("Due Date (YYYY-MM-DD): ")

        created_date = datetime.now().strftime("%Y-%m-%d")

        task = f"{task_name}|Pending|{priority}|{category}|{created_date}|{due_date}"

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

        show_tasks(tasks)

        number = int(input("Enter Task Number To Edit: "))

        index = number - 1

        if index >= 0 and index < len(tasks):

            old = tasks[index].split("|")

            print("Leave blank to keep old value")

            new_name = input(f"New Name ({old[0]}): ")
            new_priority = input(f"New Priority ({old[2]}): ")
            new_category = input(f"New Category ({old[3]}): ")
            new_due = input(f"New Due Date ({old[5]}): ")

            name = new_name if new_name else old[0]
            priority = new_priority if new_priority else old[2]
            category = new_category if new_category else old[3]
            due = new_due if new_due else old[5]

            updated = f"{name}|{old[1]}|{priority}|{category}|{old[4]}|{due}"

            tasks[index] = updated

            save_tasks(tasks)

            print(Fore.GREEN + "Task Updated")

        else:

            print(Fore.RED + "Invalid Task")
            
    elif choice == "10":
        
        filter_tasks(tasks)

    elif choice == "11":

        print("Goodbye!")

        break

    else:

        print("Invalid Choice")