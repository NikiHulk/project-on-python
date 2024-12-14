# tests/VoiceAssistantTests.py

from unittest.mock import patch
from src.assistant.VoiceAssistantClass import VoiceAssistant

# Тестирование метода voiceAssistantInforamtion
@patch('src.assistant.VoiceAssistantClass.speak')
def test_voice_assistant_information(mock_speak):
    """Тестируем корректность работы метода voiceAssistantInforamtion."""

    assistant = VoiceAssistant()

    # Мокируем ввод пользователя, если нужно
    with patch('builtins.print') as mock_print:
        assistant.voiceAssistantInforamtion(name="Ева", LanguageOfSpeaking=["Русский", "English"], LanguageOfRecognition=["Русский", "English"])

        # Проверяем, что print был вызван с правильным сообщением
        mock_print.assert_called_once_with(
            "Здравствуйте! Меня зовут Ева \nПостараюсь помочь Вам со всем о чем попросите!"
        )

        # Проверяем, что speak был вызван с тем же сообщением
        mock_speak.assert_called_once_with(
            "Здравствуйте! Меня зовут Ева \nПостараюсь помочь Вам со всем о чем попросите!"
        )

# Тестирование метода с использованием других параметров
@patch('src.assistant.VoiceAssistantClass.speak')
def test_voice_assistant_information_with_default_values(mock_speak):
    """Тестируем метод с использованием значений по умолчанию."""

    assistant = VoiceAssistant()

    with patch('builtins.print') as mock_print:
        assistant.voiceAssistantInforamtion()

        # Проверка, что метод использует значения по умолчанию
        mock_print.assert_called_once_with(
            "Здравствуйте! Меня зовут Ева \nПостараюсь помочь Вам со всем о чем попросите!"
        )

        mock_speak.assert_called_once_with(
            "Здравствуйте! Меня зовут Ева \nПостараюсь помочь Вам со всем о чем попросите!"
        )

# Тестирование метода с изменением имени
@patch('src.assistant.VoiceAssistantClass.speak')
def test_voice_assistant_information_with_custom_name(mock_speak):
    """Тестируем метод с кастомным именем для голосового помощника."""

    assistant = VoiceAssistant()

    with patch('builtins.print') as mock_print:
        assistant.voiceAssistantInforamtion(name="Алиса")

        # Проверка, что метод использует переданное имя
        mock_print.assert_called_once_with(
            "Здравствуйте! Меня зовут Алиса \nПостараюсь помочь Вам со всем о чем попросите!"
        )

        mock_speak.assert_called_once_with(
            "Здравствуйте! Меня зовут Алиса \nПостараюсь помочь Вам со всем о чем попросите!"
        )
