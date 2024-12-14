from unittest.mock import patch
from src import Greetings


def test_play_greetings_with_name():
    # Мокируем функцию speak
    with patch('src.assistant.Greetings.speak') as mock_speak:
        # Мокируем random.choice для возвращения определенного приветствия
        with patch('random.choice', return_value=f"Привет , мой друг Иван!"):
            # Создаем экземпляр класса
            greetings = Greetings()

            # Вводим имя
            name = "Иван"

            # Вызовем метод playGreetings
            greetings.playGreetings(name)

            # Проверяем, что speak была вызвана с правильным приветствием
            mock_speak.assert_called_once_with(f"Привет , мой друг Иван!")


def test_play_greetings_without_name():
    # Мокируем функцию speak
    with patch('src.assistant.Greetings.speak') as mock_speak:
        # Мокируем random.choice для возвращения определенного приветствия
        with patch('random.choice', return_value="Здарова, друг!"):
            # Создаем экземпляр класса
            greetings = Greetings()

            # Вызовем метод playGreetings без имени
            greetings.playGreetings()

            # Проверяем, что speak была вызвана с правильным приветствием
            mock_speak.assert_called_once_with("Здарова, друг!")


def test_random_greeting():
    # Мокируем функцию speak
    with patch('src.assistant.Greetings.speak') as mock_speak:
        # Мокируем random.choice для возвращения определенного приветствия
        with patch('random.choice', return_value="Привет , мой друг Иван!"):
            # Создаем экземпляр класса
            greetings = Greetings()

            # Вводим имя
            name = "Иван"

            # Проверяем, что функция speak вызывается с ожидаемым приветствием
            greetings.playGreetings(name)
            mock_speak.assert_called_once_with(f"Привет , мой друг Иван!")
