#!/usr/bin/python3
"""
Gather employee data from API
"""

import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            id = int(sys.argv[1])
        except ValueError:
            print("Employee ID must be an integer.")
            sys.exit(1)

        user_response = requests.get(f'{REST_API}/users/{id}')
        if user_response.status_code != 200:
            print("Error: Employee not found.")
            sys.exit(1)

        user_data = user_response.json()
        emp_name = user_data.get('name')

        todos_response = requests.get(f'{REST_API}/todos?userId={id}')
        todos_data = todos_response.json()

        tasks = list(filter(lambda x: x.get('userId') == id, todos_data))
        completed_tasks = list(filter(lambda x: x.get('completed'), tasks))

        for task in completed_tasks:
            print(f'\t {task.get("title")}')
    else:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
