import nltk
import random
from nltk.chat.util import Chat, reflections

# Define some patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you?', ['I am doing well, thank you!', 'I am good, thanks for asking!', 'I am fine, how about you?']),
    (r'(.*) your name?', ['I am just a chatbot.', 'I do not have a name, I am just a bot.', 'You can call me a chatbot.']),
    (r'(.*) (good|fine)', ['That\'s great!', 'Good to hear!', 'Awesome!']),
    (r'(.*) (bad|not good)', ['Oh, I\'m sorry to hear that.', 'I hope things get better soon.', 'Hang in there.']),
    (r'(.*) (age|old)', ['I am just a computer program, so I do not have an age.']),
    (r'(.*) (weather)', ['I\'m sorry, I cannot provide real-time weather information.']),
    (r'(.*) (bye|goodbye)', ['Goodbye!', 'See you later!', 'Take care!']),
    # Add more patterns and responses as needed
]

# Create a Chatbot
def simple_chatbot():
    print("Hi! I am a chatbot. You can start talking to me. Type 'quit' to end the conversation.")
    chatbot = Chat(patterns, reflections)
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    simple_chatbot()
