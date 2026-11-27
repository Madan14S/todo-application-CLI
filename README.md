# To-Do CLI

A simple command-line To-Do list app written in Python. You type short commands in the terminal to add tasks, see your list, mark tasks as done, and delete tasks. Your tasks are saved in a file, so they are still there the next time you run the program.

## Features

- Add a new task
- List all tasks (with `[ ]` for not done and `[x]` for done)
- Mark a task as done
- Delete a task
- Tasks are saved automatically in `tasks.json`
- Friendly messages for mistakes (for example, an empty title or a wrong ID)
- Unit tests for the task logic
- No extra libraries needed (uses only Python's standard library)

## Project Structure

```
todo-app/
├── todo.py         # The command-line interface (the file you run)
├── tasks.py        # The rules: add, find, complete, delete tasks
├── storage.py      # Saves and loads tasks from tasks.json
├── test_tasks.py   # Unit tests for tasks.py
├── tasks.json      # Your saved tasks (created automatically)
└── README.md       # This file
```

The code is split into three layers so each file has one job:

- `todo.py` talks to the user.
- `tasks.py` decides what happens to tasks. It never touches files.
- `storage.py` reads and writes the file. It knows nothing about task rules.

## Requirements

- Python 3 (a recent version, such as 3.8 or newer)
- A terminal (Terminal on Mac, Command Prompt or PowerShell on Windows)

To check that Python is installed, run:

```
python3 --version
```

> On Windows, you may need to type `python` instead of `python3`.

## How to Run

1. Open your terminal.
2. Go to the project folder:

```
cd todo-app
```

3. Run the program with one of the four commands below:

```
python3 todo.py <command>
```

## Commands

### 1. `add` - add a new task

Put the task title in quotes.

```
python3 todo.py add "Buy milk"
```

Output:

```
Added task 1: Buy milk
```

### 2. `list` - show all tasks

```
python3 todo.py list
```

Output:

```
[ ] 1. Buy milk
[ ] 2. Study Python
```

If you have no tasks yet, you will see:

```
No tasks yet. Add one with: python todo.py add "Buy milk"
```

### 3. `done` - mark a task as done

Use the task's ID number (the number shown in `list`).

```
python3 todo.py done 1
```

Output:

```
Task 1 marked as done.
```

Now `list` shows:

```
[x] 1. Buy milk
[ ] 2. Study Python
```

### 4. `delete` - delete a task

```
python3 todo.py delete 2
```

Output:

```
Task 2 deleted.
```

### What if something goes wrong?

```
python3 todo.py add "   "
Error: Task title cannot be empty.

python3 todo.py done 99
No task found with ID 99.
```

### Need help?

```
python3 todo.py --help
```

## Example Session

```
$ python3 todo.py add "Buy milk"
Added task 1: Buy milk

$ python3 todo.py add "Study Python"
Added task 2: Study Python

$ python3 todo.py list
[ ] 1. Buy milk
[ ] 2. Study Python

$ python3 todo.py done 1
Task 1 marked as done.

$ python3 todo.py list
[x] 1. Buy milk
[ ] 2. Study Python

$ python3 todo.py delete 2
Task 2 deleted.

$ python3 todo.py list
[x] 1. Buy milk
```

## How to Run the Unit Tests

From the project folder, run:

```
python3 -m unittest test_tasks.py -v
```

Example output (all tests passing):

```
...
Ran 23 tests in 0.001s

OK
```

The tests only use small lists made inside the tests, so they never change your real `tasks.json` file.

## How Your Data Is Saved

Tasks are stored in `tasks.json` in the same folder as the code. Each task looks like this:

```json
{
  "id": 1,
  "title": "Buy milk",
  "done": false
}
```

You can delete `tasks.json` to start over with an empty list.
