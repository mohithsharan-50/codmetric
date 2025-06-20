TASK_FILE = "tasks.txt"


def load_tasks():
    tasks = []
    try:
        with open(TASK_FILE, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 2:
                    task = {"description": parts[0], "completed": parts[1] == "True"}
                    tasks.append(task)
    except FileNotFoundError:
        pass
    return tasks


def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task['description']}|{task['completed']}\n")


def add_task(tasks):
    desc = input("Enter the task description: ")
    task = {"description": desc, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")


def delete_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            save_tasks(tasks)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def mark_completed(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Pending"
            print(f"{i}. {task['description']} [{status}]")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== To-Do List Manager =====")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            delete_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            display_tasks(tasks)
        elif choice == "5":
            print("Exiting To-Do List Manager. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


main()
