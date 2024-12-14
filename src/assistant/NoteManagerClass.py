class NotesManager:
    """
    Класс для управления списком заметок, сохраняемых в текстовом файле.
    Атрибуты:
        filename (str): Имя файла для хранения заметок (по умолчанию "notes.txt").
        notes (list): Список заметок (каждая заметка — строка).
    Методы:
        LoadNotes(): Загружает заметки из файла.
        SaveNotes(): Сохраняет заметки в файл.
        CreateNote(note_text): Создает новую заметку.
        ReadNotes(): Выводит все заметки на экран.
        DeleteNote(note_index): Удаляет заметку по её номеру.
    """

    def __init__(self, filename="notes.txt"):
        self.filename = filename
        self.LoadNotes()

    def LoadNotes(self):
        """Загружает заметки из файла.  Если файл не существует, создает пустой список заметок."""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.notes = [line.strip() for line in f]
        except FileNotFoundError:
            self.notes = []
            self.SaveNotes()

    def SaveNotes(self):
        """Сохраняет заметки в файл."""
        with open(self.filename, "w", encoding="utf-8") as f:
            if self.notes:
                f.write("\n".join(self.notes) + "\n")

    def CreateNote(self, note_text):
        """
        Создает новую заметку.
        Args:
            note_text (str): Текст заметки.
        """
        self.notes.append(note_text)  # Добавляем заметку без метки времени
        self.SaveNotes()

    def ReadNotes(self):
        """Выводит все заметки на экран."""
        if self.notes:
            for i, note in enumerate(self.notes):
                print(f"{i+1}. {note}")
        else:
            print("Заметок нет.")

    def DeleteNote(self, note_index):
        """
        Удаляет заметку по её номеру.
        Args:
            note_index (int): Номер заметки для удаления.
        """
        if 0 < note_index <= len(self.notes):
            del self.notes[note_index - 1]
            self.SaveNotes()
        else:
            print("Неверный номер заметки.")