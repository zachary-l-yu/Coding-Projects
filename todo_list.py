# a to do list app (CLI)
# started: April 3, 2026 (night)
# ended: April 4, 2026 (arvo)
import time


def add_tasks(tasks):
    task_to_add = input("Enter the task you wish to add: ").strip().title()
    time.sleep(3)

    # add the new task
    tasks.append(task_to_add)

    print(f"Added '{task_to_add}' to tasks! \n")
    time.sleep(3)


def remove_tasks(tasks):
    if not tasks:
        print("You have no tasks! \n")
    else:
        # show all tasks
        view_tasks(tasks)

        # get index of the task to remove
        task_to_remove = int(
            input("Enter the number of the task you wish to remove: "))
        time.sleep(3)

        # i printed before removing the task to avoid index errors
        print(f"Removed '{tasks[task_to_remove-1]}' from tasks! \n")

        # remove the task
        tasks.pop(task_to_remove - 1)

    time.sleep(3)


def view_tasks(tasks):
    if not tasks:
        print("You have no tasks! \n")
    else:
        # print each task
        # lists are 0-indexed that's why i added 1
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")

        print()

    time.sleep(3)


# main game variables/lists
# user starts with no tasks
tasks = []


# main game loop
while True:
    # show options
    print("========== OPTIONS ===========")
    print("1.  ADD TASKS")
    print("2.  REMOVE TASKS")
    print("3.  VIEW TASKS")
    print("4.  LEAVE")
    print("==============================")

    choice = input("What would you like to do (1-4)? ")

    # direct user to do what they want
    if choice == "1":
        add_tasks(tasks)

    elif choice == "2":
        remove_tasks(tasks)

    elif choice == "3":
        view_tasks(tasks)

    # quits the program
    elif choice == "4":
        break

    # check for invalid responses
    else:
        print("Invalid input. \n")
        time.sleep(3)
