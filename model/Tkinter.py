from tkinter import Tk, Label, Text


# class note_editor:
#     def __init__(self, input_note: dict, note_id: str, ):
#         self.__input_note = input_note
#         self.__note_id = note_id
#
#
#     @property
#     def input_note(self):
#         return self.__input_note
#
#     @property
#     def note_id(self):
#         return self.__note_id


def run_note_editor(notes: dict, note_id: str):
    root = Tk()
    # Добавляем плашку с наименованием
    label = Label(
        root,
        text=f"№:{note_id} "
             f"Название: {notes[note_id]['title']} \n"
             f"Дата создания: {notes[note_id]['date_of_creation']} "
             f"\nИзменён: {notes[note_id]['date_of_change']}\n")
    label.pack()

    # добавляем текст
    text = Text(root)
    text.insert("end", notes[note_id]["body"])
    text.pack()

    # обрабатываем нажатие креста
    def on_closing():
        text_content = text.get("1.0", "end-1c")
        global saved_text
        saved_text = str(text_content)
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()
    return saved_text
