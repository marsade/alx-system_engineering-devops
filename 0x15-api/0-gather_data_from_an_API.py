#!/usr/bin/python3
"""Uses the API to return information about a """
import requests
import sys


def employee_todo(emp_id):
    try:
        # Urls
        base_url = "https://jsonplaceholder.typicode.com"
        user_url = f"{base_url}/users/{emp_id}"
        todo_url = f"{base_url}/todos?userId={emp_id}"

        # Request and process data
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get("name")
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Counting completed tasks
        completed_tasks = [task for task in todo_data if task["completed"]]
        number_of_done_tasks = len(completed_tasks)
        total_number_of_tasks = len(todo_data)

        # Print tasks
        print("Employee {} is done with tasks ({}/{}):".format(
            employee_name, number_of_done_tasks, total_number_of_tasks))
        for task in completed_tasks:
            print("\t {}".format(task.get('title')))
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = sys.argv[1]
    employee_todo(employee_id)
