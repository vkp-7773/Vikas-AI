import os

FOLDER = "data/files"

def create_file(filename):
    path = os.path.join(FOLDER, filename)

    if os.path.exists(path):
        return "File pehle se maujood hai."

    with open(path, "w") as file:
        file.write("")

    return f"{filename} create ho gayi. ✅" 
def write_file(filename, text):
    path = os.path.join(FOLDER, filename)

    if not os.path.exists(path):
        return "File nahi mili."

    with open(path, "w") as file:
        file.write(text)

    return f"{filename} me text likh diya. ✅"