#!/usr/bin/python3
""" Export API data to JSON """
import json
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    USER_ID = sys.argv[1]
    try:
        int(USER_ID)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    url_to_user = f'https://jsonplaceholder.typicode.com/users/{USER_ID}'
    res = requests.get(url_to_user)

    if res.status_code != 200:
        print("Error: Employee not found.")
        sys.exit(1)

    USERNAME = res.json().get('username')
    url_to_task = f'{url_to_user}/todos'
    res = requests.get(url_to_task)
    tasks = res.json()

    dict_data = {USER_ID: []}
    for task in tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        dict_data[USER_ID].append({
            "task": TASK_TITLE,
            "completed": TASK_COMPLETED_STATUS,
            "username": USERNAME
        })

    json_file_name = f'{USER_ID}.json'
    with open(json_file_name, 'w') as f:
        json.dump(dict_data, f, indent=4)

    print(f"Data for employee ID {USER_ID} has been written to {json_file_name}")
