from modules.todo_handler import handle_todo
from modules.file_handler import handle_file
from modules.note_handler import handle_note
from modules.history_handler import handle_history


def execute(command, intent):

    # File & Folder
    if intent.startswith("FILE_") or intent.startswith("FOLDER_"):
        result = handle_file(command)
        if result is not None:
            return result

    # Notes
    if intent.startswith("NOTE_"):
        result = handle_note(command)
        if result is not None:
            return result

    # History
    if intent.startswith("HISTORY_"):
        result = handle_history(command)
        if result is not None:
            return result

    # Todo

    elif intent.startswith("TODO_"):
        result = handle_todo(command)

        if result is not None:
            return result

    return f"Unknown command.\nCommand: {command}\nIntent: {intent}"