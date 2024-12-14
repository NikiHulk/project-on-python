import unittest
from unittest.mock import patch
from datetime import datetime, timedelta

# Импортируем функции из вашего модуля
from src.assistant.Reminder import reminder, setReminder


class TestReminderFunctions(unittest.TestCase):

    @patch('builtins.print')  # Патчим функцию print, чтобы проверить, что выводится на экран
    def test_reminder(self, mock_print):
        # Делаем напоминание с текстом
        test_text = "Не забудь проверить почту!"
        reminder(test_text)

        # Проверяем, что print был вызван с правильным текстом
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mock_print.assert_called_with(f"\n[{now}] Напоминание:\n{test_text}\n")

    @patch('schedule.every')
    @patch('schedule.get_jobs')
    @patch('builtins.print')
    def test_set_reminder_future(self, mock_print, mock_get_jobs, mock_schedule_every):
        # Настроим mock, чтобы проверка напоминания прошла успешно
        mock_schedule_every.return_value = mock_schedule_every
        mock_get_jobs.return_value = []

        # Время напоминания в будущем
        future_time = datetime.now() + timedelta(days=1)
        setReminder("Проверить задачи", future_time.year, future_time.month, future_time.day, future_time.hour,
                    future_time.minute)

        # Проверим, что напоминание установлено
        mock_print.assert_called_with(f"Напоминание установлено на {future_time.strftime('%Y-%m-%d %H:%M')}")

    @patch('builtins.print')
    def test_set_reminder_past(self, mock_print):
        # Время напоминания в прошлом
        past_time = datetime.now() - timedelta(days=1)

        # Проверим, что функция вызывает ошибку
        setReminder("Завершить задачу", past_time.year, past_time.month, past_time.day, past_time.hour,
                    past_time.minute)

        # Ожидаем вывод ошибки
        mock_print.assert_called_with("Ошибка: Время напоминания должно быть в будущем.")

    @patch('builtins.print')
    @patch('schedule.every')
    @patch('schedule.get_jobs')
    def test_set_reminder_unexpected_error(self, mock_get_jobs, mock_schedule_every, mock_print):
        # Моделируем непредвиденную ошибку
        mock_schedule_every.side_effect = Exception("Непредвиденная ошибка")

        future_time = datetime.now() + timedelta(days=1)
        setReminder("Проверить почту", future_time.year, future_time.month, future_time.day, future_time.hour,
                    future_time.minute)

        # Проверяем, что была выведена ошибка
        mock_print.assert_called_with("Непредвиденная ошибка: Непредвиденная ошибка")


if __name__ == '__main__':
    unittest.main()
