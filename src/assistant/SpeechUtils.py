import pyttsx3


def speak(text):
    """
    Функция для озвучивания текста с использованием pyttsx3.

    Аргументы:
    text -- строка, текст, который должен быть озвучен.
    """
    print("Calling pyttsx3.init()...")
    engine = pyttsx3.init()  # Инициализация pyttsx3
    print(f"Engine initialized: {engine}")  # Выводим информацию об инициализации

    engine.say(text)  # Говорим текст
    print(f"Say method called with text: {text}")  # Выводим текст, который передан в say

    engine.runAndWait()  # Ожидаем завершения
