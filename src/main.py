import json
import sys
import os

crud_commands = ["add", "update", "delete", "list"]

task_dictionary = {"id": None, 
               "task": None, 
               "status": None, 
               "createdAt": None, 
               "updatedAt": None}

file_path = "userdata.json"

def intialize_file_if_empty(): # Check if file is empty, if true then intialize with empty list
    if os.path.getsize(file_path) == 0:
        with open(file_path, "w") as userdata:
            json.dump([], userdata)

def parse_user_input(user_input): # Parse command from input, return command and task as a string
    split_data = user_input.split(" ")
    for val in split_data:
        if val in crud_commands:
            parsed_command = split_data.pop(val)
            parsed_task = " ".join(split_data)
            return parsed_task, parsed_command
    else:
        print("Invalid. Please specify a valid command followed by an input task.")

def read_json(): # Get latest data from userdata.json file, save it to json_data variable as list
     with open(file_path, "r") as userdata:
        json_data = json.load(userdata)
        return json_data
     
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

if __name__ == "__main__": # Only run executable code if add_tasks.py is run directly
    print(f'Commands are {crud_commands}')
    print("Enter a command followed by your task, or type 'quit' to exit the program")
    print('For example: "add" buy groceries" will add "buy groceries" as a new task')

    while True:
        intialize_file_if_empty() # call function to check if json file is empty
        json_data = read_json() # Get latest data from json file and save it to json_data variable
        try:
            user_input = input(": ").lower()
            if user_input == 'quit': # check if user passed string of "quit" as value for input, exit program if true.
                print("Exiting...")
                sys.exit()
        except KeyboardInterrupt:
            print(" Aborting...")
            sys.exit()
        else:
            parsed_command = parse_user_input(user_input)[1] # Parse user_input to return command to parsed_command variable
            parsed_task = parse_user_input(user_input)[0]# Parse command from user_input and return string with user task, saved to parsed_input variable
            latest_id = id_generator(json_data) # Generate an id based on whether json_data list is empty or not.
            if parsed_task is not None # Check to see if parsed_input is not empty, if empty then don't write data to json file.
                add_task(parsed_task, json_data, latest_id) # If not empty, then we write dictionary with new data to json file.
                print(f'Task added successfully! Task ID is: {latest_id}')
                

          

            

        

            
        
        



