import pyttsx3

engine = pyttsx3.init()

def speak(text):
    """
    Произносит текст с помощью библиотеки pyttsx3.

    Args:
        text (str): Текст для произнесения.
    """

    engine.say(text)
    engine.runAndWait()