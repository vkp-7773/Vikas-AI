import shutil
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
def rename_file(old_name, new_name):

    old_path = os.path.join(FOLDER, old_name)
    new_path = os.path.join(FOLDER, new_name)

    if not os.path.exists(old_path):
        return "Purani file nahi mili."

    if os.path.exists(new_path):
        return "Nayi file pehle se maujood hai."

    os.rename(old_path, new_path)

    return f"{old_name} ka naam {new_name} kar diya. ✅"
    
    
def search_file(keyword):

    files = os.listdir(FOLDER)

    result = []

    for file in files:
        if keyword.lower() in file.lower():
            result.append(file)

    if not result:
        return "Koi file nahi mili."

    output = "Search Result:\n"

    for i, file in enumerate(result, start=1):
        output += f"{i}. {file}\n"

    return output







def copy_file(old_name, new_name):

    old_path = os.path.join(FOLDER, old_name)
    new_path = os.path.join(FOLDER, new_name)

    if not os.path.exists(old_path):
        return "Source file nahi mili."

    if os.path.exists(new_path):
        return "Destination file pehle se maujood hai."

    shutil.copy(old_path, new_path)

    return f"{old_name} copy hokar {new_name} ban gayi. ✅"


def move_file(old_name, new_name):

    old_path = os.path.join(FOLDER, old_name)
    new_path = os.path.join(FOLDER, new_name)

    if not os.path.exists(old_path):
        return "File nahi mili."

    shutil.move(old_path, new_path)

    return f"{old_name} move hokar {new_name} ban gayi. ✅"


def file_info(filename):

    path = os.path.join(FOLDER, filename)

    if not os.path.exists(path):
        return "File nahi mili."

    size = os.path.getsize(path)

    return (
        f"File : {filename}\n"
        f"Size : {size} Bytes"
    )


def count_files():

    files = [
        f for f in os.listdir(FOLDER)
        if os.path.isfile(os.path.join(FOLDER, f))
    ]

    return f"Total Files : {len(files)}"


def open_folder():

    files = os.listdir(FOLDER)

    if not files:
        return "Folder khali hai."

    output = "Folder Content:\n"

    for i, file in enumerate(files, start=1):
        output += f"{i}. {file}\n"

    return output
  