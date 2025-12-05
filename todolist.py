tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Added!")

    elif choice == "2":
        for t in tasks:
            print("-", t)

    elif choice == "3":
        break

    else:
        print("Invalid choice")
