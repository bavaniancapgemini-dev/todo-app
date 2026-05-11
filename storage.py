def save_tasks(tasks):

    file = open("tasks.txt", "w")

    for task in tasks:

        file.write(task + "\n")

    file.close()

def load_tasks():

    try:

        file = open("tasks.txt", "r")

        tasks = file.read().splitlines()

        file.close()

        return tasks

    except:

        return []