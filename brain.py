from memory import save, load
from commands import show_help

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

    else:
        return "Mujhe abhi ye command nahi aati."