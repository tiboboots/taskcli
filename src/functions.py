import variables as var
import os
import json
import sys
from datetime import datetime

def check_if_quit(user_input): # Check if user command is equal to quit, return True if it is, otherwise False
    if user_input == 'quit':
        print("Exiting...")
        sys.exit()

def input_command(): # Ask user for a command, return command if command exists in all_commands variable
    while True:
        user_command = input("Command: ").lower().strip()
        check_if_quit(user_command)
        if user_command not in var.all_commands:
            print(f"Invalid command, please try again. Command must be one of: {var.all_commands}")
            continue
        else:
            return user_command
        
def input_id(): # Ask user for id, check if id consists only of numbers, if not then loop back and prompt them again.
    while True:
        task_id = input("Task ID: ").lower().strip()
        check_if_quit(task_id) # Call check_if_quit function to check if input for id prompt is equal to quit, exit program if true
        if task_id.isdigit() == False:
            print("Invalid id, must be a number. Try again.")
            continue
        else:
            return int(task_id)
        
def input_task(): # Ask user for a task
    user_task = input("Task: ").strip()
    check_if_quit(user_task)
    return user_task   
        
def input_status(): # ask user for a new task status 
    while True:
        task_status = input("Set task status: ").strip()
        check_if_quit(task_status)
        if task_status not in var.different_statuses: # Prompt user again for status if status is not found in different_statuses
            print(f"Invalid status, must be one of {var.different_statuses}. Try again.")
            continue
        else:
            return task_status

def id_generator(json_data):
    if len(json_data) != 0: # If json is not empty, then take id of latest task and add 1 to it for new tasks
        latest_id = json_data[-1]["id"]
        latest_id += 1
        return latest_id
    else: # If json is empty, begin at 0 and add 1 to the id for every new task
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

def check_id_validility(json_data, task_id): # Check if user specified id exists within json file, return True if it does, else False
    if len(json_data) == 0:
        print("Json is empty")
        return
    valid_id = False
    for dictionary in json_data:
        if dictionary['id'] == task_id:
            valid_id = True
            break
    return valid_id
    
def updated_task_to_dictionary(json_data, task_id, user_task): # Find task with same matching id as user specified id, update task
    if len(json_data) == 0:
        print("Json is empty")
        return
    for dictionary in json_data:
        if dictionary['id'] == task_id:
            dictionary['task'] = user_task
            dictionary["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return
    else:
        return

def updated_status_to_dictionary(json_data, task_id, task_status): # Update a task's status
    if len(json_data) == 0:
        print("Json is empty")
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

def remove_task_from_list(json_data, task_id): # delete task from json_data list
    if len(json_data) == 0:
        print("Json is empty.")
        return
    for dictionary in json_data:
        if dictionary["id"] == task_id:
            json_data.remove(dictionary)
            break
    else:
        return
    
def match_task_by_status(json_data, just_the_status): # List all tasks that match user specified status
    if len(json_data) == 0:
        print("Json is empty")
        return
    flag_var = False
    for dictionary in json_data:
        if dictionary['status'] == just_the_status:
            print(f'ID: {dictionary['id']}, Task: {dictionary['task']}, Status: {dictionary['status']}')
            flag_var = True
    if flag_var == False:
        print("No tasks with that status exist.")
        return
    
def info_message():
    print(f'Welcome! Commands are: {", ".join(var.all_commands)}')
    print(f'Enter a command based on the action you want to perform. "quit" will exit the program.')
    print(f'For example, entering the command of "add" will allow you to add a new task.')
    print(f'Use the "info" command to display all commands if you forget some of them.')