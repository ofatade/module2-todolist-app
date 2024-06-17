# To-Do list Application

task_to_do = []

completed_tasks = []  


def add_task():
    task1 = input("Put the first task that needs to be complete ")
    task_to_do.append(task1.lower())
    task2 = input("Put the second task that needs to be complete ")
    task_to_do.append(task2.lower())
    task3 = input("Put the third task that needs to be complete ")
    task_to_do.append(task3.lower())


def view_tasks():
    if task_to_do == []:
             print("You have completed all your tasks")
    else:
        print("Here are the tasks that need to be done ")
        for index in range(len(task_to_do)):
            print(index + 1, task_to_do[index])
        

def completed_task():
    while True:
        try:
            done = input("What task have you completed? ")
            if done in task_to_do:
                    task_to_do.remove(done)
                    completed_tasks.append(done)
                    print(f"Successfully added {done} to your completed tasks!")
            else:
                print(f"It looks like you don't have {done} on your task list.")
            break
        except Exception:  # Catch general exceptions if necessary
            print("Invalid input")
        finally:  # This block executes regardless of whether the try block succeeds or not
            print("Your current Completed Task: ")
            print('~' * 30)
            for index in range(len(completed_tasks)):
                print(index + 1, completed_tasks[index])


def delete_task():
    take_out = input("what task would you like to remove? ")
    if take_out in task_to_do:
                    task_to_do.remove(take_out)
                    if take_out in completed_tasks:
                         completed_tasks.remove(take_out)
                    print(f"Successfully removed {take_out} from your to do list!")
    else:
        print(f"It looks like {take_out} is not in your to do list!")
    print("Your current To Do List: ")
    print('~' * 30)
    view_tasks()


def quit_app():
     print("Thanks for using To-Do list Application!")
     

def application():
    while True:
        tasks = input('''
Welcome to the To-Do List App!
                      
What would you like to do?
                      
Enter the corresponding number for the action you'd like to take     

 Menu:
        1. Add a task
        2. View tasks
        3. Mark a task as complete
        4. Delete a task
        5. Quit                 
''')
        
        if tasks == '1':
            add_task() # add function to add to the list
        elif tasks == '2':
            view_tasks() # function for removing from the list
        elif tasks == '3':
            completed_task() # function to view current list
        elif tasks == '4':
            delete_task()
        elif tasks == '5':
            quit_app()
            break
        else:
            print("Please enter a valid number!!")

application()