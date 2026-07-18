from language import understand
from modules.intent import detect_intent
from modules.executor import execute


def think(user_input):

    command = understand(user_input)

    intent = detect_intent(command)

    print("Command :", command)
    print("Intent  :", intent)

    result = execute(command, intent)

    return result