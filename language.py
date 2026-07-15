def understand(user):

    user = user.lower()

    if user.startswith("bhai "):
        user = user.replace("bhai ", "", 1)

    if user.startswith("please "):
        user = user.replace("please ", "", 1)

    return user