from model.NodeEditor import NoteEditor
from view.ConsoleUI import *

import_notes = load_notes()
node_editor = NoteEditor()


def main_menu():
    clear_console()
    while True:
        choice = view_main_menu()
        if choice == "1":
            add_note(import_notes)
            user_output(show_message(7))
            continue
        if choice == "2":
            show_all_notes(import_notes)
            note_menu(import_notes)
            continue
        if choice == "3":
            break
        else:
            print(show_message(0))


def note_menu(notes: dict):
    clear_console()
    choice_id = user_input(show_message(1))
    if check_key(notes, choice_id):
        while True:
            show_note(notes, choice_id)
            choice_note_menu = show_note_menu()
            if choice_note_menu == "1":
                user_output(show_message(6))
                edit_note(notes, choice_id)
                user_output(show_message(7))
            if choice_note_menu == "2":
                delete_note(notes, choice_id)
                break
            if choice_note_menu == "3":
                break


def edit_note(notes: dict, note_id: str):
    edit_note_text(notes, note_id)
    edit_date_of_change(notes, note_id)
    save_changes(notes)


def edit_note_text(notes: dict, note_id: str):
    notes[note_id]["body"] = node_editor.run_editor(notes, note_id)


def edit_date_of_change(data: dict, id: str):
    data[id]["date_of_change"] = current_time()


def add_note(notes: dict):
    key = find_available_key(notes)
    notes[key] = show_add_note()
    edit_note(notes, key)


def delete_note(notes: dict, note_id: str):
    temp_note = notes[note_id]
    if check_choice():
        if note_id in notes:
            user_output(show_message(4, temp_note["title"]))
            del notes[note_id]
        save_changes(notes)


def check_choice():
    return show_confirm() == "y"
