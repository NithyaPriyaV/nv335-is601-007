from datetime import datetime #imports all the content from the datetime module, but requires you to precede names that are imported from that module with the datetime. qualifier in your code.
import json #The JSON module is mainly used to convert the python dictionary above into a JSON string that can be written into a file.
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
    task = TASK_TEMPLATE.copy() # don't delete this
    #if name and description and due:
    try:
        # update lastActivity with the current datetime value
        task['lastActivity'] = datetime.now() #used imported datetime function to update lastActivity with the current datetime value  
        # set the name, description, and due date (all must be provided)
        task['name'] = name 
        task['description'] = description
        task['due'] = due
        # I have placed the entered name, description and due values in the dictionary named task individually.
        # due date must match one of the formats mentioned in str_to_datetime()
        task['due'] = str_to_datetime(due)
        # add the new task to the tasks list
        tasks.append(task)
        # I used append function to add the entered dictionary values in the tasks list
        # output a message confirming the new task was added or if the addition was rejected due to missing data
        # I used try and except to show that the task was added successfully or rejected.
        print("The new task has been added successfully!!!")
    except Exception as e:
        print("The new task was rejected due to the following issue: \n", e)      
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # """my ucid: vb437 and Date: 23/02/23"""
    save()

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    # get the task by index
    print(index)
    print(len(tasks))
    if index < len(tasks) and index >= 1: #using if statement I checked that entered task is within length of tasks in the list and made sure the task doesnt go below zero 
    # show the existing value of each property where the TODOs are marked in the text of the inputs (replace the TODO related text)
        name = input(f"What's the name of this task? {tasks[index]['name']} \n").strip()
        desc = input(f"What's a brief descriptions of this task? {tasks[index]['description']} \n").strip()
        due = input(f"When is this task due (format: mm-dd-yy hh:mm:ss) {tasks[index]['due']} \n").strip()
    # above code takes the inputted values which is implemented through f string and added it to tasks.  
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    else:
        print("Task does not exist. Please input correct index of the task") 
        name = input(f"What's the name of this task? {tasks[index]['name']} \n").strip()
        desc = input(f"What's a brief descriptions of this task? {tasks[index]['description']} \n").strip()
        due = input(f"When is this task due (format: mm-dd-yy hh:mm:ss) {tasks[index]['due']} \n").strip()
    #if the code is out of bounds it will print the above statement    
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # """my ucid: vb437 and Date: 23/02/23"""
    update_task(index, name=name, description=desc, due=due)


def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    # find the task by index
    try:
        present_task = tasks[index]
        localValues = locals();
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index  
        local_dict = {old : localValues[old] for old in ('name', 'description', 'due')} 
        updated = False
    # update incoming task data if it's provided (if it's not provided use the original task property value)         
        for key, value in local_dict.items():
            if value != None and value != present_task[key]:
                updated = True
                present_task[key] = value
    # update lastActivity with the current datetime value
                present_task['lastActivity'] = datetime.now()
    # output that the task was updated if any items were changed, otherwise mention task was not updated
        if(updated):
            print("Task updated successfully!!!!.. .")
        else:
            print("you entered the same value again. so task has not been updated.")    
    #except Exception as e:
    except IndexError:
        print("The new task was rejected due to the following issue: \n", e) 
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    """my ucid: vb437 and Date: 24/02/23"""
    save()


def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    # find task from list by index
    try: 
        task = tasks[index] #assigned the enetered list of task in a variable named task 
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    except:
        print("The index that you entered doesnot exist") #if index is out of bound prints this statement
        return
   
    # if it is done, print a message saying it's already completed
    if task["done"]:
        print("You have already completed the task!!!...") # if we get input as done prints this message
     # if it's not done, record the current datetime as the value
    else:
        task["done"] = datetime.now() # when task is done just now, captured the time of now using datetime function.
        print("This task is marked as completed.")
    
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    """my ucid: vb437 and Date: 24/02/23"""
    save()

def view_task(index):
    """ View more info about a specific task fetch by index """
    # find task from list by index
    try: 
        task = tasks[index] #assigned the enetered list of task in a variable named task 
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    except:
        print("The index that you entered doesnot exist") #if index is out of bound prints this statement
        return
    # utilize the given print statement when a task is found
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    """my ucid: vb437 and Date: 24/02/23"""
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
    try: 
            del tasks[index]   # used del keyword to delete task from list by index
    # message should show if it was successful or not
            print("The requested task at index {index} has been deleted successfully!!!... . \n")
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    except IndexError:
        print("The index that you entered doesnot exist") #if index is out of bound prints this statement
        return
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    """my ucid: vb437 and Date: 24/02/23"""
    save()

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    _tasks = [] #placed a variable with empty list
    # generate a list of tasks where the task is not done
    for task in tasks:
        if task['done'] == False: # if the value of the key value of done is false then the task will be appended in the list
        # pass that list into list_tasks()
            _tasks.append(task) #
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    """my ucid: vb437 and Date: 24/02/23"""
    list_tasks(_tasks)

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    # generate a list of tasks where the due date is older than now and that are not complete
    _tasks = [] #placed a variable with empty list
    now = str_to_datetime(str(datetime.now().strftime("%m/%d/%y %H:%M:%S"))) #Used the necessary functions and formats for comparing with due date and present date.
    for task in tasks:
        if not task['done'] and str_to_datetime(task["due"]) < now: #If task done is true and task due is less than present time then the list will be appended in created empty _tasks list. 
    # pass that list into list_tasks()
            _tasks.append(task)
    list_tasks(_tasks)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    """my ucid: vb437 and Date: 24/02/23"""

def get_time_remaining(index):
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
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    """my ucid: vb437 and Date: 24/02/23"""
    #task = {}

# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
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



