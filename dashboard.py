from colorama import Fore

def show_dashboard(tasks):

    total = len(tasks)
    completed = 0
    pending = 0

    for task in tasks:

        parts = task.strip().split("|")

        if len(parts) >= 2:

            status = parts[1]

            if status == "Completed":
                completed += 1
            else:
                pending += 1

    print(Fore.CYAN + "\n===== DASHBOARD =====")
    print(Fore.GREEN + f"Completed Tasks : {completed}")
    print(Fore.YELLOW + f"Pending Tasks   : {pending}")
    print(Fore.WHITE + f"Total Tasks     : {total}")