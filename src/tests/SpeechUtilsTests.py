from unittest.mock import patch, MagicMock
from src.assistant.SpeechUtils import speak  # Путь к функции speak


@patch('src.assistant.SpeechUtils.pyttsx3.init')  # Патчим pyttsx3.init
def test_speak(mock_init):
    """
    Тестируем функцию speak, чтобы убедиться, что она правильно вызывает методы
    pyttsx3 для озвучивания текста.
    """
    # Создаем мок для объекта, возвращаемого pyttsx3.init
    mock_engine = MagicMock()
    mock_init.return_value = mock_engine  # mock_init вернет этот объект при вызове

    # Тестируем функцию speak
    test_text = "Привет, как дела?"

    print("Calling speak function...")  # Для дебага
    speak(test_text)

    # Печатаем информацию о вызове pyttsx3.init
    print("Was pyttsx3.init called?", mock_init.called)  # Проверяем, был ли вызван pyttsx3.init

    # Печатаем все вызовы для мокированного объекта
    print("Was engine.say called?", mock_engine.say.call_args_list)  # Проверяем, был ли вызван say
    print("Was engine.runAndWait called?", mock_engine.runAndWait.call_args_list)  # Проверяем, был ли вызван runAndWait

    # Проверяем, что engine.say был вызван с правильным текстом
    mock_engine.say.assert_called_with(test_text)  # Проверяем, что say был вызван с правильным текстом

    # Проверяем, что engine.runAndWait был вызван
    mock_engine.runAndWait.assert_called_once()  # Проверяем, что runAndWait был вызван один раз
