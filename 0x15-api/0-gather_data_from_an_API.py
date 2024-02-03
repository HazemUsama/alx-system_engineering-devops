#!/usr/bin/python3
"""Display to-do list given employee ID"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={'userId': sys.argv[1]}).json()
    done_tasks = len([task for task in todos if task.get('completed')])
    print('Employee {} is done with tasks({}/{}):'.format(user.get('name'),
                                                          done_tasks,
                                                          len(todos)))
    for task in todos:
        if task.get('completed'):
            print('\t {}'.format(task.get('title')))
