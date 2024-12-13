import pytest
from unittest.mock import patch, MagicMock
from assistant.ProcessingVoiceInput import listenForWakeWord, listenForCommands, executeCommand

# Мок для speak
@pytest.fixture
def mock_speak():
    with patch('assistant.ProcessingVoiceInput.speak') as mock:
        yield mock


# Мок для распознавания речи
@pytest.fixture
def mock_recognizer():
    with patch('speech_recognition.Recognizer.recognize_google', return_value="привет ева"):
        yield


# Мок для функции input (заменяет реальный ввод)
@pytest.fixture
def mock_input():
    with patch('builtins.input', return_value="привет ева"):
        yield


# Мок для веб-браузера
@pytest.fixture
def mock_open():
    with patch('webbrowser.open') as mock:
        yield mock


# Мок для schedule
@pytest.fixture
def mock_schedule_run_pending():
    with patch('schedule.run_pending') as mock:
        yield mock


def test_listenForWakeWord(mock_speak, mock_recognizer, mock_schedule_run_pending):
    # Слушаем слово пробуждения без реального распознавания
    with patch('assistant.ProcessingVoiceInput.listenForCommands') as mock_listen:
        listenForWakeWord()
        mock_listen.assert_called_once()
        mock_speak.assert_called_once()


def test_executeCommand_unknown_command(mock_speak, mock_open):
    command = "какой курс доллара"
    with patch('builtins.input', return_value=command):
        executeCommand(command)
        mock_speak.assert_called_with("Неизвестная команда. Попробуйте снова.")
        mock_open.assert_called_once_with(f"https://yandex.ru/search/?text={command}")


def test_executeCommand_known_command(mock_speak):
    command = "здравствуйте"
    with patch('assistant.ProcessingVoiceInput.Greetings.Greetings') as mock_greetings:
        executeCommand(command)
        mock_greetings().playGreetings.assert_called_once()
        mock_speak.assert_called_with("Здравствуйте!")


def test_create_note_interaction(mock_speak):
    with patch('builtins.input', return_value="Тестовая заметка"):
        with patch('assistant.NoteManagerClass.NotesManager.createNote') as mock_create_note:
            from assistant.ProcessingVoiceInput import createNoteInteraction
            createNoteInteraction()
            mock_create_note.assert_called_with("Тестовая заметка")
            mock_speak.assert_called_with("Заметка создана.")


def test_delete_note_interaction(mock_speak):
    # Мок для удаления заметки
    with patch('assistant.NoteManagerClass.NotesManager.readNotes', return_value=[{'text': 'Заметка 1'}, {'text': 'Заметка 2'}]):
        with patch('builtins.input', return_value="1"):
            with patch('assistant.NoteManagerClass.NotesManager.deleteNote') as mock_delete_note:
                from assistant.ProcessingVoiceInput import deleteNoteInteraction
                deleteNoteInteraction()
                mock_delete_note.assert_called_with(1)
                mock_speak.assert_called_with("Заметка удалена.")


# Пример мокирования long-running функций (например, напоминаний)
@pytest.fixture
def mock_time_sleep():
    with patch('time.sleep') as mock:
        yield mock


# Тест для функции напоминания
def test_connectReminder(mock_speak, mock_time_sleep):
    with patch('builtins.input', side_effect=["2024", "12", "14", "15", "30", "Тестовое напоминание"]):
        with patch('assistant.Reminder.setReminder') as mock_setReminder:
            from assistant.ProcessingVoiceInput import connectReminder
            connectReminder()
            mock_setReminder.assert_called_once_with("Тестовое напоминание", 2024, 12, 14, 15, 30)
            mock_speak.assert_called_with("Напоминание установлено.")
