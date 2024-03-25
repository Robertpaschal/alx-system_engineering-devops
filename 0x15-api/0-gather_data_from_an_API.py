#!/usr/bin/python3

"""
This script retrieves information about an employee's TODO list progress
using a REST API.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieve and display the TODO list progress of an employee.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # URL of the API
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    # Sending a GET request to the API
    response = requests.get(url)
    
    # Checking if the request was successful
    if response.status_code == 200:
        todos = response.json()
        employee_name = todos[0].get('username')
        total_tasks = len(todos)
        done_tasks = [task for task in todos if task.get('completed')]
        num_done_tasks = len(done_tasks)
        
        # Printing employee TODO list progress
        print(f"Employee {employee_name} is done with tasks ({num_done_tasks}/{total_tasks}):")
        for task in done_tasks:
            print(f"\t{task.get('title')}")
    else:
        print(f"Failed to fetch data for employee {employee_id}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
