"""Logic layer: the rules for adding, finding, completing and deleting tasks.

Each task is a dictionary like:
    {"id": 1, "title": "Buy milk", "done": False}

The functions here work on a list of such dictionaries.
They never read or write files (that is storage.py's job).
"""


def generate_id(tasks):
    """Return the next unused task ID (biggest existing ID + 1)."""
    if len(tasks) == 0:
        return 1

    biggest = 0
    for task in tasks:
        if task["id"] > biggest:
            biggest = task["id"]

    return biggest + 1


def add_task(tasks, title):
    """Create a new task, add it to the list, and return the new task."""
    title = title.strip()
    if title == "":
        raise ValueError("Task title cannot be empty.")

    new_task = {
        "id": generate_id(tasks),
        "title": title,
        "done": False,
    }
    tasks.append(new_task)
    return new_task


def find_task(tasks, task_id):
    """Return the task with this ID, or None if there is no such task."""
    for task in tasks:
        if task["id"] == task_id:
            return task

    return None


def complete_task(tasks, task_id):
    """Mark a task as done. Return True if it worked, False if not found."""
    task = find_task(tasks, task_id)
    if task is None:
        return False

    task["done"] = True
    return True


def delete_task(tasks, task_id):
    """Remove a task. Return True if it worked, False if not found."""
    task = find_task(tasks, task_id)
    if task is None:
        return False

    tasks.remove(task)
    return True


def get_all_tasks(tasks):
    """Return a copy of the task list, ready to be displayed."""
    return list(tasks)
