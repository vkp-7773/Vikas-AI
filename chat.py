import random

RESPONSES = {
    "hello": "Hello Bhai 😄",
    "hi": "Hello Bhai 😄",
    "hey": "Hello Bhai 😄",

    "who are you":
    "Main Vikas AI hu. Ek Python based personal assistant. 🤖",

    "what can you do":
    "Main files, folders, notes, history, memory aur calculation kar sakta hu.",

    "tum kya kar sakte ho":
    "Main files, folders, notes, history, memory aur calculation kar sakta hu.",

    "tum kya kar skte ho":
    "Main files, folders, notes, history, memory aur calculation kar sakta hu.",

    "who made you":
    "Mujhe Vikas ne Python me develop kiya hai. 😎",

    "coding":
    "Coding practice se hi strong hoti hai. Roz code karo.",

    "what is python":
    "Python ek high level programming language hai.",

    "what is ai":
    "AI ka matlab Artificial Intelligence hai.",

    "what is dsa":
    "DSA ka matlab Data Structures and Algorithms hai.",

    "how are you":
    "Main badhiya hu Bhai. 😄",

    "good morning":
    "Good Morning Bhai ☀️",

    "good night":
    "Good Night Bhai 🌙",
}

JOKES = [
    "Programmer ka favourite place? Python 🐍",
    "Bug mila? Matlab naya lesson mila 😂",
    "Coding aur chai best combo ☕"
]

QUOTES = [
    "Consistency beats talent.",
    "Har error tumhe better programmer banata hai.",
    "Never stop learning."
]

MOTIVATION = [
    "Aaj ki mehnat kal ka package banegi. 🚀",
    "Roz coding karo, success pakki hai. 💪",
    "Small progress is still progress."
]


def chat(command):

    command = command.lower().strip()

    if command in RESPONSES:
        return RESPONSES[command]

    if command == "joke":
        return random.choice(JOKES)

    if command == "quote":
        return random.choice(QUOTES)

    if command == "motivate me":
        return random.choice(MOTIVATION)

    return None