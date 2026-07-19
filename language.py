from modules.patterns import PATTERNS


def understand(user):

    user = user.lower().strip()

    # Remove extra words
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

    # Pattern Matching
    for pattern, command in PATTERNS.items():

        if user.startswith(pattern):

            text = user[len(pattern):].strip()

            # Built-in commands
            if command in [
                "hello",
                "hi",
                "hey",
                "how are you",
                "good morning",
                "good night",
                "thanks",
                "time",
                "date",
                "help",
                "joke",
                "quote",
                "motivate me",
                "what is my name",
                "list files",
                "list folders",
                "count files",
                "history",
                "show notes",
                "open folder",
            ]:
                return command

            # Memory
            if command == "my name is":
                return "my name is " + text

            # Create file
            if command == "create file":
                if text and "." not in text:
                    text += ".txt"

            if text:
                return command + " " + text

            return command

    # Direct commands
    direct = (
        "create file ",
        "write file ",
        "read file ",
        "delete file ",
        "rename file ",
        "copy file ",
        "move file ",
        "search file ",
        "file info ",
        "create folder ",
        "delete folder ",
        "delete note ",
    )

    if user.startswith(direct):
        return user

    # Calculator expression
    operators = "+-*/%"
    if any(op in user for op in operators):
        return user

    return user