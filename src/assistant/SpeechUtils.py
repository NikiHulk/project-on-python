import pyttsx3


def speak(text):
    """
    Функция для озвучивания текста с использованием pyttsx3.

    Эта функция инициализирует движок pyttsx3 для синтеза речи и воспроизводит заданный текст.

    Аргументы:
    text (str): Текст, который будет озвучен. Должен быть строкой.

    Пример использования:
    >>> speak("Привет, как дела?")
    """
    print("Calling pyttsx3.init()...")  # Логирование инициализации
    engine = pyttsx3.init()  # Инициализация pyttsx3
    print(f"Engine initialized: {engine}")  # Логируем инициализацию движка

    engine.say(text)  # Говорим текст
    print(f"Say method called with text: {text}")  # Логируем текст, который передан в say

    engine.runAndWait()  # Ожидаем завершения озвучивания
