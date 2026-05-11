from tasks import show_tasks
from storage import save_tasks, load_tasks
from utils import title


tasks = load_tasks()


while True:

    title()

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose: ")


    if choice == "1":

        task = input("Enter task: ")

        tasks.append(task)

        save_tasks(tasks)

        print("Task Added")


    elif choice == "2":

        show_tasks(tasks)


    elif choice == "3":

        show_tasks(tasks)

        number = int(input("Enter task number to delete: "))

        index = number - 1


        if index >= 0 and index < len(tasks):

            tasks.pop(index)

            save_tasks(tasks)

            print("Task Deleted")

        else:

            print("Invalid Task")


    elif choice == "4":

        print("Goodbye!")

        break


    else:

        print("Invalid Choice")