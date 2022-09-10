#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export
data in the CSV format.

Requirements:

Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""
import csv
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
        task_list.append([USER_ID,
                         USERNAME,
                         task.get('completed'),
                         task.get('title')])

    filename = '{}.csv'.format(USER_ID)

    with open(filename, mode='w') as file:
        csv_writer = csv.writer(file, delimiter=',',
                                quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for task in task_list:
            csv_writer.writerow(task)
