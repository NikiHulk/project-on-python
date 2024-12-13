import pytest
from unittest.mock import patch
from src import listenForWakeWord, executeCommand

# Общий мок для speak
@pytest.fixture(scope="module")
def mock_speak():
    with patch('assistant.ProcessingVoiceInput.speak') as mock:
        yield mock

# Общий мок для распознавания речи
@pytest.fixture(scope="module")
def mock_recognizer():
    with patch('speech_recognition.Recognizer.recognize_google', return_value="привет ева") as mock:
        yield mock

# Общий мок для input
@pytest.fixture(scope="module")
def mock_input():
    with patch('builtins.input', return_value="привет ева") as mock:
        yield mock

# Мок для schedule
@pytest.fixture(scope="module")
def mock_schedule():
    with patch('schedule.run_pending') as mock:
        yield mock

# Мок для time.sleep
@pytest.fixture(scope="module")
def mock_time():
    with patch('time.sleep') as mock:
        yield mock

# Мок для сетевых вызовов (например, новости)
@pytest.fixture(scope="module")
def mock_news():
    with patch('assistant.GetMoscowNewsFromRss.GetMoscowNewsFromRss') as mock:
        yield mock

# Тесты для прослушивания ключевого слова
def test_listenForWakeWord(mock_speak, mock_recognizer, mock_schedule):
    with patch('assistant.ProcessingVoiceInput.listenForCommands') as mock_listen:
        listenForWakeWord()
        mock_listen.assert_called_once()
        mock_speak.assert_called_once()

# Тест неизвестной команды
def test_executeCommand_unknown_command(mock_speak):
    command = "какой курс доллара"
    with patch('builtins.input', return_value=command):
        with patch('webbrowser.open') as mock_open:
            executeCommand(command)
            mock_speak.assert_called_with("Неизвестная команда. Попробуйте снова.")
            mock_open.assert_called_once_with(f"https://yandex.ru/search/?text={command}")

# Тест известной команды
def test_executeCommand_known_command(mock_speak):
    command = "здравствуйте"
    with patch('assistant.ProcessingVoiceInput.Greetings.Greetings') as mock_greetings:
        executeCommand(command)
        mock_greetings().playGreetings.assert_called_once()
        mock_speak.assert_called_with("Здравствуйте!")

# Тест создания заметки
def test_create_note_interaction(mock_speak):
    with patch('builtins.input', return_value="Тестовая заметка"):
        with patch('assistant.NoteManagerClass.NotesManager.createNote') as mock_create_note:
            from src import createNoteInteraction
            createNoteInteraction()
            mock_create_note.assert_called_with("Тестовая заметка")
            mock_speak.assert_called_with("Заметка создана.")

# Тест удаления заметки
def test_delete_note_interaction(mock_speak):
    with patch('assistant.NoteManagerClass.NotesManager.readNotes', return_value=[{'text': 'Заметка 1'}, {'text': 'Заметка 2'}]):
        with patch('builtins.input', return_value="1"):
            with patch('assistant.NoteManagerClass.NotesManager.deleteNote') as mock_delete_note:
                from src import deleteNoteInteraction
                deleteNoteInteraction()
                mock_delete_note.assert_called_with(1)
                mock_speak.assert_called_with("Заметка удалена.")

# Тест напоминания
def test_connectReminder(mock_speak, mock_time):
    with patch('builtins.input', side_effect=["2024", "12", "14", "15", "30", "Тестовое напоминание"]):
        with patch('assistant.Reminder.setReminder') as mock_setReminder:
            from src import connectReminder
            connectReminder()
            mock_setReminder.assert_called_once_with("Тестовое напоминание", 2024, 12, 14, 15, 30)
            mock_speak.assert_called_with("Напоминание установлено.")
