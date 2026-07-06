from colorama import Fore
from datetime import datetime

def show_dashboard(tasks):

    total = len(tasks)

    completed = 0
    pending = 0
    overdue = 0

    today = datetime.now().strftime("%Y-%m-%d")

    for task in tasks:

        parts = task.strip().split("|")

        if len(parts) < 6:
            continue

        status = parts[1]
        due = parts[5]

        if status == "Completed":
            completed += 1
        else:
            pending += 1

        if due < today and status != "Completed":
            overdue += 1

    progress = 0

    if total > 0:
        progress = int((completed / total) * 100)

    print(Fore.CYAN + "\n===== DASHBOARD =====")

    print(Fore.WHITE + f"Total Tasks     : {total}")
    print(Fore.GREEN + f"Completed       : {completed}")
    print(Fore.YELLOW + f"Pending         : {pending}")
    print(Fore.RED + f"Overdue         : {overdue}")
    print(Fore.CYAN + f"Progress        : {progress}%")