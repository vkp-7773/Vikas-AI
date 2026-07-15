from brain import think
from history import save_history
from language import understand
print("=" * 40)
print("🤖 VIKAS AI")
print("=" * 40)

while True:

    user = input("You : ").lower()

    save_history(user)

    command = understand(user)

    answer = think(command)

    print("Vikas AI :", answer)

    if user == "bye":
        break