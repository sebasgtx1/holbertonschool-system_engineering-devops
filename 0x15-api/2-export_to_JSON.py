#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to
export data in the JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users/{}'.format(url, sys.argv[1])
    r = requests.get(user)
    r_json = r.json()

    USER_ID = sys.argv[1]
    USERNAME = r_json.get('username')

    r = requests.get(url + 'todos', params={'userId': sys.argv[1]})

    tasks = r.json()
    task_list = []
    for task in tasks:
        task_dict = {'task': task.get('title'),
                     'completed': task.get('completed'),
                     'username': USERNAME}
        task_list.append(task_dict)

    task_dict = {'{}'.format(USER_ID): task_list}
    filename = '{}.json'.format(USER_ID)

    with open(filename, mode='w') as file:
        json.dump(task_dict, file)
