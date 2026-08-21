def chatbot():
    print("Chatbot: Hello! How can I help you?")
    print("Chatbot: You can say hello, ask how I am, or say bye.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hi" or user_input == "hello":
            print("Chatbot: Hi!")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand.")


chatbot()