import pyttsx3

engine = pyttsx3.init()

def speak(text):
    """
    Произносит заданный текст с помощью синтезатора речи.

    Аргументы:
    text (str): Текст, который будет произнесен синтезатором речи.

    Возвращает:
    None
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()