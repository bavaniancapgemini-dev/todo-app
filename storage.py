def save_tasks(tasks, username):

    filename = f"{username}_tasks.txt"

    with open(filename, "w") as file:

        for task in tasks:

            file.write(task + "\n")


def load_tasks(username):

    filename = f"{username}_tasks.txt"

    try:

        with open(filename, "r") as file:

            return [line.strip() for line in file.readlines()]

    except:

        return []