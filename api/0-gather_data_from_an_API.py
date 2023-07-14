#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import requests
import sys

EMPLOYEE_ID = int(sys.argv[1])

# API endpoint
url = 'https://jsonplaceholder.typicode.com/users/{id}'.format(id=EMPLOYEE_ID)

# Retrieve employee information
response = requests.get(url)
employee_data = response.json()

# Get employee name
employee_name = employee_data['name']

# API endpoint for employee's TODO list
todos_url = 'https://jsonplaceholder.typicode.com/todos?userId={id}'.format(id=EMPLOYEE_ID)

# Retrieve employee's TODO list
todos_response = requests.get(todos_url)
todos_data = todos_response.json()

# Count the number of completed tasks
completed_tasks = [todo for todo in todos_data if todo['completed']]
number_of_done_tasks = len(completed_tasks)

# Count the total number of tasks
total_number_of_tasks = len(todos_data)

# Display employee's TODO list progress
print("Employee {name} is done with tasks ({done}/{total}):".format(
    name=employee_name,
    done=number_of_done_tasks,
    total=total_number_of_tasks
))

# Display the title of completed tasks
for task in completed_tasks:
    print("\t", task['title'])
