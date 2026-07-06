from colorama import Fore

def show_tasks(tasks):

    print("\n===== ALL TASKS =====\n")

    if len(tasks) == 0:

        print("No tasks available")

        return

    for i, task in enumerate(tasks):

        parts = task.split("|")

        # OLD FORMAT SUPPORT
        if len(parts) == 1:

            name = parts[0]

            status = "Pending"

            priority = "Medium"

            date = "No Date"

        elif len(parts) == 3:

            name = parts[0]

            status = parts[1]

            priority = "Medium"

            date = parts[2]

        else:

            name = parts[0]

            status = parts[1]

            priority = parts[2]

            date = parts[3]

        symbol = "[X]" if status == "Completed" else "[ ]"

        # PRIORITY COLORS
        if priority.lower() == "high":

            priority_color = Fore.RED

        elif priority.lower() == "medium":

            priority_color = Fore.YELLOW

        else:

            priority_color = Fore.GREEN

        print(f"{i+1}. {symbol} {name}")

        print(f"   Status  : {status}")

        print(f"   Priority: {priority_color}{priority}")

        print(f"   Date    : {date}")

        print()