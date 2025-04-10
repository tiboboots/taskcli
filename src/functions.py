import variables as var
import os
import json
import sys
from datetime import datetime

def quit_program():
    print("Exiting...")
    sys.exit()

def input_command(): # Ask user for a command, return command if command exists in crud_commands list or status_command variable
    while True:
        user_command = input("Command: ").lower()
        if user_command in var.crud_commands or user_command == var.status_command or user_command in var.list_tasks_commands:
            return user_command
        elif user_command == 'quit':
            quit_program()
        else:
            print("Invalid command, please try again.")
            continue

def input_id(user_command):
    if user_command in ['update', 'delete'] or user_command == var.status_command:
        while True:
            task_id = input("Task ID: ").lower()
            if task_id.isdigit():
                return int(task_id) # Convert task_id to integer for data type consistency when performing conditonal checks with id field in json dictionaries
            elif task_id == 'quit':
                quit_program()
            else:
                print("Invalid ID, must be a number. Try again.")
                continue
    
def input_task(user_command): # Ask user for a task if command is either update or add
    if user_command in ['update', 'add']:
        user_task = input("Task: ")
        if user_task == 'quit':
            quit_program()
        else:
            return user_task   
        
def input_status(task_id): # ask user for a new task status if task_id variable is valid
    if task_id is not None:
        task_status = input("Set task status: ")
        return task_status

def id_generator(json_data):
    """Get id from the id key in the latest dictionary element in json_data list if list is not empty, 
    and add 1 to it after each function call.
    Else if json_data list is empty, start at 0 and add 1 to the id for each function call.
      """
    if len(json_data) != 0:
        latest_id = json_data[-1]["id"]
        latest_id += 1
    else:
        latest_id = 0
        latest_id += 1
    return latest_id 

def intialize_file_if_empty(): # Check if file is empty, if true then intialize with empty list
    if os.path.getsize(var.file_path) == 0:
        with open(var.file_path, "w") as userdata:
            json.dump([], userdata)

def parse_status_from_command(user_command): # Parse the status from the user command and return it
    split_command = user_command.split()
    just_the_status = split_command.pop()
    return just_the_status

def check_id_validility(json_data, task_id): #Check if user specified id exists within json file
    if len(json_data) != 0:
        valid_id = False
        for dictionary in json_data:
            if dictionary['id'] == task_id:
                valid_id = True
                return valid_id
        else:
            return valid_id
    else:
        print("Json is empty.")
    
def updated_task_to_dictionary(json_data, task_id, user_task): #find task with matching id as user specified id, update task
    if len(json_data) != 0:
        for dictionary in json_data:
            if dictionary['id'] == task_id:
                dictionary['task'] = user_task
                dictionary["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                return
    else:
        print("Json is empty.")

def updated_status_to_dictionary(json_data, task_id, task_status):
    if len(json_data) == 0:
        return
    for dictionary in json_data:
        if dictionary["id"] == task_id:
            dictionary["status"] = task_status
            dictionary["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            break
    else:
        return
    
def append_new_task(json_data, user_task, latest_id): # adds new tasks to json_data list
    var.task_dictionary["task"] = user_task
    var.task_dictionary["id"] = latest_id
    var.task_dictionary["status"] = "to-do"
    var.task_dictionary['createdAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    json_data.append(var.task_dictionary)