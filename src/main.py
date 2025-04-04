import json
import sys
import os
import variables as var
import functions as func
import crud_functions as crud

if __name__ == "__main__": # Only run executable code if add_tasks.py is run directly
    print(f'Commands are {var.crud_commands}')
    print("Enter a command followed by your task, or type 'quit' to exit the program")
    print('For example: "add" buy groceries" will add "buy groceries" as a new task')

    while True:
        func.intialize_file_if_empty() # call function to check if json file is empty
        json_data = crud.read_json() # Get latest data from json file and save it to json_data variable
        try:
            user_input = input(": ").lower()
            if user_input == 'quit': # check if user passed string of "quit" as value for input, exit program if true.
                print("Exiting...")
                sys.exit()
        except KeyboardInterrupt:
            print(" Aborting...")
            sys.exit()
        else:
            parsed_command = func.parse_user_input(user_input)[1] # Parse user_input to return command to parsed_command variable
            parsed_task = func.parse_user_input(user_input)[0]# Parse command from user_input and return string with user task, saved to parsed_input variable
            latest_id = func.id_generator(json_data) # Generate an id based on whether json_data list is empty or not.
            if parsed_task is not None and parsed_command == 'add': # Check to see if parsed_input is not empty, if empty then don't write data to json file.
                crud.add_task(parsed_task, json_data, latest_id) # If not empty, then we write dictionary with new data to json file.
                print(f'Task added successfully! Task ID is: {latest_id}')
