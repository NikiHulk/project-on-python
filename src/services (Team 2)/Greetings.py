import random

from SpeechUtils import speak


class Greetings:
    def playGreetings(self, name="друг"):
        """Приветствует пользователя с использованием его имени (по умолчанию 'друг')."""
        config = [
            f"Здарова, {name}!",
            f"Привет, мой друг {name}!",
            "ЧЁ надо?",
            f"Привет, кожаный {name}!",
            "На связи!"
        ]
        greetingMassage = random.choice(config)
        print(greetingMassage)
        speak(greetingMassage)

if __name__ == "__main__":
    speak("Введите ваше имя")
    name = input("Введите ваше имя: ")  # Получаем имя пользователя
    greetings = Greetings()
    greetings.playGreetings(name)
