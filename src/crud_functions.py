import variables as var
import json
from datetime import datetime
import functions as func
import sys

def read_json(): # Get latest data from userdata.json file, save it to json_data variable as list
     with open(var.file_path, "r") as userdata:
        json_data = json.load(userdata)
        return json_data
     
def write_json(json_data):
    with open(var.file_path, "w") as json_file:
        json.dump(json_data, json_file, indent = 4)

def add_task(user_command): # Add new tasks to json_data list, write list back to json file with new tasks
    if user_command != "add" or user_command != 'quit': # If command is not add or quit, then exit function
        return
    quit_status = func.check_if_quit(user_command)
    if quit_status == True: # If command is quit, then use sys.exit to quit program gracefully
        print("Exiting...")
        sys.exit()
    json_data = read_json() # If command is not quit, thus add, then begin add task process
    latest_id = func.id_generator(json_data)
    user_task = func.input_task(user_command) 
    func.append_new_task(json_data, user_task, latest_id)
    write_json(json_data)
    print("Task added successfully!")
    return
     
def update_task(user_command):
    if user_command != 'update':
        return
    json_data = read_json() # Get fresh data from json file
    task_id = func.input_id(user_command) # ask user for id if command is update, save to task_id variable
    valid_id = func.check_id_validility(json_data, task_id)  # Check if id exists within json file's data
    if valid_id == False:
        print("No tasks with that id exist.")
        return
    user_task = func.input_task(user_command) # If id exists, then we ask user for the new task
    func.updated_task_to_dictionary(json_data, task_id, user_task) # add new task to matching dictionary in json_data list
    write_json(json_data) # Write updated json_data list with new task back to json file
    print("Task successfully updated!")
    return

def set_status(user_command): # Update an existing task's status, if id exists and command is equal to status_command variable
   if user_command != var.status_command:
       return
   json_data = read_json()
   task_id = func.input_id(user_command)
   valid_id = func.check_id_validility(json_data, task_id)
   if valid_id == False:
       print("No tasks with that id exist.")
       return
   task_status = func.input_status()
   func.updated_status_to_dictionary(json_data, task_id, task_status)
   write_json(json_data)
   print("Status updated successfully!")

def delete_task(user_command): # Delete task from json file if command is equal to "delete" and id is found in json_data list
    if user_command != 'delete':
        return
    json_data = read_json()
    task_id = func.input_id(user_command)
    valid_id = func.check_id_validility(json_data, task_id)
    if valid_id == False:
        print("No tasks with that id exist.")
        return
    func.remove_task_from_list(json_data, task_id)
    write_json(json_data)
    print("Task deleted successfully!")
    return

def list_all_tasks(user_command):# List all existing tasks if command equals "list" and json_data list is not empty
    if user_command != 'list':
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
