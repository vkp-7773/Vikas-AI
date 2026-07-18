from modules.patterns import PATTERNS


def understand(user):

    user = user.lower().strip()

    # Remove common extra words
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

            text = user.replace(pattern, "").strip()

            if command == "create file":

                if "." not in text:
                    text += ".txt"

            return command + " " + text



    # Direct file commands

    if user.startswith("create file "):

        filename = user.replace("create file ", "")

        if "." not in filename:
            filename += ".txt"

        return "create file " + filename



    if user.startswith("copy file "):

        return user


    if user.startswith("move file "):

        return user


    if user.startswith("rename file "):

        return user


    if user.startswith("delete file "):

        return user


    if user.startswith("read file "):

        return user


    if user.startswith("write file "):

        return user



    # Search

    if "search" in user or "find" in user:

        words = user.split()

        for word in words:

            if word not in ["search", "find", "file"]:

                return "search file " + word



    # Folder

    if "folder" in user and "banao" in user:

        name = user.replace("folder banao", "").strip()

        return "create folder " + name



    # Notes

    if "note" in user:

        text = user.replace("note", "").strip()

        return "note " + text



    return user