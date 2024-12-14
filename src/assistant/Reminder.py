import schedule
import time
from datetime import datetime
def reminder(text, sound_file=None): #Выводит напоминание текстом
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[{now}] Напоминание:\n{text}\n")


def setReminder(text, year, month, day, hour, minute): #напоминание на указанное время
    try:
        reminder_time = datetime(year, month, day, hour, minute)
        if reminder_time <= datetime.now():# Проверка на то, что время в будущем
            raise ValueError("Время напоминания должно быть в будущем.")

        schedule.every().day.at(reminder_time.strftime("%H:%M")).do(reminder, text, 'path/to/your/sound.mp3')
        print(f"Напоминание установлено на {reminder_time.strftime('%Y-%m-%d %H:%M')}")

    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")





