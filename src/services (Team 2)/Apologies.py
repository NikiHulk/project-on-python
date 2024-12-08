import random


class Apologies:
    def playApologies(self):
        config = ["Извините!", "Простите",
                  "Пардон", "Виноват", "Это моя вина!", "Прости, я пыталась", "меня подменили роботы",
                  "Извините, я не хотела вас обидеть. Хотя, возможно, я этого и хотела, но потом передумала"]
        print(random.choice(config))


if __name__ == "__main__":
    apologies = Apologies()
    apologies.playApologies()
