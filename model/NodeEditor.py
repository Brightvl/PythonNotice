from tkinter import Tk, Label, Text, Button, Frame


class NoteEditor:
    def __init__(self):
        self.saved_text = ""

    def run_editor(self, notes: dict, note_id: str):
        root = Tk()
        root.configure(background="#F9EABD")

        label = Label(
            root,
            text=f"""№:{note_id}
Название: {notes[note_id]['title']}
Дата создания: {notes[note_id]['date_of_creation'].strftime("%d-%m-%Y %H:%M")}
Изменён: {notes[note_id]['date_of_change'].strftime("%d-%m-%Y %H:%M")}""",
            justify="left", font=13)
        label.configure(background="#F9EABD")
        label.pack(side="top", anchor="w")

        text = Text(root)
        text.configure(background="#F9CD9D", font=11)
        text.insert("end", notes[note_id]["body"])
        text.pack(expand=True, fill="both")

        def exit_application():
            root.destroy()

        button_frame = Frame(root)
        button_frame.pack()

        exit_button = Button(button_frame, text="Выйти без сохранения", command=exit_application)
        exit_button.pack(side="left")

        def exit_and_save_application():
            text_content = text.get("1.0", "end-1c")
            self.saved_text = str(text_content)
            root.destroy()

        exit_and_save_button = Button(button_frame, text="Сохранить и выйти", command=exit_and_save_application)
        exit_and_save_button.pack(side="left")

        def on_closing():
            root.destroy()

        root.protocol("WM_DELETE_WINDOW", on_closing)

        root.mainloop()
        return self.saved_text
