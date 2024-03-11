"""
My modifications to the given code:
	
	1) Create a to-do file
	2) Append the query to the to-do file directly (so it remembers the data)
	3) Overall formatting and code improvement 
	4) Bypass keyboardInterrupt
	
~ Ayus Chatterjee	
"""

import os

# Define the file path for the to-do list
todo_file = "todo.txt"

# Function to create the to-do file if it doesn't exist
def create_todo_file():
    if not os.path.exists(todo_file):
        with open(todo_file, 'w'):
            pass

# Function to display the to-do list
def display_tasks():
    create_todo_file()
    with open(todo_file, 'r') as file:
        tasks = file.readlines()
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")

# Function to add a task to the to-do list
def add_task(task_name):
    create_todo_file()
    with open(todo_file, 'a') as file:
        file.write(task_name + "\n")
    print(f"Task '{task_name}' added to your to-do list.")

# Function to mark a task as completed
def mark_completed(task_number):
    create_todo_file()
    with open(todo_file, 'r') as file:
        tasks = file.readlines()
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1] = tasks[task_number - 1].strip() + " (Completed)\n"
        with open(todo_file, 'w') as file:
            file.writelines(tasks)
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number. Please enter a valid task number.")

# Function to remove a task from the to-do list
def remove_task(task_number):
    create_todo_file()
    with open(todo_file, 'r') as file:
        tasks = file.readlines()
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        with open(todo_file, 'w') as file:
            file.writelines(tasks)
        print(f"Task '{removed_task.strip()}' removed from your to-do list.")
    else:
        print("Invalid task number. Please enter a valid task number.")

# Main program loop
while True:
    try:
        print("\nOptions:")
        print("1. Display to-do list")
        print("2. Add a task")
        print("3. Mark a task as completed")
        print("4. Remove a task")
        print("5. Quit")
        print("")
        choice = input("Enter your choice: ")
        os.system("clear")
	    
        if choice == '1':
            display_tasks()
        elif choice == '2':
            task_name = input("Enter the task: ")
            add_task(task_name)
        elif choice == '3':
            display_tasks()
            task_number = int(input("Enter the task number to mark as completed: "))
            mark_completed(task_number)
        elif choice == '4':
            display_tasks()
            task_number = int(input("Enter the task number to remove: "))
            remove_task(task_number)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Program will continue.")
        
