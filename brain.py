from files import create_file
from tools import get_time, get_date
from memory import save, load
from commands import show_help
from notes import save_note, show_notes, delete_note

from datetime import datetime

def think(user):

    if user.startswith("my name is "):
        name = user.replace("my name is ", "")
        save("name", name)
        return f"Nice to meet you {name} ❤️"

    elif user == "what is my name":
        name = load("name")

        if name:
            return f"Your name is {name} 😊"
        else:
            return "Mujhe abhi tumhara naam nahi pata."

    elif user == "hello":
        return "Radhe Radhe Vikas ❤️"

    elif user == "bye":
        return "Fir milenge 😊"

    elif user == "python":
        return "Python ek powerful programming language hai."

    elif "+" in user:
        try:
            a, b = user.split("+")
            return str(float(a) + float(b))
        except:
            return "Galat format. Example: 25+75"

    elif "-" in user:
        try:
            a, b = user.split("-")
            return str(float(a) - float(b))
        except:
            return "Galat format. Example: 100-25"

    elif "*" in user:
        try:
            a, b = user.split("*")
            return str(float(a) * float(b))
        except:
            return "Galat format. Example: 25*4"

    elif "/" in user:
        try:
            a, b = user.split("/")

            if float(b) == 0:
                return "0 se divide nahi kar sakte."

            return str(float(a) / float(b))

        except:
            return "Galat format. Example: 100/5"

    elif user == "help":
        return show_help()
    elif user == "time":
        return get_time()
    elif user == "date":
        return get_date()
    elif user.startswith("note "):
        note = user.replace("note ", "")
        save_note(note)
        return "Note save ho gaya. ✅"

    elif user == "show notes":
        return show_notes()
    elif user.startswith("delete note "):
        try:
            number = int(user.replace("delete note ", ""))
            return delete_note(number)
        except:
            return "Sahi note number likho."
    elif user.startswith("create file "):
        filename = user.replace("create file ", "")
        return create_file(filename)
    else:
        return "Mujhe abhi ye command nahi aati."