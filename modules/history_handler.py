from history import show_history

def handle_history(command):

    if command == "history":
        return show_history()

    return None