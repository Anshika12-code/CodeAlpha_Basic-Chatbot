def chatbot():
    print("Bot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi there!")
        elif user == "how are you":
            print("Bot: I'm fine!")
        elif user == "bye":
            print("Bot: Goodbye!") 
            break
        else:
            print("Bot: I don't understand.")

chatbot()