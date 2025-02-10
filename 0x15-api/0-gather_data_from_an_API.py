#!/usr/bin/python3
"""
Fetches TODO list progress for a given employee ID using a REST API.
"""
import requests
import sys

def get_employee_todo_progress(employee_id):
    """Fetch and display the TODO list progress of an employee."""
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = requests.get(url)
    if response.status_code != 200:
        print("Invalid employee ID")
        return

    employee = response.json()
    name = employee.get("name")

    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    todo_response = requests.get(todo_url)
    todos = todo_response.json()

    total_tasks = len(todos)
    done_tasks = [task.get("title") for task in todos if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(name, number_of_done_tasks, total_tasks))
    for task in done_tasks:
        print("\t {}".format(task))

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)
    
    get_employee_todo_progress(int(sys.argv[1]))

