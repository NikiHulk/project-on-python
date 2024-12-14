import unittest
from unittest.mock import patch
import sys
from io import StringIO
from src.assistant.Farewell import Farewell  # Путь импорта зависит от структуры проекта


class TestFarewell(unittest.TestCase):

    @patch('random.choice')
    @patch('sys.exit')
    def test_farewellAndQuit(self, mock_exit, mock_random_choice):
        # Мокаем вывод случайного прощального сообщения
        mock_random_choice.return_value = "Прощай!"

        # Мокаем sys.exit, чтобы не завершать программу во время теста
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            farewell = Farewell()
            farewell.farewellAndQuit()

            # Проверяем, что выбранное прощальное сообщение было выведено
            self.assertIn("Прощай!", mock_stdout.getvalue())

            # Проверяем, что sys.exit был вызван
            mock_exit.assert_called_once()

    @patch('random.choice')
    @patch('sys.exit')
    def test_random_farewell(self, mock_exit, mock_random_choice):
        # Проверим, что случайное сообщение из списка действительно выбирается
        mock_random_choice.return_value = "Пока!"

        # Мокаем sys.exit, чтобы не завершать программу во время теста
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            farewell = Farewell()
            farewell.farewellAndQuit()

            # Проверяем, что выбранное случайное сообщение выведено в stdout
            self.assertIn("Пока!", mock_stdout.getvalue())
            mock_exit.assert_called_once()


if __name__ == '__main__':
    unittest.main()
