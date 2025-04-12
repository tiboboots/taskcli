import variables as var
import json
import functions as func

def read_json(): # Get latest data from userdata.json file, save it to json_data variable as list
     with open(var.file_path, "r") as userdata:
        json_data = json.load(userdata)
        return json_data
     
def write_json(json_data):
    with open(var.file_path, "w") as json_file:
        json.dump(json_data, json_file, indent = 4)

def add_task(user_command): # Add new tasks to json_data list, write list back to json file with new tasks
    if user_command != var.add_command:
        return
    json_data = read_json() # If command is not quit, thus add, then begin add task process
    latest_id = func.id_generator(json_data)
    user_task = func.input_task()
    func.append_new_task(json_data, user_task, latest_id)
    write_json(json_data)
    print("Task added successfully!")
    return
     
def update_task(user_command):
    if user_command != var.update_command:
        return
    json_data = read_json()
    task_id = func.input_id() # ask user for id if command is update, save to task_id variable
    func.check_if_quit(task_id)
    valid_id = func.check_id_validility(json_data, task_id)  # Check if id exists within json file's data
    if valid_id == False:
        print("No tasks with that id exist.")
        return
    user_task = func.input_task() 
    func.check_if_quit(user_task)
    func.updated_task_to_dictionary(json_data, task_id, user_task) # add new task to matching dictionary in json_data list
    write_json(json_data) # Write updated json_data list with new task back to json file
    print("Task successfully updated!")
    return

def set_status(user_command): # Update an existing task's status, if id exists and command is equal to status_command variable
   if user_command != var.set_status_command:
       return
   json_data = read_json()
   task_id = func.input_id()
   valid_id = func.check_id_validility(json_data, task_id)
   if valid_id == False:
       print("No tasks with that id exist.")
       return
   task_status = func.input_status()
   func.updated_status_to_dictionary(json_data, task_id, task_status)
   write_json(json_data)
   print("Status updated successfully!")

def delete_task(user_command): # Delete task from json file if command is equal to "delete" and id is found in json_data list
    if user_command != var.delete_command:
        return
    json_data = read_json()
    task_id = func.input_id()
    valid_id = func.check_id_validility(json_data, task_id)
    if valid_id == False:
        print("No tasks with that id exist.")
        return
    func.remove_task_from_list(json_data, task_id)
    write_json(json_data)
    print("Task deleted successfully!")
    return

def list_all_tasks(user_command):# List all existing tasks if command equals "list" and json_data list is not empty
    if user_command != var.list_command:
        return
    json_data = read_json()
    if len(json_data) == 0:
        return
    for dictionary in json_data:
        print(f'Task: {dictionary['task']}, Task ID: {dictionary['id']}, Task Status: {dictionary['status']}')

def list_tasks_by_status(user_command): # List tasks based on user specified status
    if user_command not in var.list_tasks_commands:
        return
    json_data = read_json()
    just_the_status = func.parse_status_from_command(user_command)
    func.match_task_by_status(json_data, just_the_status) # Use match_task function to find and list any tasks with user specified status

command_dictionary = {var.add_command: add_task, # dictionary containing all functions that map to a single command, so no filter commands
                      var.update_command: update_task,
                      var.delete_command: delete_task,
                      var.set_status_command: set_status,
                      var.list_command: list_all_tasks}

def perform_task(user_command): # Centralized function to run proper function based on user command, using command_dictionary
    if user_command in var.list_tasks_commands:
        list_tasks_by_status(user_command) # Call list_tasks_by_status function if user_command is in the list_tasks_commands variable
        return # Exit function and don't execute any code below, if condition is True
    task_function = command_dictionary.get(user_command) # Use .get() method to return function/value from command_dictionary based on user command
    task_function(user_command) # Call returned function, for example, if user_command is 'add', then task_function = add_task() function
    return
