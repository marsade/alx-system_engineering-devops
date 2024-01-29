#!/usr/bin/python3
"""Uses the API to return information about an rmplo """
import csv
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

        # Export to CSV
        csv_file_path = f"{employee_id}.csv"
        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            # Write data rows
            for task in todo_data:
                csv_writer.writerow([employee_id, employee_name, str(
                    task["completed"]), task["title"]])

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = sys.argv[1]
    employee_todo(employee_id)
