# Define global variables
tasks = []

def display_menu():
    """Display the menu of the To-Do List App."""
    print("""
    Welcome to the To-Do List App!
    Menu:
    1. Add a task
    2. View tasks
    3. View organized tasks
    4. Mark a task as complete
    5. Mark a task as incomplete
    6. Delete a task
    7. Save and Quit
    """)

def add_task():
    """Add a new task to the list."""
    try:
        title = input("Enter the task title: ")
        priority = input("Enter the priority (High/Medium/Low): ")
        due_date = input("Enter the due date (YYYY-MM-DD): ")
        tasks.append({"title": title, "status": "Incomplete", "priority": priority, "due_date": due_date})
        print("Task added successfully.")
    except Exception as e:
        print(f"An error occurred while adding the task: {e}")

def view_tasks():
    """View all tasks with their details."""
    try:
        if not tasks:
            print("No tasks.")
        else:
            print("Tasks:")
            for index, task in enumerate(tasks, start=1):
                status_color = "\033[92m" if task['status'] == "Complete" else "\033[91m"
                print(f"{index}. {task['title']} - Priority: {task['priority']} - Due Date: {task['due_date']} - Status: {status_color}{task['status']}\033[0m")
        input("Press Enter to return to the main menu.")
    except Exception as e:
        print(f"An error occurred while viewing tasks: {e}")

def view_organized_tasks():
    """View tasks organized by status."""
    try:
        if not tasks:
            print("No tasks.")
        else:
            incomplete_tasks = [task for task in tasks if task["status"] == "Incomplete"]
            complete_tasks = [task for task in tasks if task["status"] == "Complete"]
            print("Organized Tasks:")
            if incomplete_tasks:
                print("Incomplete Tasks:")
                for index, task in enumerate(incomplete_tasks, start=1):
                    status_color = "\033[91m"  # Red color for incomplete tasks
                    print(f"{index}. {task['title']} - Priority: {task['priority']} - Due Date: {task['due_date']} - Status: {status_color}{task['status']}\033[0m")
            else:
                print("No incomplete tasks.")
            if complete_tasks:
                print("Complete Tasks:")
                for index, task in enumerate(complete_tasks, start=1):
                    status_color = "\033[92m"  # Green color for complete tasks
                    print(f"{index}. {task['title']} - Priority: {task['priority']} - Due Date: {task['due_date']} - Status: {status_color}{task['status']}\033[0m")
            else:
                print("No complete tasks.")
        input("Press Enter to return to the main menu.")
    except Exception as e:
        print(f"An error occurred while viewing organized tasks: {e}")

def mark_complete():
    """Mark a task as complete."""
    try:
        view_tasks()
        if not tasks:
            print("No tasks to mark as complete.")
            return
        index = int(input("Enter the index of the task to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["status"] = "Complete"
            print("Task marked as complete.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred while marking task as complete: {e}")
    finally:
        input("Press Enter to return to the main menu.")

def mark_incomplete():
    """Mark a task as incomplete."""
    try:
        view_tasks()
        if not tasks:
            print("No tasks to mark as incomplete.")
            return
        index = int(input("Enter the index of the task to mark as incomplete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["status"] = "Incomplete"
            print("Task marked as incomplete.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred while marking task as incomplete: {e}")
    finally:
        input("Press Enter to return to the main menu.")

def delete_task():
    """Delete a task from the list."""
    try:
        view_tasks()
        if not tasks:
            print("No tasks to delete.")
            return
        index = int(input("Enter the index of the task to delete: ")) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            print("Task deleted successfully.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred while deleting task: {e}")
    finally:
        input("Press Enter to return to the main menu.")

def save_tasks_to_file(filename):
    """Save tasks to a file."""
    try:
        with open(filename, 'w') as file:
            for task in tasks:
                file.write(f"{task['title']},{task['status']},{task['priority']},{task['due_date']}\n")
        print("Tasks saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving tasks to file: {e}")

def get_user_choice():
    """Get user's choice from the menu."""
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 7:
                return choice
            else:
                print("Invalid choice. Please enter a number from 1 to 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """Main function to run the To-Do List application."""
    try:
        while True:
            display_menu()
            choice = get_user_choice()
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                view_organized_tasks()
            elif choice == 4:
                mark_complete()
            elif choice == 5:
                mark_incomplete()
            elif choice == 6:
                delete_task()
            elif choice == 7:
                save_tasks_to_file("tasks.txt")  # Save tasks to file before quitting
                print("Tasks saved. Goodbye!")
                break
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point of the program
if __name__ == "__main__":
    main()