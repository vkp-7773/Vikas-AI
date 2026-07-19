import random
import string


def generate_password(length=12):

    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%^&*?"

    chars = letters + digits + symbols

    password = "".join(random.choice(chars) for _ in range(length))

    return password