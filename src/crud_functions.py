import variables as var
import json

def add_task(parsed_input, json_data, latest_id): 
    var.task_dictionary["task"] = parsed_input
    var.task_dictionary["id"] = latest_id
    json_data.append(var.task_dictionary)
    with open(var.file_path, "w") as json_file:
        json.dump(json_data, json_file, indent = 4)

def read_json(): # Get latest data from userdata.json file, save it to json_data variable as list
     with open(var.file_path, "r") as userdata:
        json_data = json.load(userdata)
        return json_data
     

     
