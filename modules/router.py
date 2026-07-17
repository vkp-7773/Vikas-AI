def get_category(command):

    if command.startswith("create file"):
        return "file"

    if command.startswith("write file"):
        return "file"

    if command.startswith("read file"):
        return "file"

    if command.startswith("delete file"):
        return "file"

    if command.startswith("append file"):
        return "file"

    if command.startswith("create folder"):
        return "folder"

    if command.startswith("list folders"):
        return "folder"

    if command.startswith("delete folder"):
        return "folder"

    if command.startswith("note"):
        return "note"

    if command.startswith("show notes"):
        return "note"

    if command.startswith("delete note"):
        return "note"

    if command == "history":
        return "history"

    if command.startswith("rename file"):
        return "file"


    return "general"