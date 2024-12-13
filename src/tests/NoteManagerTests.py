import pytest
from unittest.mock import patch
from src import NotesManager  # Путь к файлу NotesManagerClass.py

@pytest.fixture
def notes_manager():
    # Создаем новый экземпляр NotesManager перед каждым тестом
    manager = NotesManager()
    manager.notes = []  # Очищаем список заметок перед каждым тестом
    return manager

def test_create_note(notes_manager):
    # Мокируем метод SaveNotes
    with patch.object(NotesManager, 'SaveNotes') as mock_save_notes:
        note_text = "Тестовая заметка"
        notes_manager.CreateNote(note_text)

        # Проверяем, что заметка была добавлена
        assert note_text in notes_manager.notes
        mock_save_notes.assert_called_once()  # Убедимся, что SaveNotes был вызван

def test_read_notes(notes_manager):
    # Добавим заметки для теста
    note_text1 = "Первая заметка"
    note_text2 = "Вторая заметка"
    notes_manager.CreateNote(note_text1)
    notes_manager.CreateNote(note_text2)

    # Проверяем, что все заметки отображаются
    assert note_text1 in notes_manager.notes
    assert note_text2 in notes_manager.notes

def test_delete_note(notes_manager):
    # Добавим заметку для теста
    note_text = "Заметка для удаления"
    notes_manager.CreateNote(note_text)

    # Убедимся, что заметка добавлена
    assert note_text in notes_manager.notes

    # Мокируем метод SaveNotes
    with patch.object(notes_manager, 'SaveNotes') as mock_save_notes:
        notes_manager.DeleteNote(1)

        # Проверяем, что заметка была удалена
        assert note_text not in notes_manager.notes  # Заметка должна быть удалена
        mock_save_notes.assert_called_once()  # Убедимся, что SaveNotes был вызван
