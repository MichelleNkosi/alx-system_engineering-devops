#!/usr/bin/python3
"""
Fetches data from JSONPlaceholder API and saves in JSON format.
"""

import json
import requests


if __name__ == "__main__":
    # Base URL for JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch users
    users = requests.get(url + "users").json()

    # Dictionary to store all tasks per user
    all_tasks = {}

    # Loop through each user
    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")

        # Fetch tasks for the current user
        todos = requests.get(url + "todos", params={"userId": user_id}).json()

        # Store tasks in required format
        all_tasks[user_id] = [
            {"username": username, "task": task.get("title"),
                "completed": task.get("completed")}
            for task in todos
        ]

    # Write to JSON file
    with open("todo_all_employees.json", "w") as file:
        json.dump(all_tasks, file)
