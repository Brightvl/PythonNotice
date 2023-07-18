from model.NodeEditor import NoteEditor
from View.ConsoleUI import *

import_notes = load_notes()  # Переменная в которую сохранен Json словарь
node_editor = NoteEditor()  # Создание объекта "редактор заметок"


def main_menu():
    """
    Метод для работы с главным меню
    :return:
    """
    clear_console()
    while True:
        choice = view_main_menu()
        if choice == "1":
            add_note(import_notes)
            user_output(show_message(7))
            continue
        elif choice == "2":
            if check_length_input_notes(import_notes) > 0:
                show_all_notes(import_notes)
                note_menu(import_notes)
            else:
                user_output(show_message(8))
            continue
        elif choice == "3":
            user_output(show_message(9))
            break
        else:
            print(show_message(0))


def note_menu(notes: dict):
    """
    Метод для работы с меню заметки
    :param notes:
    :return:
    """
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
            elif choice_note_menu == "2":
                delete_note(notes, choice_id)
                break
            elif choice_note_menu == "3":
                break
    else:
        user_output(show_message(10))


def edit_note(notes: dict, note_id: str):
    """
    Редактирование заметки
    :param notes:
    :param note_id:
    :return:
    """
    edit_note_text(notes, note_id)
    edit_date_of_change(notes, note_id)
    save_changes(notes)


def edit_note_text(notes: dict, note_id: str):
    """
    Редактирование текста заметки
    :param notes:
    :param note_id:
    :return:
    """
    notes[note_id]["body"] = node_editor.run_editor(notes, note_id)


def edit_date_of_change(notes: dict, note_id: str):
    """
    Изменение времени последнего изменения в заметке
    :param notes:
    :param note_id:
    :return:
    """
    notes[note_id]["date_of_change"] = current_time()


def add_note(notes: dict):
    """
    Добавить новую заметку
    :param notes:
    :return:
    """
    key = find_available_key(notes)
    notes[key] = show_add_note()
    edit_note(notes, key)


def delete_note(notes: dict, note_id: str):
    """
    Удалить заметку
    :param notes:
    :param note_id:
    :return:
    """
    temp_note = notes[note_id]
    if check_choice():
        if note_id in notes:
            user_output(show_message(4, temp_note["title"]))
            del notes[note_id]
        save_changes(notes)


def check_choice():
    """
    Проверить подтвердил ли пользователь
    :return:
    """
    return show_confirm() == "y"


def check_length_input_notes(notes: dict):
    """
    Проверяет сколько заметок создано
    :return:
    """
    return len(notes)



