#!/usr/bin/python3
"""
    Uses the API to return information about an employee
    and exports it in json format
"""
import json
import requests
import sys


if __name__ == "__main__":
    try:
        users = requests.get("https://jsonplaceholder.typicode.com/users")
        users = users.json()
        todos = requests.get('https://jsonplaceholder.typicode.com/todos')
        todos = todos.json()
        todoAll = {}

        for user in users:
            taskList = []
            for task in todos:
                if task.get('userId') == user.get('id'):
                    taskDict = {"username": user.get('username'),
                                "task": task.get('title'),
                                "completed": task.get('completed')}
                    taskList.append(taskDict)
            todoAll[user.get('id')] = taskList

        with open('todo_all_employees.json', mode='w') as f:
            json.dump(todoAll, f)

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
