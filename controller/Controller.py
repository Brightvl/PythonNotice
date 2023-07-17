from tkinter import Tk, Label, Button, Text

from model.Tkinter import run_note_editor
from view.ConsoleUI import *
from model.Model import load_notions, save_changes, clear_console, current_time, find_available_key, check_key

import_notes = load_notions()


def main_menu():
    clear_console()
    while True:
        show_all_notes(import_notes)
        choice = view_main_menu()
        if choice == "1":
            add_note(import_notes)
        if choice == "2":
            note_menu(import_notes)
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
                edit_note(notes, choice_id)
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
    notes[note_id]["body"] = run_note_editor(notes, note_id)


def edit_date_of_change(data: dict, id: str):
    data[id]["date_of_change"] = current_time()


def add_note(notes: dict):
    new_note = {
        "title": input("Введите название"),
        "date_of_creation": current_time(),
        "date_of_change": current_time(),
        "body": ""
    }
    key = find_available_key(notes)
    notes[key] = new_note
    edit_note(notes, key)


def delete_note(notes: dict, note_id: str):
    if note_id in notes:
        del notes[note_id]
    save_changes(notes)
