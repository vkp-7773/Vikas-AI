from modules.patterns import PATTERNS


def understand(user):

    user = user.lower().strip()

    # Common extra words remove
    remove_words = [
        "bhai ",
        "please ",
        "plz ",
        "mujhe ",
        "ek ",
    ]

    for word in remove_words:
        if user.startswith(word):
            user = user.replace(word, "", 1)

    # Pattern matching
    for pattern, command in PATTERNS.items():

        if user.startswith(pattern):

            text = user.replace(pattern, "").strip()

            if command == "create file":
                if text and "." not in text:
                    text += ".txt"

            return (command + " " + text).strip()

    # Direct commands
    direct_commands = [
        "create file",
        "write file",
        "read file",
        "delete file",
        "append file",
        "rename file",
        "copy file",
        "move file",
        "search file",
        "file info",
        "create folder",
        "delete folder",
        "list files",
        "list folders",
        "count files",
        "open folder",
        "show notes",
        "history",
    ]

    for cmd in direct_commands:
        if user.startswith(cmd):
            return user

    # Notes
    if user.startswith("note "):
        return user

    return user