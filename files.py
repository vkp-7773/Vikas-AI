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
def read_file(filename):
    path = os.path.join(FOLDER, filename)

    if not os.path.exists(path):
        return "File nahi mili."

    with open(path, "r") as file:
        return file.read()
def list_files():
    files = os.listdir(FOLDER)

    if not files:
        return "Koi file nahi hai."

    result = "Files:\n"

    for i, file in enumerate(files, start=1):
        result += f"{i}. {file}\n"

    return result
    return f"{filename} me text likh diya. ✅"
def delete_file(filename):
    path = os.path.join(FOLDER, filename)

    if not os.path.exists(path):
        return "File nahi mili."

    os.remove(path)

    return f"{filename} delete ho gayi. 🗑️"


def append_file(filename, text):
    path = os.path.join(FOLDER, filename)

    try:
        with open(path, "a") as file:
            file.write("\n" + text)

        return "File me new text add ho gaya."

    except:
        return "File nahi mili."