def show_tasks(tasks):

    print("\n---- TASKS ----")

    if len(tasks) == 0:

        print("No tasks available")

    else:

        for i, task in enumerate(tasks):

            print(i + 1, "-", task)