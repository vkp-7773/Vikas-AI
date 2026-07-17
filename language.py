from modules.patterns import PATTERNS

def understand(user):

    user = user.lower().strip()

    # Remove extra words
    if user.startswith("bhai "):
        user = user.replace("bhai ", "", 1)

    if user.startswith("please "):
        user = user.replace("please ", "", 1)

    # Pattern Router
    for pattern, command in PATTERNS.items():

        if user.startswith(pattern):

            text = user.replace(pattern, "").strip()

            if command == "create file":

                if "." not in text:
                    text += ".txt"

            return command + " " + text

    # Auto .txt only for create file
    if user.startswith("create file "):

        filename = user.replace("create file ", "")

        if "." not in filename:
            filename += ".txt"

        return "create file " + filename

    return user