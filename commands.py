from converter import convert
from password_tools import generate_password
from reminder import (
    add_reminder,
    show_reminders,
    delete_reminder,
)
from todo import (
    add_todo,
    show_todos,
    delete_todo,
    clear_todos,
)
from calculator import calculate
from chat import chat
from memory import save, load
from tools import get_time, get_date
from knowledge import get_answer, save_knowledge
import random


JOKES = [
    "Programmer ka favourite place? Python 🐍",
    "Bug mila? Samajh lo naya lesson mil gaya 😂",
    "Coding aur chai ka combo best hai ☕",
]


QUOTES = [
    "Har din kuch naya seekhna hi progress hai.",
    "Consistency se hi bade goals complete hote hain.",
    "Har error tumhe better programmer banata hai.",
]


MOTIVATION = [
    "Bhai lage raho, ek-ek step se bada project banta hai. 🚀",
    "Aaj ki mehnat kal ka result banegi. 💪",
    "Practice karte raho, coding strong hoti jayegi.",
]












def execute_builtin(command):

    command = command.lower().strip()


    calc = calculate(command)

    if calc:
       return calc

    # UNIT CONVERTER

    result = convert(command)

    if result:
        return result


    # Knowledge Database

    answer = get_answer(command)

    if answer:
        return answer



# Chat

    response = chat(command)

    if response:
        return response



    # Greetings

    if command in ["hello", "hi", "hey"]:
        return "Hello Bhai 😄"


    if command == "how are you":
        return "Main badhiya hu Bhai. Tu bata?"


    if command == "good morning":
        return "Good Morning Bhai ☀️"


    if command == "good night":
        return "Good Night Bhai 🌙"



    # Time Date

    if command == "time":
        return get_time()


    if command == "date":
        return get_date()



    # Fun

    if command == "joke":
        return random.choice(JOKES)


    if command == "quote":
        return random.choice(QUOTES)


    if command == "motivate me":
        return random.choice(MOTIVATION)



    # Memory

    if command.startswith("my name is "):

        name = command.replace("my name is ", "").strip()

        save("name", name)

        return f"Okay {name}, yaad rakh liya. ✅"



    if command == "what is my name":

        name = load("name")

        if name:
            return f"Tumhara naam {name} hai."

        return "Mujhe abhi tumhara naam nahi pata."


    # Knowledge Save

    if command.startswith("learn "):

        data = command.replace("learn ", "").split("=", 1)

        if len(data) == 2:

            question = data[0].strip().lower()
            answer = data[1].strip()

            save_knowledge(question, answer)

            return f"Yaad rakh liya:\n{question} = {answer} ✅"



    # Knowledge Search (saved knowledge)

    answer = get_answer(command)

    if answer:
        return answer

    # TODO

    if command.startswith("todo "):

        task = command.replace("todo ", "").strip()

        return add_todo(task)


    if command == "show todos":

        return show_todos()


    if command.startswith("delete todo "):

        try:

            number = int(command.replace("delete todo ", ""))

            return delete_todo(number)

        except:

            return "Sahi todo number likho."


    if command == "clear todos":

        return clear_todos()
    # Reminder

    if command.startswith("remind me "):

        text = command.replace("remind me ", "").strip()

        return add_reminder(text)


    if command == "reminders":

        return show_reminders()


    if command.startswith("delete reminder "):

        try:

            number = int(command.replace("delete reminder ", ""))

            return delete_reminder(number)

        except:

            return "Sahi reminder number likho."
    # PASSWORD GENERATOR

    if command == "password":
        return "Generated Password:\n" + generate_password()

    if command.startswith("password "):

        try:
            length = int(command.replace("password ", "").strip())

            if length < 4:
                return "Minimum password length 4 honi chahiye."

            if length > 100:
                return "Maximum password length 100 hai."

            return "Generated Password:\n" + generate_password(length)

        except:
            return "Example: password 12"


    # Help

    if command == "help":

        return """
========== VIKAS AI ==========

Conversation:
hello
who are you
what can you do

Knowledge:
what is python
what is ai
what is dsa

Learning:
learn who is vikas = Vikas AI ka developer

Todo:
todo Buy milk
show todos
delete todo 1
clear todos

Tools:
time
date
joke
quote
motivate me

Calculator:
2+2
25*6

Unit Converter:
10 km to m
500 cm to m
5 kg to g
2000 g to kg
2 hour to minutes
30 min to sec

Memory:
my name is Vikas
what is my name

Files:
create file
read file
write file
list files

Folders:
create folder
list folders

Notes:
note
show notes

Password:
password
password 8
password 16

History:
history

==============================
"""

    return None