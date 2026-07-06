from tasks import show_tasks
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
from database import *
from security import hash_password
from getpass import getpass


init(autoreset=True)

failed_attempts = 0

CURRENT_USER = ""

while True:

    print("\n===== TODO APP LOGIN =====")

    print("1. Login")
    print("2. Register")
    print("3. Exit")

    auth_choice = input("Choose: ")

    if auth_choice == "1":

        username = input("Username: ")
        password = getpass("Password: ")

        hashed = hash_password(password)

        success = login_user(username, hashed)

        if success:

            CURRENT_USER = username

            print("Login Successful")

            break

        else:

            failed_attempts += 1
            print("Invalid Login")

    elif auth_choice == "2":

        username = input("Choose Username: ")
        password = getpass("Choose Password: ")

        hashed = hash_password(password)

        success = register_user(username, hashed)

        if success:

            print("Account Created")

        else:

            print("Username Already Exists")

    elif auth_choice == "3":

        exit()

    else:

        print("Invalid Choice")
        
tasks = load_tasks(CURRENT_USER)

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
    print(Fore.CYAN + "11. View Activity Logs")
    print(Fore.CYAN + "12. Exit")

    choice = input("Choose: ")

    if choice == "1":

        task_name = input("Enter Task: ")

        priority = input("Priority (High/Medium/Low): ")
        
        category = input("Category: ")

        due_date = input("Due Date (YYYY-MM-DD): ")

        created_date = datetime.now().strftime("%Y-%m-%d")

        task = f"{task_name}|Pending|{priority}|{category}|{created_date}|{due_date}"

        add_task(

            CURRENT_USER,
            task_name,
            "Pending",
            priority,
            category,
            created_date,
            due_date
        )

        print(Fore.GREEN + "Task Added")

    elif choice == "2":

        show_tasks(tasks)


    elif choice == "3":

        task_id = int(input("Enter Task ID To Delete: "))

        delete_task(task_id)

        print("Task Deleted")
            
    elif choice == "4":

        task_id = int(input("Enter Task ID To Complete: "))

        complete_task(task_id)

        print("Task Completed")
    
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

        task_id = int(input("Enter Task ID To Edit: "))

        name = input("New Task Name: ")

        priority = input("New Priority: ")

        category = input("New Category: ")

        due = input("New Due Date: ")

        update_task(
            task_id,
            name,
            priority,
            category,
            due
        )

        print("Task Updated")
            
    elif choice == "10":
        
        filter_tasks(tasks)
        
    elif choice == "11":

        if CURRENT_USER == "admin":

            try:

                with open("activity.log", "r") as file:

                    print(file.read())

            except:

                print("No activity logs")

        else:

            print("Admin access only")

    elif choice == "12":

        print("Goodbye!")

        break

    else:

        print("Invalid Choice")