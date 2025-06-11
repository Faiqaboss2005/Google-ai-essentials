def chatbot():
    print("🤖 Hello! I'm a simple AI chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Bot: Hi there! How can I assist you today?")
        elif "your name" in user_input:
            print("Bot: I'm just a simple AI bot, created as a learning project!")
        elif "ai" in user_input:
            print("Bot: AI stands for Artificial Intelligence. It's about making machines think like humans.")
        elif "bye" in user_input:
            print("Bot: Goodbye! 👋")
            break
        else:
            print("Bot: I'm not sure how to respond to that.")

# Run the chatbot
chatbot()
