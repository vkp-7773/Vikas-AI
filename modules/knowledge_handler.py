from knowledge import (
    save_knowledge,
    get_answer,
    all_knowledge,
    delete_knowledge,
)


def handle_knowledge(command):

    command = command.strip()

    # learn question = answer

    if command.startswith("learn "):

        try:

            data = command.replace("learn ", "").split("=", 1)

            question = data[0].strip().lower()
            answer = data[1].strip()

            save_knowledge(question, answer)

            return "Knowledge save ho gayi. ✅"

        except:

            return "Use : learn question = answer"



    # show knowledge

    elif command == "show knowledge":

        data = all_knowledge()

        if not data:
            return "Knowledge empty hai."

        result = "Knowledge:\n\n"

        i = 1

        for q, a in data.items():

            result += f"{i}. {q}\n   → {a}\n\n"

            i += 1

        return result



    # knowledge count

    elif command == "knowledge count":

        return f"Total Knowledge : {len(all_knowledge())}"



    # delete knowledge

    elif command.startswith("delete knowledge "):

        question = command.replace("delete knowledge ", "").strip()

        if delete_knowledge(question):

            return "Knowledge delete ho gayi. ✅"

        return "Knowledge nahi mili."



    # Search

    answer = get_answer(command)

    if answer:

        return answer

    return None