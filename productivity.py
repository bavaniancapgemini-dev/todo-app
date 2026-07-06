from colorama import Fore

def productivity_report(tasks):

    total = len(tasks)

    completed = 0

    for task in tasks:

        parts = task.split("|")

        if len(parts) >= 4:

            if parts[1] == "Completed":

                completed += 1

    if total == 0:

        percent = 0

    else:

        percent = int((completed / total) * 100)

    bars = int(percent / 10)

    progress = "█" * bars + "-" * (10 - bars)

    print("\n===== PRODUCTIVITY REPORT =====\n")

    print(f"Progress: [{progress}] {percent}%")

    print()

    print("Completed Tasks :", completed)

    print("Pending Tasks   :", total - completed)

    print("Total Tasks     :", total)

    print()

    if percent == 100:

        print(Fore.GREEN + "Excellent Productivity!")

    elif percent >= 70:

        print(Fore.CYAN + "Good Work!")

    elif percent >= 40:

        print(Fore.YELLOW + "Keep Improving!")

    else:

        print(Fore.RED + "Need Better Focus!")