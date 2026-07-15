import json
import os

FILE_NAME = "data/history.json"

def load_history():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_history(command):
    history = load_history()
    history.append(command)

    with open(FILE_NAME, "w") as file:
        json.dump(history, file, indent=4)


def show_history():
    history = load_history()

    if not history:
        return "History khali hai."

    result = "Command History:\n"

    for i, command in enumerate(history, start=1):
        result += f"{i}. {command}\n"

    return result