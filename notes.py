import json
import os

FILE_NAME = "data/notes.json"

def load_notes():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_note(note):
    notes = load_notes()
    notes.append(note)

    with open(FILE_NAME, "w") as file:
        json.dump(notes, file, indent=4)

def show_notes():
    notes = load_notes()

    if not notes:
        return "Koi note nahi hai."

    result = ""
    for i, note in enumerate(notes, start=1):
        result += f"{i}. {note}\n"

    return result