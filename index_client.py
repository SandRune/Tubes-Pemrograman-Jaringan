import threading
from multithread.client import ChatClient
from SingleThread.newclient import SingleThreadChatClient
import os

if __name__ == '__main__':
    os.system("cls")
    print("Welcome to Chat Client!")

    threading_choice = input("Do you want to use multithreading? (yes/no): ").lower().strip()
    if threading_choice == 'yes':
        chat_client = ChatClient()
        receive_thread = threading.Thread(target=chat_client.receive)
        receive_thread.start()

        write_thread = threading.Thread(target=chat_client.write)
        write_thread.start()
    else:
        chat_client = SingleThreadChatClient()
        chat_client.run()
