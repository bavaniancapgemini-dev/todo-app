def edit_task(tasks, index, new_name):

    parts = tasks[index].split("|")

    status = parts[1]

    date = parts[2]

    tasks[index] = f"{new_name}|{status}|{date}"

    return tasks