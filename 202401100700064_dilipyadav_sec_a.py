filename = "tasks.txt"

def add_task():
    task = input("Enter new task: ")
    with open(filename, "a") as file:
        file.write("[ ] " + task + "\n")
    print("Task added.")

def view_tasks():
    print("\n--- Task List ---")
    with open(filename, "r") as file:
        tasks = file.readlines()
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.strip()}")

def delete_task():
    view_tasks()
    num = int(input("Enter task number to delete: "))
    with open(filename, "r") as file:
        tasks = file.readlines()
    if 1 <= num <= len(tasks):
        del tasks[num - 1]
        with open(filename, "w") as file:
            file.writelines(tasks)
        print("Task deleted.")
    else:
        print("Invalid task number.")

def mark_completed():
    view_tasks()
    num = int(input("Enter task number to mark as completed: "))
    with open(filename, "r") as file:
        tasks = file.readlines()
    if 1 <= num <= len(tasks):
        if "[✔]" in tasks[num - 1]:
            print("[✔]Task already completed.")
        else:
            tasks[num - 1] = tasks[num - 1].replace("[ ]", "[✔]", 1)
            with open(filename, "w") as file:
                file.writelines(tasks)
            print("[✔]Task marked as completed.")
    else:
        print("Invalid task number.")

# Main loop
while True:
    print("\n1. Add task\n2. View task\n3. Delete task\n4. Mark as completed\n5. Exit\n")
    choice = input("Choose option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        mark_completed()
    elif choice == "5":
        print("Exiting... Bye Dilip!")
        break
    else:
        print("Enter a valid option (1-5).")
