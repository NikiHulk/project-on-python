import random

from SpeechUtils import speak


class Greetings:
    def playGreetings(self, name="друг"):

        """
        Приветствует пользователя с использованием его имени (по умолчанию 'друг').

        Эта функция выбирает случайное приветственное сообщение из набора фраз и выводит его пользователю.
        Также проигрывается соответствующее сообщение с помощью синтеза речи.

        Параметры:
            name (str): Имя пользователя, которое будет использоваться в приветствии (по умолчанию 'друг').

        Возвращаемое значение:
            None: Функция не возвращает значение, она только выводит на экран приветствие и воспроизводит его голосом.
        """

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

    """
    Главная функция программы. Запрашивает имя пользователя и выводит случайное приветствие с этим именем.
    Также воспроизводит приветствие с помощью синтеза речи.
    """

    speak("Введите ваше имя")
    name = input("Введите ваше имя: ")  # Получаем имя пользователя
    greetings = Greetings()
    greetings.playGreetings(name)
