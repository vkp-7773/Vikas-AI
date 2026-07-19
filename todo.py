import json
import os

FILE_NAME = "data/todos.json"


def load_todos():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_todos(todos):
    with open(FILE_NAME, "w") as file:
        json.dump(todos, file, indent=4)


def add_todo(task):
    todos = load_todos()
    todos.append(task)
    save_todos(todos)
    return "Todo add ho gaya. ✅"


def show_todos():
    todos = load_todos()

    if not todos:
        return "Koi todo nahi hai."

    result = "Todo List:\n"

    for i, task in enumerate(todos, start=1):
        result += f"{i}. {task}\n"

    return result


def delete_todo(index):
    todos = load_todos()

    if index < 1 or index > len(todos):
        return "Invalid todo number."

    todos.pop(index - 1)
    save_todos(todos)

    return "Todo delete ho gaya. ✅"


def clear_todos():
    save_todos([])
    return "Sabhi todos delete ho gaye. 🗑️"