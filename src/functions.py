import variables as var
import os
import json

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

def parse_user_input(user_input): # Parse command from input, return command and task as a string
    split_data = user_input.split(" ")
    for val in split_data:
        if val in var.crud_commands:
            parsed_command = split_data.pop(val)
            parsed_task = " ".join(split_data)
            return parsed_task, parsed_command
        elif isinstance(val, int): # Check to see if item in split_data list is integer, if true then this is an id that we return
            parsed_id = val
            return parsed_id
    else:
        print("Invalid. Please specify a valid command followed by an input task.")

def intialize_file_if_empty(): # Check if file is empty, if true then intialize with empty list
    if os.path.getsize(var.file_path) == 0:
        with open(var.file_path, "w") as userdata:
            var.json.dump([], userdata)



