import json
import sys
import os
from datetime import datetime
import variables as var
import functions as func
import crud_functions as crud

if __name__ == "__main__": # Only run executable code if add_tasks.py is run directly
   while True:
    print(f'Commands are {*var.crud_commands, var.status_command, *var.list_tasks_commands}')
    print("Enter a command followed by your task, or type 'quit' to exit the program")
    print('For example: "add" buy groceries" will add "buy groceries" as a new task')

    func.intialize_file_if_empty() # check if json file is empty, if true then add empty list to it
    json_data = crud.read_json() # read json file and check for new data, save data to json_data variable
    latest_id = func.id_generator(json_data) # Generate an id for each task based on whether json file is empty or not
    user_command = func.input_command() # ask user to specify a command, save valid command to user_command variable

    crud.perform_task(user_command) # Use perform_task function to run the proper crud function based on user specified command