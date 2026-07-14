import json
import os

FILE_NAME = "data/memory.json"

def load_memory():

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return {}

memory = load_memory()


def save(key, value):

    memory[key] = value

    with open(FILE_NAME, "w") as file:
        json.dump(memory, file)


def load(key):

    return memory.get(key, None)