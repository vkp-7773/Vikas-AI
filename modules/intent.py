INTENTS = {
    "create file": "FILE_CREATE",
    "write file": "FILE_WRITE",
    "read file": "FILE_READ",
    "append file": "FILE_APPEND",
    "delete file": "FILE_DELETE",
    "rename file": "FILE_RENAME",
    "copy file": "FILE_COPY",
    "move file": "FILE_MOVE",
    "search file": "FILE_SEARCH",
    "file info": "FILE_INFO",
    "count files": "FILE_COUNT",

    "create folder": "FOLDER_CREATE",
    "delete folder": "FOLDER_DELETE",
    "list files": "FILE_LIST",
    "list folders": "FOLDER_LIST",

    "note": "NOTE_CREATE",
    "show notes": "NOTE_SHOW",

    "history": "HISTORY_SHOW",

    "learn": "KNOWLEDGE",
    "show knowledge": "KNOWLEDGE",
    "delete knowledge": "KNOWLEDGE",
    "knowledge count": "KNOWLEDGE",
    "todo": "TODO_ADD",
    "show todos": "TODO_SHOW",
    "delete todo": "TODO_DELETE",
    "clear todos": "TODO_CLEAR",
}


def detect_intent(command):

    command = command.lower().strip()

    for key, value in INTENTS.items():
        if command.startswith(key):
            return value

    return "UNKNOWN"