#!/usr/bin/python3
"""Export data in the JSON format"""
import requests
import json
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={'userId': sys.argv[1]}).json()

    info = {'{}'.format(user.get('id')): [
        {
            'title': task.get('title'),
            'completed': task.get('completed'),
            'username': user.get('username')
        }
        for task in todos
    ]}
    with open('{}.json'.format(sys.argv[1]), 'w') as json_file:
        json.dump(info, json_file)
