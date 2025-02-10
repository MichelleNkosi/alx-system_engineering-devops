#!/usr/bin/python3
"""Exports an employee's TODO list data to a CSV file."""
import csv
import requests
import sys


def export_to_csv(employee_id):
    """Fetch and save the TODO list of an employee in CSV format."""
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information
    user = requests.get(f"{url}users/{employee_id}").json()
    if not user:
        return

    # Fetch TODO list for the user
    todos = requests.get(f"{url}todos?userId={employee_id}").json()

    # Define the CSV file name
    filename = f"{employee_id}.csv"

    # Write data to CSV file
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, user["username"],
                             task["completed"], task["title"]])


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        sys.exit("Usage: ./1-export_to_CSV.py <employee_id>")

    export_to_csv(int(sys.argv[1]))
