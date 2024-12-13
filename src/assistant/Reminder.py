import schedule
import time
from datetime import datetime


def reminder(text, sound_file=None):
    """
    Выводит напоминание на консоль.

    Эта функция выводит напоминание в виде текста на консоль с временной меткой, а также может проигрывать звуковой файл.
    В текущей реализации звуковой файл не используется.

    Args:
        text (str): Текст напоминания, который будет выведен на консоль.
        sound_file (str, optional): Путь к звуковому файлу для воспроизведения. В данной реализации не используется.

    Example:
        reminder("Не забудьте купить хлеб!")
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[{now}] Напоминание:\n{text}\n")


def setReminder(text, year, month, day, hour, minute):
    """
    Устанавливает напоминание на указанную дату и время.

    Эта функция позволяет установить напоминание на определенное время, указанное пользователем.
    Напоминание будет срабатывать в указанное время и выводить сообщение на консоль.

    Args:
        text (str): Текст напоминания.
        year (int): Год (например, 2024).
        month (int): Месяц (от 1 до 12).
        day (int): День (от 1 до 31).
        hour (int): Час (от 0 до 23).
        minute (int): Минута (от 0 до 59).

    Raises:
        ValueError: Если время напоминания находится в прошлом.
        Exception: При возникновении других непредвиденных ошибок.

    Example:
        setReminder("Время пить чай!", 2024, 12, 14, 15, 30)
    """
    try:
        reminder_time = datetime(year, month, day, hour, minute)
        if reminder_time <= datetime.now():  # Проверка на то, что время в будущем
            raise ValueError("Время напоминания должно быть в будущем.")

        schedule.every().day.at(reminder_time.strftime("%H:%M")).do(reminder, text, 'path/to/your/sound.mp3')
        print(f"Напоминание установлено на {reminder_time.strftime('%Y-%m-%d %H:%M')}")

    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")
