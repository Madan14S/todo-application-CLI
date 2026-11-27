"""Storage layer: saves tasks to a JSON file and loads them back.

This file only knows about reading and writing the file.
It knows nothing about adding or deleting tasks.
"""

import json
import os

# Build the path to tasks.json so it always sits next to this file,
# no matter which folder you run the program from.
FOLDER = os.path.dirname(os.path.abspath(__file__))
TASKS_FILE = os.path.join(FOLDER, "tasks.json")


def load_tasks(filename=TASKS_FILE):
    """Read tasks from the JSON file and return them as a list.

    If the file does not exist yet, or is empty/damaged,
    return an empty list instead of crashing.
    """
    try:
        with open(filename, "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        # First run: nothing has been saved yet.
        return []
    except json.JSONDecodeError:
        # The file exists but its content is not valid JSON.
        return []

    return tasks


def save_tasks(tasks, filename=TASKS_FILE):
    """Write the list of tasks to the JSON file (replacing old content)."""
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=2)
