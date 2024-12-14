import random

from SpeechUtils import speak


class Greetings:
    def playGreetings(self, name="друг"):
        """Приветствует пользователя с использованием его имени (по умолчанию 'друг')."""
        config = [
            f"Здарова, {name}!",
            f"Привет , мой друг {name}!",
            "ЧЁ надо?",
            f"Привет, кожаный {name}!",
            "На связи!", "Здравствуйте! Или, как говорят оптимисты, 'привет!'", "What's up",
            "Как давно мы не виделись!", "Добрый день, коллеги!", "Салам", "Hi", "Hello",
            "Моё почтение", "Явился не запылился", "Aloha!", f"Салют, {name}",
            "Тысяча чертей, вот это встреча!", "Какие люди и без охраны", "Рад тебя видеть",
            "Здравия желаю", "Готова к вашим услугам", "Сколько лет, сколько зим"
        ]
        greetingMassage = random.choice(config)
        print(greetingMassage)
        speak(greetingMassage)

if __name__ == "__main__":
    speak("Введите ваше имя")
    name = input("Введите ваше имя: ")  # Получаем имя пользователя
    greetings = Greetings()
    greetings.playGreetings(name)
