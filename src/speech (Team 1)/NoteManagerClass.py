class NotesManager:
    def __init__(self, filename="notes.txt"):
        self.filename = filename
        self.LoadNotes()

    def LoadNotes(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.notes = [line.strip() for line in f]
        except FileNotFoundError:
            self.notes = []
            self.SaveNotes()

    def SaveNotes(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            if self.notes:
                f.write("\n".join(self.notes) + "\n")

    def CreateNote(self, note_text):
        self.notes.append(note_text)  # Добавляем заметку без метки времени
        self.SaveNotes()

    def ReadNotes(self):
        if self.notes:
            for i, note in enumerate(self.notes):
                print(f"{i+1}. {note}")
        else:
            print("Заметок нет.")

    def DeleteNote(self, note_index):
        if 0 < note_index <= len(self.notes):
            del self.notes[note_index - 1]
            self.SaveNotes()
        else:
            print("Неверный номер заметки.")


