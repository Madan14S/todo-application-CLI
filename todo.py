"""Command-line interface for the To-Do app.

Usage:
    python todo.py add "Buy milk"
    python todo.py list
    python todo.py done 1
    python todo.py delete 1
"""

import argparse

import storage
import tasks


def build_parser():
    """Describe the commands our program understands."""
    parser = argparse.ArgumentParser(description="A simple To-Do list app.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # add "title"
    add_parser = subparsers.add_parser("add", help="add a new task")
    add_parser.add_argument("title", help="what you need to do")

    # list
    subparsers.add_parser("list", help="show all tasks")

    # done ID
    done_parser = subparsers.add_parser("done", help="mark a task as done")
    done_parser.add_argument("task_id", type=int, help="the task's ID number")

    # delete ID
    delete_parser = subparsers.add_parser("delete", help="delete a task")
    delete_parser.add_argument("task_id", type=int, help="the task's ID number")

    return parser


def show_tasks(task_list):
    """Print every task, one per line."""
    if len(task_list) == 0:
        print("No tasks yet. Add one with: python todo.py add \"Buy milk\"")
        return

    for task in task_list:
        if task["done"]:
            mark = "[x]"
        else:
            mark = "[ ]"
        print(f"{mark} {task['id']}. {task['title']}")


def main():
    """Read the command, run it, and save any changes."""
    parser = build_parser()
    args = parser.parse_args()

    task_list = storage.load_tasks()

    if args.command == "add":
        try:
            new_task = tasks.add_task(task_list, args.title)
        except ValueError as error:
            print(f"Error: {error}")
            return
        storage.save_tasks(task_list)
        print(f"Added task {new_task['id']}: {new_task['title']}")

    elif args.command == "list":
        show_tasks(tasks.get_all_tasks(task_list))

    elif args.command == "done":
        if tasks.complete_task(task_list, args.task_id):
            storage.save_tasks(task_list)
            print(f"Task {args.task_id} marked as done.")
        else:
            print(f"No task found with ID {args.task_id}.")

    elif args.command == "delete":
        if tasks.delete_task(task_list, args.task_id):
            storage.save_tasks(task_list)
            print(f"Task {args.task_id} deleted.")
        else:
            print(f"No task found with ID {args.task_id}.")


# Run main() only when this file is run directly (not when imported).
if __name__ == "__main__":
    main()
