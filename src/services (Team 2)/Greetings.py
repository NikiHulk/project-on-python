import random

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
        print(random.choice(config))

if __name__ == "__main__":
    name = input("Введите ваше имя: ")  # Получаем имя пользователя
    greetings = Greetings()
    greetings.playGreetings(name)
