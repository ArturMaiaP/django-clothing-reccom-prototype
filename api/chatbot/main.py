from chatbot import Chatbot

if __name__ == '__main__':
    chatbot = Chatbot()
    while True:
        text = input('> ')
        print(chatbot.turn(text))