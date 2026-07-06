from colorama import Fore
from datetime import datetime

def show_tasks(tasks):

    print(Fore.CYAN + "\n===== ALL TASKS =====\n")

    if len(tasks) == 0:

        print(Fore.RED + "No Tasks Found")
        return

    today = datetime.now().strftime("%Y-%m-%d")

    for i, task in enumerate(tasks, start=1):

        parts = task.strip().split("|")

        if len(parts) < 6:
            continue

        name = parts[0]
        status = parts[1]
        priority = parts[2]
        category = parts[3]
        created = parts[4]
        due = parts[5]

        overdue = ""

        if due < today and status != "Completed":
            overdue = Fore.RED + " ⚠ OVERDUE"

        print(Fore.YELLOW + f"{i}. {name}")
        print(Fore.WHITE + f"   Status    : {status}")
        print(Fore.WHITE + f"   Priority  : {priority}")
        print(Fore.WHITE + f"   Category  : {category}")
        print(Fore.WHITE + f"   Created   : {created}")
        print(Fore.WHITE + f"   Due Date  : {due}{overdue}")
        print()