# Define global variables
tasks = []

# Function to display the menu
def display_menu():
    print("""
    Welcome to the To-Do List App!
    Menu:
    1. Add a task
    2. View tasks
    3. View organized tasks
    4. Mark a task as complete
    5. Delete a task
    6. Quit
    """)

# Function to add a task
def add_task():
    title = input("Enter the task title: ")
    tasks.append({"title": title, "status": "Incomplete"})
    print("Task added successfully.")

# Function to view tasks
def view_tasks():
    if not tasks:
        print("No tasks.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']} - {task['status']}")
    input("Press Enter to return to the main menu.")

# Function to view organized tasks
def view_organized_tasks():
    if not tasks:
        print("No tasks.")
    else:
        incomplete_tasks = [task for task in tasks if task["status"] == "Incomplete"]
        complete_tasks = [task for task in tasks if task["status"] == "Complete"]
        print("Organized Tasks:")
        if incomplete_tasks:
            print("Incomplete Tasks:")
            for index, task in enumerate(incomplete_tasks, start=1):
                print(f"{index}. {task['title']} - {task['status']}")
        else:
            print("No incomplete tasks.")
        if complete_tasks:
            print("Complete Tasks:")
            for index, task in enumerate(complete_tasks, start=1):
                print(f"{index}. {task['title']} - {task['status']}")
        else:
            print("No complete tasks.")
    input("Press Enter to return to the main menu.")

# Function to mark a task as complete
def mark_complete():
    view_tasks()
    try:
        index = int(input("Enter the index of the task to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["status"] = "Complete"
            print("Task marked as complete.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    input("Press Enter to return to the main menu.")

# Function to delete a task
def delete_task():
    view_tasks()
    try:
        index = int(input("Enter the index of the task to delete: ")) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            print("Task deleted successfully.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    input("Press Enter to return to the main menu.")

# Main function
def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                view_organized_tasks()
            elif choice == 4:
                mark_complete()
            elif choice == 5:
                delete_task()
            elif choice == 6:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Entry point of the program
if __name__ == "__main__":
    main()