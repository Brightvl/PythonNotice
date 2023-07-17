from model.Model import *


def view_main_menu() -> str:
    print(f"""
{separator()}
"Заметки"
{separator()}
1. Добавить заметку
2. Выбрать заметку
3. Выйти""")
    return input("Введите номер команды: ")


def show_note_menu() -> str:
    print("""Доступные команды:
1. Редактировать
2. Удалить
3. Назад""")
    return input("Введите номер команды: ")


def separator():
    return "-" * 50


def show_message(number_message: int, param=0):
    message_dict = {0: "Неверный выбор. Пожалуйста, попробуйте снова.",
                    1: "Введите № заметки: ",
                    2: "Редактировать?",
                    3: "Введите новый текст: ",
                    4: f"Заметка {param} удалена",
                    5: "Вы уверенны? Y:Yes/N:No ",
                    6: "||||Работа в режиме редактора||||",
                    7: "||||Выход из режима редактора||||"}
    return message_dict[number_message]


def show_all_notes(notes: dict):
    print("Список заметок")
    for key, value in notes.items():
        line = "№{:<3s}  Название: {:<15s} Дата изменения: {:<17s}".format(key, value['title'],
                                                                                value['date_of_change'])
        print(line)

def user_input(message: str) -> str:
    return input(message)


def user_output(message: str):
    print(message)


def show_note(notes: dict, note_id: str):
    temp_data = notes[note_id]
    text = f"""
{separator()}
№:{note_id} 
Название: {temp_data["title"]} 
Дата создания: {temp_data['date_of_creation']} \nИзменён: {temp_data['date_of_change']}
{separator()}
Тело заметки:
{temp_data["body"]}
{separator()}"""
    print(text)


def show_text_editing_window(data: dict, id_note: str):
    print(f"""
Редактирование текста:
{separator()}
{data[id_note]["body"]}
{separator()}""")


def show_add_note():
    new_note = {
        "title": input(f"{separator()}\nВведите название: "),
        "date_of_creation": current_time(),
        "date_of_change": current_time(),
        "body": ""
    }
    user_output(show_message(6))
    return new_note


def show_confirm():
    return user_input(show_message(5)).lower()
