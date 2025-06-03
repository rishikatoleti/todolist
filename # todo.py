# todo.py

todo_list = []

def show_menu():
    print("\n===== To-Do List Menu =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Edit task")
    print("4. Mark task as complete")
    print("5. Delete task")
    print("6. Exit")

def add_task():
    task = input("Enter task description: ")
    priority = input("Enter priority (High/Medium/Low): ")
    todo_list.append({"task": task, "done": False, "priority": priority})
    print("Task added successfully.")

def view_tasks():
    if not todo_list:
        print("No tasks found.")
    else:
        for i, task in enumerate(todo_list, start=1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['task']} | {task['priority']} | {status}")

def edit_task():
    view_tasks()
    try:
        index = int(input("Enter task number to edit: ")) - 1
        if 0 <= index < len(todo_list):
            new_task = input("New task description: ")
            new_priority = input("New priority (High/Medium/Low): ")
            todo_list[index]["task"] = new_task
            todo_list[index]["priority"] = new_priority
            print("Task updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def mark_complete():
    view_tasks()
    try:
        index = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= index < len(todo_list):
            todo_list[index]["done"] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(todo_list):
            removed = todo_list.pop(index)
            print(f"Task '{removed['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        edit_task()
    elif choice == "4":
        mark_complete()
    elif choice == "5":
        delete_task()
    elif choice == "6":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
