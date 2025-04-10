import variables as var
import json
from datetime import datetime
import functions as func

def read_json(): # Get latest data from userdata.json file, save it to json_data variable as list
     with open(var.file_path, "r") as userdata:
        json_data = json.load(userdata)
        return json_data
     
def write_json(json_data):
    with open(var.file_path, "w") as json_file:
        json.dump(json_data, json_file, indent = 4)

def add_task(user_command): # Add new tasks to json_data list, write list back to json file with new tasks
    if user_command == "add":
        json_data = read_json()
        latest_id = func.id_generator(json_data)
        user_task = func.input_task(user_command) 
        func.append_new_task(json_data, user_task, latest_id)
        write_json(json_data)
        print("Task added successfully!")
        return
    else:
        return
     
def update_task(user_command):
    if user_command == 'update':
        json_data = read_json() # Get fresh data from json file
        task_id = func.input_id(user_command) # ask user for id if command is update, save to task_id variable
        valid_id = func.check_id_validility(json_data, task_id) # Check if id exists within json file's data
    else:
        return
    if valid_id == True: 
        user_task = func.input_task(user_command) # If id exists, then we ask user for the new task
        func.updated_task_to_dictionary(json_data, task_id, user_task) # add new task to matching dictionary in json_data list
        write_json(json_data) # Write updated json_data list with new task back to json file
        print("Task successfully updated!")
        return
    else: 
        print("No tasks with that id exist.")
        return

def update_status(json_data, task_status, task_id): # Update an existing task's status if user specified id exists within json_data
    if len(json_data) != 0:
        for dictionary in json_data:
            if dictionary["id"] == task_id:
                dictionary["status"] = task_status
                dictionary["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open(var.file_path, "w") as json_file:
                    json.dump(json_data, json_file, indent = 4)
                    break

def delete_task(json_data, task_id): # Delete task if json_data list is not empty and user specified task_id is found in list
    if len(json_data) != 0:
        for dictionary in json_data:
            if dictionary["id"] == task_id:
                json_data.remove(dictionary)
                with open(var.file_path, "w") as json_file:
                    json.dump(json_data, json_file, indent = 4)
                    break

def list_all_tasks(json_data):# List all existing tasks if json_data list is not empty
    if len(json_data) != 0:
        for dictionary in json_data:
            print(f'Task: {dictionary['task']}, Task ID: {dictionary['id']}, Task Status: {dictionary['status']}')

def list_tasks_by_status(json_data, just_the_status): #List tasks by their status, use flag variable to determine whether task with specified status exists or not.
    if len(json_data) != 0:
        flag_var = False
        for dictionary in json_data:
            if dictionary['status'] == just_the_status:
                print(f'ID: {dictionary['id']}, Task: {dictionary['task']}, Status: {dictionary['status']}')
                flag_var = True #If any task with specified status exists, then set flag_var to be True.
        if flag_var == False: #If flag_var variable equals False after loop, then no tasks matching specified status exist.
            print("No tasks with that status exist.")
