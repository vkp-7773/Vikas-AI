from notes import save_note, show_notes, delete_note

def handle_note(command):

    if command.startswith("note "):
        text = command.replace("note ", "")
        save_note(text)
        return "Note save ho gaya. ✅"

    elif command == "show notes":
        return show_notes()

    elif command.startswith("delete note "):
        try:
            number = int(command.replace("delete note ", ""))
            return delete_note(number)
        except:
            return "Sahi note number likho."

    return None