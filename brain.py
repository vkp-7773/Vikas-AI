from language import understand
from commands import execute_builtin
from modules.intent import detect_intent
from modules.executor import execute


def think(user_input):

    command = understand(user_input)

    print("Command :", command)

    # 1. Built-in Commands
    result = execute_builtin(command)

    if result is not None:
        return result

    # 2. File / Note / History
    intent = detect_intent(command)

    print("Intent  :", intent)

    result = execute(command, intent)

    if result is not None:
        return result

    # 3. Unknown
    return f"Unknown command.\nCommand: {command}\nIntent: {intent}"