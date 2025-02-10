#!/usr/bin/python3
"""Fetches and displays TODO list progress for employee ID using REST API."""
import requests
import sys


def fetch_todo_progress(employee_id):
    """Fetch and display the TODO list progress of an employee."""
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information
    user = requests.get(f"{url}users/{employee_id}").json()
    if not user:
        return

    # Fetch TODO list for the user
    todos = requests.get(f"{url}todos?userId={employee_id}").json()

    # Filter completed tasks
    completed_tasks = [task["title"] for task in todos if task["completed"]]

    # Display results
    print(f"Employee {user['name']} is done with tasks"
          f"({len(completed_tasks)}/{len(todos)}):")
    for task in completed_tasks:
        print(f"\t {task}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        sys.exit("Usage: ./0-gather_data_from_an_API.py <employee_id>")

    fetch_todo_progress(int(sys.argv[1]))
