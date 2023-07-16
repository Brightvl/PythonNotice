def view_menu() -> str:
    print("""
Доступные команды:
1. Добавить заметку
2. Выбрать заметку
3. Выйти""")

    return input("Введите номер команды: ")


def message(number_message: int):
    dict = {0: "Неверный выбор. Пожалуйста, попробуйте снова.",
            1: "Введите Id заметки: ",
            2: "Редактировать?"}
    return dict[number_message]


def show_all_records(data: dict):
    print("Имя:")
    for key, value in data.items():
        print(f"id {key}. "
              f"Название: {value['title']}. "
              f"Дата изменения: {value['date_of_change']}"
              )


def user_input(mmessage: str) -> str:
    return input(mmessage)


def user_output(message: str):
    print(message)


def show_notion(data: dict, id: str):
    temp_data = data[id]
    text = f"""
Id:{id} 
Название: {temp_data["title"]} 
Дата создания: {temp_data['date_of_creation']} Последнее изменение: {temp_data['date_of_change']}

{temp_data["body"]}"""
    print(text)
