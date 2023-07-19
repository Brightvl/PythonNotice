import json
import os
from datetime import datetime


def load_notes() -> dict:
    with open("data/notes.json", "r") as read_file:
        return json.loads(read_file.read())


def save_changes(data):
    with open("data/notes.json", 'w') as save_file:
        json.dump(data, save_file, indent=4)


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def current_time():
    return datetime.now().strftime("%d-%m-%Y %H:%M")


def find_available_key(notes):
    keys = set(notes.keys()) if isinstance(notes, dict) else set()
    i = 1
    while str(i) in keys:
        i += 1
    return str(i)


def check_key(data: dict, key: str):
    return key in data


def check_length_body_note(note: dict, note_id: str):
    return len(note[note_id]['body'])


def sort_dictionary_by_key(notes: dict):
    return dict(sorted(notes.items(), key=lambda x: int(x[0])))


def sort_dictionary_by_title(notes: dict):
    return dict(sorted(notes.items(), key=lambda x: x[1]["title"]))


def sort_dictionary_by_date_of_creation(notes: dict):
    return dict(sorted(notes.items(), key=lambda x: x[1]["date_of_creation"]))


def sort_dictionary_by_date_of_change(notes: dict):
    return dict(sorted(notes.items(), key=lambda x: x[1]["date_of_change"]))


def check_length_input_notes(notes: dict):
    """
    Проверяет сколько заметок создано
    :return:
    """
    return len(notes)
