def chatbot():
    print("bot: Hello! I am Simple Chatbot.")
    print("bot: Type 'bye' to exit.")
    while True:
        user = input("you:").lower()
        if user =="hello":
            print("bot: Hi! How can i help you?")
        elif user =="how are you":
                print("bot: I am fine, thank you!")
        elif user =="what is your name":    
                print("bot: I am Simple Chatbot.") 
        elif user =="who creat you":
                print("bot: I was created by a developer.")
        elif user =="what can you do":
                print("bot: I can chat with you and answer simple questions.")
        elif user =="thank you":
                print("bot: You're welcome!")
        elif user =="bye":
                print("bot: Goodbye! Have a nice day.")
                break
        else:
                print("bot: I'm sorry, I don't understand that.")
chatbot()