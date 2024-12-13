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
        """
        Инициализирует менеджер заметок, загружая заметки из указанного файла.

        Аргументы:
            filename (str): Имя файла для хранения заметок (по умолчанию "notes.txt").
        """
        self.filename = filename
        self.notes = []  # Инициализация пустого списка заметок
        self.LoadNotes()

    def LoadNotes(self):
        """Загружает заметки из файла. Если файл не существует, создает пустой список заметок."""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.notes = [line.strip() for line in f]
        except FileNotFoundError:
            print(f"Файл {self.filename} не найден. Будет создан новый файл.")
            self.notes = []
            self.SaveNotes()
        except Exception as e:
            print(f"Ошибка при загрузке заметок: {e}")

    def SaveNotes(self):
        """Сохраняет все заметки в файл."""
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                if self.notes:
                    f.write("\n".join(self.notes) + "\n")
        except Exception as e:
            print(f"Ошибка при сохранении заметок: {e}")

    def CreateNote(self, note_text):
        """
        Создает новую заметку.

        Аргументы:
            note_text (str): Текст заметки.
        """
        if note_text:
            self.notes.append(note_text)
            self.SaveNotes()
        else:
            print("Нельзя создать пустую заметку.")

    def ReadNotes(self):
        """Выводит все заметки на экран."""
        if self.notes:
            for i, note in enumerate(self.notes, start=1):
                print(f"{i}. {note}")
        else:
            print("Заметок нет.")

    def DeleteNote(self, note_index):
        """
        Удаляет заметку по её номеру.

        Аргументы:
            note_index (int): Номер заметки для удаления.
        """
        if 0 < note_index <= len(self.notes):
            del self.notes[note_index - 1]
            self.SaveNotes()
            print(f"Заметка номер {note_index} удалена.")
        else:
            print(f"Неверный номер заметки: {note_index}. Пожалуйста, введите правильный номер.")
