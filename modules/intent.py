INTENTS = {
    # Files
    "create file": "FILE_CREATE",
    "write file": "FILE_WRITE",
    "read file": "FILE_READ",
    "list files": "FILE_LIST",
    "delete file": "FILE_DELETE",
    "append file": "FILE_APPEND",
    "rename file": "FILE_RENAME",
    "copy file": "FILE_COPY",
    "move file": "FILE_MOVE",
    "search file": "FILE_SEARCH",
    "file info": "FILE_INFO",
    "count files": "FILE_COUNT",
    "open folder": "FILE_OPEN_FOLDER",

    # Folders
    "create folder": "FOLDER_CREATE",
    "list folders": "FOLDER_LIST",
    "delete folder": "FOLDER_DELETE",

    # Notes
    "note": "NOTE_CREATE",
    "show notes": "NOTE_SHOW",
    "delete note": "NOTE_DELETE",

    # History
    "history": "HISTORY_SHOW",
}


def detect_intent(command):

    command = command.lower().strip()

    for key, value in INTENTS.items():
        if command.startswith(key):
            return value

    return "UNKNOWN"