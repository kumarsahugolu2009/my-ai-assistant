
print("Namaste! Main tumhara AI Assistant hoon.")

while True:
    question = input("Tum: ")

    if question.lower() in ["exit", "quit", "band"]:
        print("Assistant: Phir milenge!")
        break

    print("Assistant: Tumne poochha:", question)


