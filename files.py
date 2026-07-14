import os

FOLDER = "data/files"

def create_file(filename):
    path = os.path.join(FOLDER, filename)

    if os.path.exists(path):
        return "File pehle se maujood hai."

    with open(path, "w") as file:
        file.write("")

    return f"{filename} create ho gayi. ✅"