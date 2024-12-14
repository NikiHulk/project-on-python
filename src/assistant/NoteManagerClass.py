
"""
Этот модуль содержит класс `NotesManager`, который управляет заметками, хранящимися в текстовом файле.

Класс:
- NotesManager: Класс для создания, чтения, удаления и сохранения заметок в текстовом файле.

Методы:
- __init__(self, filename="notes.txt"): Инициализирует объект с указанием имени файла для хранения заметок (по умолчанию 'notes.txt').
- LoadNotes(self): Загружает заметки из файла, если файл существует. Если файл не найден, создаёт пустой список и сохраняет его.
- SaveNotes(self): Сохраняет заметки в файл.
- CreateNote(self, note_text): Создаёт новую заметку, добавляя её в список и сохраняет изменения в файл.
- ReadNotes(self): Выводит все заметки с их номерами. Если заметок нет, выводится соответствующее сообщение.
- DeleteNote(self, note_index): Удаляет заметку по заданному индексу. Если индекс некорректен, выводится сообщение об ошибке.

Зависимости:
- Нет внешних зависимостей.

Примечания:
- Все заметки хранятся в текстовом файле, указанном при создании объекта (по умолчанию 'notes.txt').
- Заметки сохраняются в файл при добавлении, удалении и при запуске программы, если файл существует.
"""


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