from colorama import Fore
from datetime import datetime


def show_tasks(tasks):

    print(Fore.CYAN + "\n===== ALL TASKS =====\n")

    if len(tasks) == 0:

        print(Fore.RED + "No Tasks Found")

        return

    today = datetime.now().strftime("%Y-%m-%d")

    for task in tasks:

        task_id = task[0]
        username = task[1]
        name = task[2]
        status = task[3]
        priority = task[4]
        category = task[5]
        created = task[6]
        due = task[7]

        overdue = ""

        if due < today and status != "Completed":

            overdue = Fore.RED + " ⚠ OVERDUE"

        print(Fore.YELLOW + f"ID: {task_id}")
        print(Fore.WHITE + f"Task      : {name}")
        print(Fore.WHITE + f"Status    : {status}")
        print(Fore.WHITE + f"Priority  : {priority}")
        print(Fore.WHITE + f"Category  : {category}")
        print(Fore.WHITE + f"Created   : {created}")
        print(Fore.WHITE + f"Due Date  : {due}{overdue}")
        print()