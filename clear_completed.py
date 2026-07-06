from storage import save_tasks

def clear_completed(tasks):

    new_tasks = []

    for task in tasks:

        parts = task.split("|")

        if len(parts) >= 4:

            if parts[1] != "Completed":

                new_tasks.append(task)

    save_tasks(new_tasks)

    return new_tasks