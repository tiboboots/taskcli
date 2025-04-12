crud_commands = ["add", "update", "delete", "list"]

task_dictionary = {"id": None, 
               "task": None, 
               "status": None, 
               "createdAt": None, 
               "updatedAt": None}

file_path = "userdata.json"

status_command = "set"

different_statuses = ['to-do', 'in-progress', 'done']

list_tasks_commands = {'list to-do', 'list in-progress', 'list done'}

all_commands = {"add", "update", "delete", "list", "list to-do", "list in-progress", "list done", "set", "quit"}