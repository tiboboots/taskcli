import variables as var
import functions as func
import crud_functions as crud

func.info_message()

if __name__ == "__main__": # Only run executable code if add_tasks.py is run directly
   while True:
    func.intialize_file_if_empty() # check if json file is empty, if true then add empty list to it
    user_command = func.input_command() # ask user to specify a command, save valid command to user_command variable

    crud.perform_task(user_command) # Use perform_task function to run the proper crud function based on user specified command