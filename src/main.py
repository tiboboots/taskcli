import json
import sys
import os
import variables as var
import functions as func
import crud_functions as crud

if __name__ == "__main__": # Only run executable code if add_tasks.py is run directly
   while True:
    print(f'Commands are {*var.crud_commands, var.status_command}')
    print("Enter a command followed by your task, or type 'quit' to exit the program")
    print('For example: "add" buy groceries" will add "buy groceries" as a new task')

    func.intialize_file_if_empty() # check if json file is empty, if true then add empty list to it
    json_data = crud.read_json() # read json file and check for new data, save data to json_data variable
    latest_id = func.id_generator(json_data) # Generate an id for each task based on whether json file is empty or not
    user_command = func.input_command() # ask user to specify a command, save valid command to user_command variable

    if user_command == 'add':
      user_task = func.input_task(user_command) # ask user to specify task to add, save task to user_task variable
      crud.add_task(user_task, json_data, latest_id)# Use user_task, json_data, and latest_id variables to add task with id to file
      print("Task successfully added!")

    elif user_command == 'update':
      task_id = func.input_id(user_command) # ask user for id if command is update, save to task_id variable
      if task_id is not None: # check if task_id is not null, if true and it contains a valid id, then ask for new task below
        user_task = func.input_task(user_command)
        crud.update_task(task_id, json_data, user_task)
        print("Task updated successfully!")

    elif user_command == 'delete':
      task_id = func.input_id(user_command)
      if task_id is not None:
        crud.delete_task(json_data, task_id)
        print("Task successfully deleted!")

    elif user_command == 'list':
      crud.list_tasks(json_data)

            