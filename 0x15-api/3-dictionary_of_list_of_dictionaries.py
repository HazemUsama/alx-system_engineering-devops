#!/usr/bin/python3
"""Export data in the JSON format"""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    info = {}
    for user in users:
        todos = requests.get(url + "todos",
                             params={'userId': user.get('id')}).json()

        info['{}'.format(user.get('id'))] = [
            {
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': user.get('username')
            }
            for task in todos
        ]

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(info, json_file)
