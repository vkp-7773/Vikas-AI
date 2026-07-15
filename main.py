from brain import think
from history import save_history
print("=" * 40)
print("🤖 VIKAS AI")
print("=" * 40)

while True:

    user = input("You : ").lower()
    save_history(user)
    answer = think(user)

    print("Vikas AI :", answer)

    if user == "bye":
        break