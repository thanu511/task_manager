import json
import os

# Define dummy login credentials
DUMMY_EMAIL = "test@gmail.com"
DUMMY_PASSWORD = "Test@1234"

# Task class and functions remain the same
class Task:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"ID: {self.id}, Title: '{self.title}', Status: {status}"

tasks = []

def add_task(id, title):
    task = Task(id, title)
    tasks.append(task)
    print(f"Task '{title}' added.")

def view_tasks():
    if tasks:
        print("\nCurrent Tasks:")
        for task in tasks:
            print(task)
    else:
        print("\nNo tasks available.")

def delete_task(id):
    global tasks
    tasks = [task for task in tasks if task.id != id]
    print(f"Task with ID {id} deleted.")

def complete_task(id):
    for task in tasks:
        if task.id == id:
            task.completed = True
            print(f"Task with ID {id} marked as completed.")
            return
    print(f"No task found with ID {id}.")

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump([task.__dict__ for task in tasks], file)
    print("Tasks saved to tasks.json.")

def load_tasks():
    global tasks
    if os.path.exists('tasks.json') and os.path.getsize('tasks.json') > 0:
        try:
            with open('tasks.json', 'r') as file:
                tasks_data = json.load(file)
                tasks = [Task(**data) for data in tasks_data]
                print("Tasks loaded from tasks.json.")
        except json.JSONDecodeError:
            print("Error: tasks.json is not in a valid format. Starting with an empty task list.")
            tasks = []
    else:
        print("No existing tasks found. Starting with an empty task list.")

# New function for login
def login():
    print("Please log in to access the Task Manager.")
    email = input("Enter email: ")
    password = input("Enter password: ")

    if email == DUMMY_EMAIL and password == DUMMY_PASSWORD:
        print("Login successful.")
        return True
    else:
        print("Invalid credentials. Access denied.")
        return False

# Main function with login check
def main():
    if not login():
        return  # Exit if login fails
    
    load_tasks()
    while True:
        print("\nTask Manager CLI")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Save and Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            task_id = len(tasks) + 1
            title = input("Enter task title: ")
            add_task(task_id, title)
        
        elif choice == '2':
            view_tasks()
        
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        
        elif choice == '4':
            task_id = int(input("Enter task ID to mark as complete: "))
            complete_task(task_id)
        
        elif choice == '5':
            save_tasks()
            print("Exiting the application.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
