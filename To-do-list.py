print("Welcome to the To-Do List App. \n") 

tasks = []

def add_task(tasks):
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list of tasks.")


def view_tasks(tasks):
    if not tasks:
        print ("There are no tasks currently.")
    else:
        print("Current Tasks: ")
        for index, task in enumerate(tasks):
            print(f"Tasks #{index}. {task}")

def complete_tasks(tasks):
    if not tasks:
        print("There are currently no tasks to complete.")
        return
    
    view_tasks(tasks)
    index = int(input("Enter a number of the task to mark as completed."))

    if 0<= index <len(tasks):
        task_completed = tasks.pop(index)
        print(f"Your task '{task_completed}' has been completed. \nIt was also deleted from the list.")
    else:
        print("Sorry the task you have chosen was not found. \n Please try again.")


def delete_task():
    view_tasks(tasks)
    try:
        task_to_delete = int(input("Choose the number of the task you want to delete: "))
        if task_to_delete >= 0 and task_to_delete < len(tasks):
           tasks.pop(task_to_delete)
           print(f"Task {task_to_delete} has been deleted from the list.")
        else:
            print(f"Tasks #{task_to_delete}. {tasks} was not found in the list. \nPlease try again. ")
    except TypeError:
        print("Sorry the item you tried to delete wasn't in the system. Please try again.")



while True: # Will repeat unitl 5 is chosen to stop the loop
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")
    
    try:
        decision = input("What would you like to do. ")
    except ValueError:
        print("Please enter a number.")


    if decision == "1": # Add Task
        add_task(tasks)
    elif decision == "2": # View Tasks
        view_tasks(tasks)
    elif decision == "3": # Mark a task as complete
        complete_tasks(tasks)
    elif decision == "4": # Delete Task
        delete_task()
    elif decision == "5": # Quit 
       print("Thank you for using our program. \nHave a wonderful day.")
       break
    else:
        print("Invalid input. Please enter a number and try again. ")
     