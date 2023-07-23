import json
import os
from datetime import datetime
import copy


def load_notes() -> dict:
    with open("data/notes.json", "r") as read_file:
        data = json.loads(read_file.read())
        load_convert_datetime(data)
        return data


def load_convert_datetime(data: json):
    for key, value in data.items():
        if 'date_of_creation' in value:
            value['date_of_creation'] = datetime.strptime(value['date_of_creation'], "%d-%m-%Y %H:%M")
        if 'date_of_change' in value:
            value['date_of_change'] = datetime.strptime(value['date_of_change'], "%d-%m-%Y %H:%M")


def save_changes(data: dict):
    temp_data = copy.deepcopy(data)
    save_convert_datetime(temp_data)
    with open("data/notes.json", 'w') as save_file:
        json.dump(temp_data, save_file, indent=4)


def save_convert_datetime(data: dict):
    for key, value in data.items():
        if 'date_of_creation' in value:
            value['date_of_creation'] = value['date_of_creation'].strftime("%d-%m-%Y %H:%M")
        if 'date_of_change' in value:
            value['date_of_change'] = value['date_of_change'].strftime("%d-%m-%Y %H:%M")


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')



def current_time():
    return datetime.now()


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


def find_date_first_note(notes: dict):
    return min(note['date_of_creation'] for note in notes.values())


def find_date_end_note(notes: dict):
    return max(note['date_of_creation'] for note in notes.values())


