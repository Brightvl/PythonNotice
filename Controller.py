from ConsoleUI import *
from Model import load_notions

data = {};


def run_menu():
    data = load_notions()

    print(data)
    choice = view_menu()
    if choice == "2":
        view_records(data)
    if choice == "3":
        id = user_input(message(1))
        show_notion(data, id)


    else:
        print(message(0))
