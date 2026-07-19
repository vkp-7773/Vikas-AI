import json
import os

FILE_NAME = "data/knowledge.json"


def load_knowledge():

    if not os.path.exists(FILE_NAME):
        return {}

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except:
        return {}


def save_knowledge(question, answer):

    data = load_knowledge()

    data[question.lower().strip()] = answer.strip()

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def get_answer(question):

    data = load_knowledge()

    return data.get(question.lower().strip())


def all_knowledge():

    return load_knowledge()


def delete_knowledge(question):

    data = load_knowledge()

    question = question.lower().strip()

    if question in data:
        del data[question]

        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

        return True

    return False