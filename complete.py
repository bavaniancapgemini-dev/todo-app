from storage import save_tasks

def complete_task(tasks, index):

    if index >= 0 and index < len(tasks):

        parts = tasks[index].split("|")

        if len(parts) >= 4:

            parts[1] = "Completed"

            tasks[index] = "|".join(parts)

            save_tasks(tasks)

            return True

    return False