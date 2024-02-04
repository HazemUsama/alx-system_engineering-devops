#!/usr/bin/python3
"""Display to-do list given employee ID"""
import requests
import sys
import csv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={'userId': sys.argv[1]}).json()

    info = [{'id': user.get('id'),
             'username': user.get('username'),
             'status': task.get('completed'),
             'title': task.get('title')} for task in todos]

    with open("{}.csv".format(sys.argv[1]), 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=info[0].keys())

        writer.writerows(info)
