add_command = 'add'
update_command = 'update'
delete_command = 'delete'
list_command = 'list'
set_status_command = "set"
info_command = "info"

task_dictionary = {"id": None, 
               "task": None, 
               "status": None, 
               "createdAt": None, 
               "updatedAt": None}

file_path = "userdata.json"

different_statuses = ['to-do', 'in-progress', 'done']

list_tasks_commands = {'list to-do', 'list in-progress', 'list done'}

all_commands = {"add", "update", "delete", "list", "list to-do", "list in-progress", "list done", "set", "quit", "info"}