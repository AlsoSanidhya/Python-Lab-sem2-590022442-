tasks = []

while True:
    print("\n--- To-Do List Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Add task
    if choice == 1:
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added.")

    # 2. View tasks
    elif choice == 2:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(i, ".", task)

    # 3. Update task
    elif choice == 3:
        num = int(input("Enter task number to update: "))
        if 1 <= num <= len(tasks):
            new_task = input("Enter new task: ")
            tasks[num - 1] = new_task
            print("Task updated.")
        else:
            print("Invalid task number.")

    # 4. Delete task
    elif choice == 4:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task deleted.")
        else:
            print("Invalid task number.")

    # 5. Exit
    elif choice == 5:
        print("Exiting To-Do List Manager.")
        break

    else:
        print("Invalid choice.")