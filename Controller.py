from ConsoleUI import *
from Model import load_notions, save_changes, clear_screen, current_time, find_available_key, check_key

data = {}


def main_menu():
    clear_screen()
    data = load_notions()
    while True:
        show_all_notes(data)
        choice = view_main_menu()
        if choice == "1":
            add_note(data)
        if choice == "2":
            note_menu(data)
        if choice == "3":
            break
        else:
            print(show_message(0))


def note_menu(data: dict):
    clear_screen()
    id = user_input(show_message(1))
    if check_key(data, id):
        while True:
            show_note(data, id)
            choice_note_menu = view_note_menu()
            if choice_note_menu == "1":
                edit_note(data, id)
            if choice_note_menu == "2":
                delete_note(data, id)
                break
            if choice_note_menu == "3":
                break


def exit_menu():
    pass


def edit_note(data: dict, id: str):
    user_output(show_message(3))
    show_text_editing_window(data, id)
    edit_date_of_change(data, id)
    save_changes(data)


def edit_date_of_change(data: dict, id: str):
    data[id]["date_of_change"] = current_time()


def add_note(data: dict):
    new_note = {
        "title": input("введите название"),
        "date_of_creation": current_time(),
        "date_of_change": current_time(),
        "body": input("Тело заметки:")
    }
    key = find_available_key(data)
    data[key] = new_note
    save_changes(data)


def delete_note(data: dict, id: str):
    if id in data:
        del data[id]
    save_changes(data)
