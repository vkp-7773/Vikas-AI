import json
import os

FILE_NAME = "data/memory.json"


def load_memory():

    if not os.path.exists(FILE_NAME):
        return {}

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return {}


memory = load_memory()


def save(key, value):

    memory[key] = value

    with open(FILE_NAME, "w") as file:
        json.dump(memory, file, indent=4)


def load(key):

    return memory.get(key)


def clear():

    global memory

    memory = {}

    with open(FILE_NAME, "w") as file:
        json.dump(memory, file, indent=4)