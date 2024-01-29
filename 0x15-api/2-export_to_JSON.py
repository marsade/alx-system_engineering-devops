#!/usr/bin/python3
"""
    Uses the API to return information about an employee
    and exports it in json format
"""
import json
import requests
import sys


def employee_todo(emp_id):
    try:
        # Urls
        base_url = "https://jsonplaceholder.typicode.com"
        user_url = f"{base_url}/users/{emp_id}"
        todo_url = 'https://jsonplaceholder.typicode.com/users/{}/ \
        todos'.format(emp_id)

        # Request and process data
        user_response = requests.get(user_url)
        user_data = user_response.json()
        emp_usrname = user_data.get("username")
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        total_tasks = []
        updateUser = {}

        for data in todo_data:
            total_tasks.append(
                {
                    'tasks': data.get('title'),
                    "completed": data.get('completed'),
                    "username": emp_usrname,
                }
            )
        updateUser[emp_id] = total_tasks

        file_Json = emp_id + ".json"
        with open(file_Json, 'w') as f:
            json.dump(updateUser, f)

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = sys.argv[1]
    employee_todo(employee_id)
