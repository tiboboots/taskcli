import main

def add_task(parsed_input, json_data, latest_id): 
    main.task_dictionary["task"] = parsed_input
    main.task_dictionary["id"] = latest_id
    json_data.append(main.task_dictionary)
    with open(main.file_path, "w") as json_file:
        main.json.dump(json_data, json_file, indent = 4)
# Add user task to task key in dictionary, then append dictionary to json_data list and write changes to original file.