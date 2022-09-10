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
    user = '{}users'.format(url)
    r = requests.get(user)
    users = r.json()
    all_dict = {}
    for user in users:
        r = requests.get(url + 'todos', params={'userId': user['id']})
        tasks = r.json()
        task_list = []
        for task in tasks:
            task_dict = {'username': user['username'],
                         'task': task.get('title'),
                         'completed': task.get('completed')}
            task_list.append(task_dict)
        all_dict['{}'.format(user['id'])] = task_list

    filename = 'todo_all_employees.json'

    with open(filename, mode='w') as file:
        json.dump(all_dict, file)
