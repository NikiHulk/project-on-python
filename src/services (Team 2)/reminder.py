import schedule
import time
from datetime import datetime
def reminder(text, sound_file=None): #Выводит напоминание текстом
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n[{now}] Напоминание:\n{text}\n")


def SetReminder(text, year, month, day, hour, minute): #напоминание на указанное время
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


if __name__ == "__main__":
    year = int(input("Введите год (YYYY): "))
    month = int(input("Введите месяц (MM): "))
    day = int(input("Введите день (DD): "))
    hour = int(input("Введите час (HH): "))
    minute = int(input("Введите минуту (MM): "))
    reminder_text = input("Введите текст напоминания: ")

    SetReminder(reminder_text, year, month, day, hour, minute)

    while True:
        schedule.run_pending()
        time.sleep(1)  # Проверка каждые 1 секунду


