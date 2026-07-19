import json
import os

FILE_NAME = "data/reminders.json"


def load_reminders():

    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_reminders(reminders):

    with open(FILE_NAME, "w") as file:
        json.dump(reminders, file, indent=4)


def add_reminder(text):

    reminders = load_reminders()

    reminders.append(text)

    save_reminders(reminders)

    return "Reminder save ho gaya. ⏰"


def show_reminders():

    reminders = load_reminders()

    if not reminders:
        return "Koi reminder nahi hai."

    result = "REMINDERS\n\n"

    for i, item in enumerate(reminders, start=1):
        result += f"{i}. {item}\n"

    return result


def delete_reminder(number):

    reminders = load_reminders()

    if number < 1 or number > len(reminders):
        return "Invalid reminder number."

    reminders.pop(number - 1)

    save_reminders(reminders)

    return "Reminder delete ho gaya. ✅"