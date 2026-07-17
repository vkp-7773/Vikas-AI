from modules.patterns import PATTERNS
def understand(user):

    user = user.lower().strip()

    # Pattern Router

    for pattern, command in PATTERNS.items():

        if user.startswith(pattern):

            text = user.replace(pattern, "").strip()

            return command + " " + text

    # Remove extra words
    if user.startswith("bhai "):
        user = user.replace("bhai ", "", 1)

    if user.startswith("please "):
        user = user.replace("please ", "", 1)

    # Fixed sentence rules
    if user.startswith("ek file banao "):
        filename = user.replace("ek file banao ", "")
        return "create file " + filename

    if user.startswith("file banao "):
        filename = user.replace("file banao ", "")
        return "create file " + filename

    if user.startswith("meri file banao "):
        filename = user.replace("meri file banao ", "")
        return "create file " + filename

    if user.startswith("make file "):
        filename = user.replace("make file ", "")
        return "create file " + filename

    # Keyword based rule
    if "file" in user and ".txt" in user:

        words = user.split()

        filename = ""

        for word in words:
            if word.endswith(".txt"):
                filename = word
                break

        if filename:
            return "create file " + filename
    # Natural Language Notes

    if user.startswith("note bana do "):
        text = user.replace("note bana do ", "")
        return "note " + text

    if user.startswith("meri note bana do "):
        text = user.replace("meri note bana do ", "")
        return "note " + text

    if user.startswith("save note "):
        text = user.replace("save note ", "")
        return "note " + text
    # Natural Language Notes

    if user.startswith("note bana do "):
        text = user.replace("note bana do ", "")
        return "note " + text

    if user.startswith("meri note bana do "):
        text = user.replace("meri note bana do ", "")
        return "note " + text

    if user.startswith("save note "):
        text = user.replace("save note ", "")
        return "note " + text
     # Natural Language Folder

    if user.startswith("folder banao "):
        folder = user.replace("folder banao ", "")
        return "create folder " + folder

    if user.startswith("ek folder banao "):
        folder = user.replace("ek folder banao ", "")
        return "create folder " + folder

    if user.startswith("mera folder banao "):
        folder = user.replace("mera folder banao ", "")
        return "create folder " + folder
 
     # Auto add .txt extension

    if user.startswith("create file "):

        filename = user.replace("create file ", "")

        if "." not in filename:
            filename += ".txt"

        return "create file " + filename
    return user