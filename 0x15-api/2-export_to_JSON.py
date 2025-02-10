#!/usr/bin/python3
"""Exports an employee's TODO list data to a JSON file."""
import json
import requests
import sys


def export_to_json(employee_id):
    """Fetch and save the TODO list of an employee in JSON format."""
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information
    user = requests.get(f"{url}users/{employee_id}").json()
    if not user:
        return

    # Fetch TODO list for the user
    todos = requests.get(f"{url}todos?userId={employee_id}").json()

    # Structure the JSON data
    json_data = {employee_id: [{
        "task": task["title"],
        "completed": task["completed"],
        "username": user["username"]
    } for task in todos]}

    # Define the JSON file name
    filename = f"{employee_id}.json"

    # Write data to JSON file
    with open(filename, "w") as file:
        json.dump(json_data, file)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        sys.exit("Usage: ./2-export_to_JSON.py <employee_id>")

    export_to_json(int(sys.argv[1]))
