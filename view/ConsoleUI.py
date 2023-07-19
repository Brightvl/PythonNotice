from model import check_length_body_note


def view_main_menu() -> str:
    print(f"""{separator()}
\033[1mЗаметки\033[0m
1. Добавить заметку
2. Выбрать заметку
3. Выйти""")
    return input("Введите номер команды: ")


def show_note_menu() -> str:
    print("""Доступные команды:
1. Изменить название
2. Изменить тело 
3. Удалить
4. Назад""")
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
                    7: "||||Выход из режима редактора||||",
                    8: "Список заметок пуст!",
                    9: "До свидания!",
                    10: "Заметки с таким номером не существует!",
                    11: "Смена фильтра -> 0",
                    12: "Фильтр: ",
                    13: "Заметка не удалена",
                    14: "Введите новое название: "}
    return message_dict[number_message]


def show_all_notes(notes: dict):
    print("Список заметок:")
    for key, value in notes.items():
        line = "№{:<3s}  Название: {:<15s} Создана: {:<17s} Изменена: {:<17s}". \
            format(key, value['title'], value['date_of_creation'], value['date_of_change'])
        print(f"{line}")


def user_input(message: str) -> str:
    return input(message)


def user_output(message: str):
    print(message)


def show_note(notes: dict, note_id: str):
    temp_data = notes[note_id]
    body_check = (
        temp_data["body"]) if check_length_body_note(notes,
                                                     note_id) > 0 else "| Заметка не содержит записей |"
    text = f"""\033[0mЗаметка\033[0m №:{note_id} 
Название: {temp_data["title"]} 
Создана: {temp_data['date_of_creation']} \nИзменена: {temp_data['date_of_change']}
{separator()}
Тело заметки:
{body_check}
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
