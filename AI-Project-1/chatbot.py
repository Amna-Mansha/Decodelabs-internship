print("===AI Chatbot===")
print("type 'bye' to exit")
while True:
    user_input = input("You: ").lower()
     #Greetings
    if user_input =="hello" or user_input =="hi":
        print("Chatbot: Hello! Nice to meet you")
       
     #asking condition
    elif user_input == "how are you?":
         print("Chatbot: I'm doing well, thank you! How about you?")
       
     # Name feature
    elif user_input == "what's your name?":
         print( "chatbot: My name is chatbot")
        
     #Help feature
    elif user_input == "help":
       print("Chatbot: I can answer simple questions like 'how are you?' or 'what's your name?'")
     # exit command
    elif user_input == "bye":
        print("Chatbot: Goodbye! Have a great day!")
        break       
     # unknown input
    else:
        print("Chatbot: I'm sorry, I don't understand that.")  