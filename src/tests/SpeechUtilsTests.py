import pytest
from unittest.mock import patch, MagicMock
from src.assistant.SpeechUtils import speak  # Убедитесь, что путь корректен

# Замените путь в зависимости от импорта в SpeechUtils.py
@patch('src.assistant.SpeechUtils.pyttsx3.init')
def test_speak(mock_init):
    """
    Тестируем функцию speak.
    """
    # Настройка мока
    mock_engine = MagicMock()
    mock_init.return_value = mock_engine

    # Тестируемый текст
    test_text = "Привет, как дела?"

    # Вызов функции
    speak(test_text)

    # Проверка вызовов
    print(f"mock_init.called: {mock_init.called}")  # Для диагностики
    mock_init.assert_called_once()  # Убедитесь, что init вызван
    mock_engine.say.assert_called_once_with(test_text)
    mock_engine.runAndWait.assert_called_once()
