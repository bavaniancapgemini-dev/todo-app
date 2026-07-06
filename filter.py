from colorama import Fore
from datetime import datetime

def filter_tasks(tasks):

    print("\n1. Pending")
    print("2. Completed")
    print("3. High Priority")
    print("4. Overdue")

    choice = input("Choose Filter: ")

    today = datetime.now().strftime("%Y-%m-%d")

    print(Fore.CYAN + "\n===== FILTERED TASKS =====\n")

    for task in tasks:

        parts = task.strip().split("|")

        if len(parts) < 6:
            continue

        name = parts[0]
        status = parts[1]
        priority = parts[2]
        due = parts[5]

        if choice == "1" and status == "Pending":
            print(name)

        elif choice == "2" and status == "Completed":
            print(name)

        elif choice == "3" and priority.lower() == "high":
            print(name)

        elif choice == "4" and due < today and status != "Completed":
            print(name)