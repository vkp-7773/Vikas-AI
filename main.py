from brain import think
from history import save_history

print("=" * 40)
print("🤖 VIKAS AI")
print("=" * 40)

while True:

    user = input("You : ")

    if user.lower() == "bye":
        print("Vikas AI : Bye Bhai 👋")
        break

    save_history(user)

    answer = think(user)

    print("Vikas AI :", answer)