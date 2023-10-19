from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    task = TASK_TEMPLATE.copy() 
    # don't delete this; use this task reference for the below requirements
    # 1.update lastActivity with the current datetime value
    # 2.set the name, description, and due date (all must be provided)
    # 3.due date must match one of the formats mentioned in str_to_datetime()
    # 4.add the new task to the tasks list
    # 5.output a message confirming the new task was added or if the addition was rejected due to missing data based on the prior checks
    # 6.make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # 7.make sure any checks/conditions clearly display an appropriate message of what failed
    task = TASK_TEMPLATE.copy()
    task["lastActivity"] = datetime.now() #1.updating lastActivity
    task["name"] = name
    task["description"] = description       #2.set the name,description
    #checking the format for the due date and time
    try:
        datetime.strptime(due, "%m/%d/%y %H:%M:%S") #3.checking due date format
        #print("The variable is in the correct format (mm/dd/yy hh:mm:ss).") 
        task["due"] = due
    except ValueError: #7.checking failure conditions
        # If parsing fails, try the "yyyy-mm-dd hh:mm:ss" format
        try:
            datetime.strptime(due, "%Y-%m-%d %H:%M:%S")
            task["due"] = due
            #print("The variable is in the correct format (yyyy-mm-dd hh:mm:ss).")
        except ValueError:
            print("The variable is not in the correct format.")
    
    #checking if everything is correctly added.
    if task["name"] and task["description"] and task["due"] and task["lastActivity"]:
        print(f"Task '{task['name']}' added successfully.")#5.printing message
        tasks.append(task) #4.adding newt task to tasklist
    else:
        print("Failed to add task. Please make sure all required fields are filled in.")
    #nv335 10.2.2023
    save() #6.saving the file

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # show the existing value of each property where the TODOs are marked in the text of the inputs below (replace the TODO related text with the found tasks's data)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    if bool(index > 1 and index < len(tasks)):
            name = input(f"What's the name of this task? (TODO name) \n").strip()
            desc = input(f"What's a brief descriptions of this task? (TODO description) \n").strip()
            due = input(f"When is this task due (format: m/d/y H:M:S) (TODO due) \n").strip()
            update_task(index, name=name, description=desc, due=due)
            exit
    else:
        print("Task does not exist. Please input correct index of the task") 

    
def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    # find the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # update incoming task data if it's provided (if it's not provided use the original task property value)
    # update lastActivity with the current datetime value
    # output that the task was updated if any items were changed, otherwise mention task was not updated
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    
    #Maybe usually this function is already called by another function within this application.
    #index is also provided/taken input as the first argument to this function. 
    
    #finding task by index; index out of bounds condition checked with appropriate message.
    try:
        task = tasks[index]
    except IndexError:
        raise IndexError("Invalid task index")
    
    # Updates the incoming task data if it's provided (if it's not provided use the original task property value).
    if name:
        task["name"] = name
    if description:
        task["description"] = description
    if due:
        task["due"] = due

    # Updates the lastActivity field with the current datetime value.
    task["lastActivity"] = datetime.now()

    # Outputs that the task was updated if any items were changed, otherwise mentions task was not updated.
    if name or description or due:
        print(f"Task '{task['name']}' updated successfully.")
    else:
        print("Task was not updated.")
    #nv335 10.2.20
    save()

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # if it's not currently marked as done, record the current datetime as the value (don't just set it as true)
    # if it is currently done, print a message saying it's already been completed
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    """ Updates a single task, via index, to a done datetime """

    # Finds the task by index.
    try:
        task = tasks[index]
    except IndexError:
        raise IndexError("Invalid task index")

    # If the task is not currently marked as done, records the current datetime as the value.
    if not task["done"]:
        task["done"] = datetime.now()

    # Outputs a message indicating whether the task was marked as done or was already done.
    if not task["done"]:
        print(f"Task '{task['name']}' marked as done.")
    else:
        print("Task is already done.")
    save()

def view_task(index):
    """ View more info about a specific task fetch by index """
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # utilize the given print statement when a task is found
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    task = {} # <-- replace or update the assignment of this variable, I just used an empty dict so it would run without changes
    try: 
        task = tasks[index] #assigned the enetered list of task in a variable named task 
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    except:
        print("The index that you entered doesnot exist") #if index is out of bound prints this statement
        return
    print(f"""
        [{'x' if task['done'] else ' '}] Task: {task['name']}\n 
        Description: {task['description']} \n 
        Last Activity: {task['lastActivity']} \n
        Due: {task['due']}\n
        Completed: {task['done'] if task['done'] else '-'} \n
        """.replace('  ', ' '))


def delete_task(index):
    """ deletes a task from the tasks list by index """
    # delete/remove task from list by index
    # message should show if it was successful or not
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    """ deletes a task from the tasks list by index """

    # Finds the task by index.
    try:
        task = tasks[index]
        tasks.remove(task)
        # Outputs a message indicating that the task was deleted.
        print(f"Task '{task['name']}' deleted.")
    except:
        print("The index that you entered doesnot exist")
    '''
    # Removes the task from the list.
    tasks.remove(task)

    # Outputs a message indicating that the task was deleted.
    print(f"Task '{task['name']}' deleted.")'''
    save()

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    # generate a list of tasks where the task is not done
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    _tasks = [] # <-- this is a placeholder to populate based on the above requirements
    list_tasks(_tasks)
    #from here;
    """ prints a list of tasks that are not done """
    
    # Generates a list of tasks where the task is not done.
    incomplete_tasks = []
    for task in tasks:
        if not task["done"]:
            incomplete_tasks.append(task)

    # Prints the list of incomplete tasks.
    list_tasks(incomplete_tasks)

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    # generate a list of tasks where the due date is older than "now" and that are not complete (i.e., not done)
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    #_tasks = [] # <-- this is a placeholder to populate based on the above requirements
    #list_tasks(_tasks)
    #starts here
    """ prints a list of tasks that are over due completion (not done and expired) """

    # Generates a list of tasks where the due date is older than "now" and that are not complete (i.e., not done).
    overdue_tasks = []
    now_datetime= datetime.now()
    now = now_datetime.strftime("%m/%d/%Y, %H:%M:%S")
    #print(type(now))
    for task in tasks:
        #print(type(task["due"]))
        if task["due"] < now and not task["done"]:
            overdue_tasks.append(task)

    # Prints the list of overdue tasks.
    list_tasks(overdue_tasks)


def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # get the days, hours, minutes, seconds between the due date and now
    # display the remaining time via print in a clear format showing X days, X hours, X minutes, X seconds (time components must be clearly separated)
    # example: 1 day, 0 hours, 0 minutes, 0 seconds remaining
    # if the due date is in the past print out how many days, hours, minutes, seconds the task is overdue (clearly note that it's overdue, values should be positive)
    # example: 0 days, 2 hours, 5 minutes, 10 seconds overdue (note there's no negative values)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    #task = {}# <-- this is a placeholder to populate based on the above requirements
    # do your print logic here
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """

    # Gets the task by index.
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    # get the task by index
    try:
        task = tasks[index]
    # get the days, hours, minutes, seconds between the due date and now
        now = str_to_datetime(str(datetime.now().strftime("%m/%d/%y %H:%M:%S"))) #used the necessary functions and formats for comparing with due date and present date
        due_date = str_to_datetime(task["due"]) #Due date taken from list with entered index and changed the format 
    # display the remaining time via print in a clear format showing days, hours, minutes, seconds
        if due_date >= now: # if due date is greater than present time then the remaining time will be displayed
            difference = due_date - now
            print("The remaining time is : ", difference)
    # if the due date is in the past print out how many days, hours, minutes, seconds the task is over due (clearly note that it's over due, values should be positive)
        else: # else due date is less than present time then the over due time will be displayed
            difference = now - due_date
            print("The task is over due by: ", difference)
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    except:
    #else:
        if task['done']:
            print("The task is already completed on", task['done'] )
        else:
            print("The index that you entered doesnot exist") #if index is out of bound prints this statement
        return

# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("\n--------------Choices-----------------")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")
    print("--------------------------------------")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1 
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()