#!/usr/bin/python3
""" Export API data to CSV """
import csv
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    user_id = sys.argv[1]
    
    try:
        user_id_int = int(user_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
    
    # Fetch user information
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error: Employee not found.")
        sys.exit(1)
    
    user_data = user_response.json()
    user_name = user_data.get('username')
    
    # Fetch user's TODO list
    todos_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    todos_response = requests.get(todos_url)
    todos = todos_response.json()
    
    # Write to CSV
    csv_file_name = f'{user_id}.csv'
    with open(csv_file_name, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            completed = task.get('completed')
            title_task = task.get('title')
            csv_writer.writerow([user_id, user_name, completed, title_task])
    
    print(f"Data for employee ID {user_id} has been written to {csv_file_name}")
