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

def add_task(user_command, json_data, latest_id): # Update task_dictionary variable and it's keys to have the user specified task, generated id, and default status of 'to-do'
    if user_command == "add":
        user_task = func.input_task(user_command) # ask user to specify task to add, save task to user_task variable
        var.task_dictionary["task"] = user_task
        var.task_dictionary["id"] = latest_id
        var.task_dictionary["status"] = "to-do"
        var.task_dictionary['createdAt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        json_data.append(var.task_dictionary)
        with open(var.file_path, "w") as json_file:
            json.dump(json_data, json_file, indent = 4)
        print("Task successfully added!")
     

def update_task(task_id, json_data, user_task):
    if len(json_data) != 0:
        for dictionary in json_data:
            if dictionary["id"] == task_id:
                dictionary["task"] = user_task
                dictionary["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open(var.file_path, "w") as json_file:
                    json.dump(json_data, json_file, indent = 4)
                    break                  
'''If json_data list is not empty, then iterate over each dictionary object, 
 match the user specified id the correct dictionary's id, and update that dictionaries task with the new user task.
'''

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

            
     
