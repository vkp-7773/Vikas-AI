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
    
def create_folder(foldername):
    path = os.path.join(FOLDER, foldername)

    if os.path.exists(path):
        return "Folder pehle se maujood hai."

    os.mkdir(path)

    return f"{foldername} folder create ho gaya. 📁"



def list_folders():
    items = os.listdir(FOLDER)

    folders = []

    for item in items:
        path = os.path.join(FOLDER, item)

        if os.path.isdir(path):
            folders.append(item)

    if not folders:
        return "Koi folder nahi hai."

    result = "Folders:\n"

    for i, folder in enumerate(folders, start=1):
        result += f"{i}. {folder}\n"

    return result
    
    
    
def delete_folder(foldername):
    path = os.path.join(FOLDER, foldername)

    if not os.path.exists(path):
        return "Folder nahi mila."

    if not os.path.isdir(path):
        return "Ye folder nahi hai."

    if os.listdir(path):
        return "Folder khaali nahi hai."

    os.rmdir(path)

    return f"{foldername} folder delete ho gaya. 🗑️"
  