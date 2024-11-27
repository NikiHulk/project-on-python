import random


class Greetings:

    def playGreetings(self):
        config = ["Здарова, чепуха!", "Привет, мой друг!", "ЧЁ надо?", "Привет, кожаный", "На связи!"]
        print(random.choice(config))


if __name__ == "__main__":
    greetings = Greetings()
    greetings.playGreetings()
