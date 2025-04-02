import json
import sys
import os

def intialize_file_if_empty(): # Check if file is empty, if true then intialize with empty list
    if os.path.getsize(file_path) == 0:
        with open(file_path, "w") as userdata:
            json.dump([], userdata)

def parse_user_input(user_input): # Parse command from input and return string containing user task
    split_data = user_input.split(" ")
    for val in split_data:
        if val in crud_commands:
            split_data.remove(val)
            task_string = " ".join(split_data)
            return task_string
    else:
        print("Invalid. Please specify a valid command followed by an input task.")

def read_json(): # Get latest data from userdata.json file, save it to json_data variable as list
     with open(file_path, "r") as userdata:
        json_data = json.load(userdata)
        return json_data

def task_to_json(parsed_task, json_data): 
    task_dictionary["task"] = parsed_task
    json_data.append(task_dictionary)
    with open(file_path, "w") as user_data:
        json.dump(json_data, user_data, indent = 4)
# Add user task to task key in dictionary, then append dictionary to json_data list and write changes to original file.

crud_commands = ["add", "update", "delete", "list"]

task_dictionary = {"id": None, 
               "task": None, 
               "status": None, 
               "createdAt": None, 
               "updatedAt": None}

print(f'Commands are {crud_commands}')
print("Enter a command followed by your task, or type 'quit' to exit the program")
print('For example: "add" buy groceries" will add "buy groceries" as a new task')

file_path = "userdata.json"

while True:
    intialize_file_if_empty() # call function to check if json file is empty
    json_data = read_json() # Get latest data from json file and save it to json_data variable
    try:
        user_input = input(":").lower()
        if user_input == 'quit': # check if user passed string of "quit" as value for input, exit program if true.
            print("Exiting...")
            sys.exit()
    except KeyboardInterrupt:
        print(" Aborting...")
        sys.exit()
    else:
        task_string = parse_user_input(user_input)# Parse command from user_input and return string with user task, saved to task_string variable.
        if task_string is not None: #Check to see if task_string is not empty, if empty then don't write data to json file.
            task_to_json(task_string, json_data) #If not empty, then we write dictionary with new user task to json file.

            
          

            

        

            
        
        



