def task_stats(tasks):

    total = len(tasks)

    completed = 0

    pending = 0

    high = 0

    medium = 0

    low = 0

    for task in tasks:

        parts = task.split("|")

        if len(parts) >= 4:

            status = parts[1]

            priority = parts[2]

            if status == "Completed":

                completed += 1

            else:

                pending += 1

            if priority.lower() == "high":

                high += 1

            elif priority.lower() == "medium":

                medium += 1

            elif priority.lower() == "low":

                low += 1

    print("\n===== TASK STATISTICS =====\n")

    print("Total Tasks      :", total)

    print("Completed Tasks  :", completed)

    print("Pending Tasks    :", pending)

    print()

    print("High Priority    :", high)

    print("Medium Priority  :", medium)

    print("Low Priority     :", low)