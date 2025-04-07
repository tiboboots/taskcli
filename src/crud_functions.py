import variables as var
import json

def read_json(): # Get latest data from userdata.json file, save it to json_data variable as list
     with open(var.file_path, "r") as userdata:
        json_data = json.load(userdata)
        return json_data

def add_task(user_task, json_data, latest_id): 
    var.task_dictionary["task"] = user_task
    var.task_dictionary["id"] = latest_id
    var.task_dictionary["status"] = "to-do"
    json_data.append(var.task_dictionary)
    with open(var.file_path, "w") as json_file:
        json.dump(json_data, json_file, indent = 4)
     

def update_task(task_id, json_data, user_task):
    if len(json_data) != 0:
        for dictionary in json_data:
            if dictionary["id"] == task_id:
                dictionary["task"] = user_task
                with open(var.file_path, "w") as json_file:
                    json.dump(json_data, json_file, indent = 4)
                    break                  
'''If json_data list is not empty, then iterate over each dictionary object, 
 match the user specified id the correct dictionary's id, and update that dictionaries task with the new user task.
'''

def update_status(json_data, task_status, task_id):
    if len(json_data) != 0:
        for dictionary in json_data:
            if dictionary["id"] == task_id:
                dictionary["status"] == task_status
                with open(var.file_path, "w") as json_file:
                    json.dump(json_data, json_file, indent = 4)
                    break

def delete_task(json_data, task_id):
    if len(json_data) != 0:
        for dictionary in json_data:
            if dictionary["id"] == task_id:
                json_data.remove(dictionary)
                with open(var.file_path, "w") as json_file:
                    json.dump(json_data, json_file, indent = 4)
                    break

def list_tasks(json_data):
    if len(json_data) != 0:
        for dictionary in json_data:
            print(f'Task ID: {dictionary['id']}, Task: {dictionary['task']}')


     
