import variables as var
import json

def read_json(): # Get latest data from userdata.json file, save it to json_data variable as list
     with open(var.file_path, "r") as userdata:
        json_data = json.load(userdata)
        return json_data

def add_task(user_task, json_data, latest_id): 
    var.task_dictionary["task"] = user_task
    var.task_dictionary["id"] = latest_id
    json_data.append(var.task_dictionary)
    with open(var.file_path, "w") as json_file:
        json.dump(json_data, json_file, indent = 4)
     

     
