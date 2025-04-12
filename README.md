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

## Instructions
To get started, you can clone this repo locally, which already includes the necessary files and modules needed for the project to run.
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
