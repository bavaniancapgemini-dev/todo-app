def search_task(tasks, keyword):

    found = False

    print("\n===== SEARCH RESULTS =====")

    for i, task in enumerate(tasks):

        if keyword.lower() in task.lower():

            parts = task.split("|")

            print(f"{i+1}. {parts[0]}")

            print("   Status :", parts[1])

            print("   Date   :", parts[2])

            print()

            found = True

    if not found:

        print("No matching tasks found")