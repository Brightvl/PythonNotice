def view_menu() -> str:
    while True:
        print("Доступные команды:")
        print("1. Добавить заметку")
        print("2. Показать список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")
        return input("Введите номер команды: ")


def message(number_message: int):
    dict = {0: "Неверный выбор. Пожалуйста, попробуйте снова.",
            1: "Введите id заметки: "}
    return dict[number_message]


def view_records(data: dict):
    for key, value in data.items():
        print(f"№{key}. Название - {value['title']}. Дата последнего изменения {value['date_of_change']}")


def user_input(msg: str) -> str:
    return input(msg)


def show_notion(data: dict, id: str):
    temp_data = data[id]
    print(f"""
    id:{id} 
    Название:{temp_data["title"]} 
    Дата создания: {temp_data['date_of_creation']}
    Последнее изменение: {temp_data['date_of_change']}""")

