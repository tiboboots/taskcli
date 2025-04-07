import variables as var
import os
import json
import sys

def quit_program():
    print("Exiting...")
    sys.exit()

def input_command():
    while True:
        user_command = input("Command: ").lower()
        if user_command in var.crud_commands or user_command == var.status_command:
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
    
def input_task(user_command):
    if user_command in ['update', 'add']:
        user_task = input("Task: ")
        if user_task == 'quit':
            quit_program()
        else:
            return user_task   
        
def input_status(task_id):
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





