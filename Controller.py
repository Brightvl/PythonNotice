from ConsoleUI import *
from Model import load_notions

data = {};


def run_menu():
    data = load_notions()
    show_all_records(data)
    choice = view_menu()
    if choice == "2":
        show_all_records(data)
    if choice == "3":
        id = user_input(message(1))
        show_notion(data, id)
        user_output(message(2))



    else:
        print(message(0))
