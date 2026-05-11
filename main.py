tasks = []


while True:

    print("\n---- TODO APP ----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose: ")


    if choice == "1":

        task = input("Enter task: ")

        tasks.append(task)

        print("Task Added")


    elif choice == "2":

        print("\nYour Tasks:")

        for i, task in enumerate(tasks):

            print(i + 1, "-", task)


    elif choice == "3":

        print("\nYour Tasks:")

        for i, task in enumerate(tasks):

            print(i + 1, "-", task)

        number = int(input("Enter task number to delete: "))

        index = number - 1


        if index >= 0 and index < len(tasks):

            tasks.pop(index)

            print("Task Deleted")

        else:

            print("Invalid Task")


    elif choice == "4":

        print("Goodbye!")

        break


    else:

        print("Invalid Choice")