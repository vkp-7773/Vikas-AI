from brain import think

print("=" * 40)
print("🤖 VIKAS AI")
print("=" * 40)

while True:

    user = input("You : ").lower()

    answer = think(user)

    print("Vikas AI :", answer)

    if user == "bye":
        break