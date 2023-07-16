def view_main_menu() -> str:
    print("""
Доступные команды:
1. Добавить заметку
2. Выбрать заметку
3. Выйти""")

    return input("Введите номер команды: ")


def view_note_menu() -> str:
    print("""Доступные команды:
1. Редактировать
2. Удалить
3. Назад""")

    return input("Введите номер команды: ")


def show_message(number_message: int):
    message_dict = {0: "Неверный выбор. Пожалуйста, попробуйте снова.",
                    1: "Введите Id заметки: ",
                    2: "Редактировать?",
                    3: "Режим редактирования:"}
    return message_dict[number_message]




def show_all_notes(data: dict):
    print("Список заметок")
    for key, value in data.items():
        print(f"id {key}. "
              f"Название: {value['title']}. "
              f"Дата изменения: {value['date_of_change']}"
              )


def user_input(message: str) -> str:
    return input(message)


def user_output(message: str):
    print(message)


def show_note(data: dict, id_note: str):
    temp_data = data[id_note]
    text = f"""
{"-"*50}
Id:{id_note} 
Название: {temp_data["title"]} 
Дата создания: {temp_data['date_of_creation']} \nИзменён: {temp_data['date_of_change']}
{"-"*50}
{temp_data["body"]}
{"-"*50}"""
    print(text)


def show_text_editing_window(data: dict, id_note: str):
    print("Редактирование текста")
    print("-"*50)
    print(data[id_note]["body"])
    print("-"*50)
    new_text = user_input("Введите новый текст:\n")
    data[id_note]["body"] = new_text
