def calculate(command):

    try:
        expression = command.replace(" ", "")

        allowed = "0123456789+-*/().%"

        for ch in expression:
            if ch not in allowed:
                return None

        return f"Answer : {eval(expression)}"

    except:
        return None