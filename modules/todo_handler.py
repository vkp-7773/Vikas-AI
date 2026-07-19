from todo import add_todo, show_todos, delete_todo, clear_todos


def handle_todo(command):

    if command.startswith("todo "):
        task = command.replace("todo ", "")
        return add_todo(task)

    elif command == "show todos":
        return show_todos()

    elif command.startswith("delete todo "):
        try:
            number = int(command.replace("delete todo ", ""))
            return delete_todo(number)
        except:
            return "Sahi todo number likho."

    elif command == "clear todos":
        return clear_todos()

    return None