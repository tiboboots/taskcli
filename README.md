# Task Tracker CLI Application

## About
This is a command-line task tracker/to-do application, which allows you to manage your tasks via your terminal.
You can add tasks, update them, delete them, and list them. 

The tasks are stored in a .json file, containing the following fields:
- id: The unique identifier for each task.
- task: The actual task.
- status: The status of the task, which can be one of the following: to-do, in-progress, or done.
- createdAt: The date and time when the task was first created and added.
- updatedAt: The date and time when the task was last updated.

Here is an example of the basic structure:
```json
[
    {
        "id": 1,
        "task": "buy food",
        "status": "in-progress",
        "createdAt": "2025-04-12 17:43:50",
        "updatedAt": "2025-04-12 17:44:47"
    },
    {
        "id": 2,
        "task": "buy water",
        "status": "to-do",
        "createdAt": "2025-04-12 17:44:11",
        "updatedAt": null
    }
]
```

## Requirements
You'll need to have Python installed to run the app, and git in order to clone the repo.

## Instructions
To get started, you can clone this repo locally: 

``` bash 
git clone https://github.com/tiboboots/taskcli.git
```

Then, run the main.py file containing the executable code for the program.
As mentioned before, you can add tasks, update them, delete them, and list them. 

This is done using the following commands:
- add: This adds and saves a task to the json file. All new tasks by default begin with a status of to-do, which you can update later.
- update: This will allow you to update an existing task with a new task, by specifying the task id.
- delete: This allows you to delete an existing task by specifying it's id.
- list: Allows you to view all of your existing tasks.
- list to-do, list in-progress, list done: All 3 of these commands can be used to filter tasks by their status when listing them.
- set: Can be used to set/update an existing tasks status.
- quit: Allows you to stop the program and exit it at any point.
- info: Let's you bring up all commands in case you forgot some of them.

## Example
``` bash
# add a task
Command: add
Task: buy food
Task added successfully!
# List all tasks
Command: list
Task: buy food, Task ID: 1, Task Status: to-do
Task: buy water, Task ID: 2, Task Status: in-progress
# List task by status
Command: list in-progress
Task: buy water, Task ID: 2, Task Status: in-progress
# Update an existing task
Command: update  
Task ID: 1
Task: buy monke
Task successfully updated!
# Update an existing task's status
Command: set
Task ID: 1
Set task status: done
Status updated successfully!
# Delete an existing task
Command: delete     
Task ID: 1
Task deleted successfully!
# Display all commands
Command: info
All commands: list to-do, list, update, set, quit, info, list in-progress, delete, add, list done
# Quit program
Command: quit
: Exiting...
/Users/name
```

## Project URL
The original inspiration for this project can be found here: https://roadmap.sh/projects/task-tracker