# TODO List Management APP

# Plan
# when we run the program - we need to load the existing items from the file and display them.
# 1. Creating a new item
# 2. List items
# 3. Mark an item as completed / incomplete
# 4. Delete an item
# 4. Save items

# Write some of the functions that we'll have in order to kind of perform these operations.
# So the way that I start a larger program like this is I begin by just writing out the core operations
# I don't implement them, so I don't write all of the code and make it work, but I just write kind of the name of different functions and I start just mapping the program out a little bit.
# So visually I know what's going on.

import json

# Sample json format:

# {
#     "tasks": [
#         {"description": "Buy groceries", "completed": false},
#         {"description": "Clean the house", "completed": false},
#         {"description": "Go to the gym", "completed": false}
#     ]
# }

# "   ".isspace()      # Returns True
# "hello".isspace()    # Returns False
# "\t\n  ".isspace()   # Returns True
# "   a   ".isspace()  # Returns False

file_name = "todo_list.json"

def load_tasks():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"tasks": []}

def save_tasks(tasks):
    try:
        with open(file_name, 'w') as file:
            json.dump(tasks, file) # json.dump() function is used when we want to use json data into a file. It takes two arguments, the json data and the file object that you want to save the data to.
    except:
        print("Failed to save, Error saving tasks")


def view_tasks(tasks):
    print()
    tasks_list = tasks['tasks']
    if len(tasks_list) == 0:
        print("No tasks available.")
    else:
        print("Your tasks are: ")
        for idx, task in enumerate(tasks_list):
            status = "[Completed]" if task['completed'] else "[Incomplete]"
            print(f"Task {idx + 1}. {task['description']} | {status}")


def create_task(tasks):
    description = input("Enter the description of the task: ").strip()
    if description and not description.isspace(): # This ensures the description is neither empty nor just whitespace. Only executes if description has actual text content
        tasks["tasks"].append({"description": description, "completed": False})#Dictionary: If you pass them b/n different functions, any changes you make to them inside the function will apply outside the function as well.
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Invalid task. Task description cannot be empty.")


def mark_task_complete(tasks):
    view_tasks(tasks)
    id = input("\nWhich task id should be marked as complete? ").strip()
    task_status_updated(id, tasks, True)


def task_status_updated(id, tasks, status):
    try:
        task_id = int(id)
        tasks_list = tasks['tasks']
        if task_id > 0 and task_id <= len(tasks_list):
            if status:
                tasks_list[task_id - 1]['completed'] = True
                complete = "complete"
            else:
                tasks_list[task_id - 1]['completed'] = False
                complete = "incomplete"
            save_tasks(tasks)
            print(f"Task {task_id} marked as {complete}.")
        else:
            print("Invalid task id.")
    except ValueError:
        print("Invalid task id. Please enter a number.")


def mark_task_incomplete(tasks):
    view_tasks(tasks)
    id = input("\nWhich task id should be marked as incomplete? ").strip()
    task_status_updated(id, tasks, False)


def delete_task(tasks):
    view_tasks(tasks)
    id = input("\nWhich task id should be deleted? ").strip()
    try:
        task_id = int(id)
        tasks_list = tasks['tasks']
        if task_id > 0 and task_id <= len(tasks_list):
            confirm = input(f"Are you sure you want to delete task {task_id}? (y/n): ").lower()
            if confirm == 'y':
                del tasks_list[task_id - 1]
                save_tasks(tasks)
                print(f"Task {task_id} deleted.")
            else:
                print("Delete cancelled.")
        else:
            print("Invalid task id.")
    except ValueError:
        print("Invalid task id. Please enter a number.")


def main():
    tasks = load_tasks()
    # print(tasks['tasks'][0]['description']) # Task1Description

    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete task")
        print("4. InComplete task")
        print("5. Delete task")
        print("6. Exit")

        choice = input("Enter your choice: " ).strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            mark_task_incomplete(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please try again.")


main()