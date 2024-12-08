import random


class Apologies:
    def playApologies(self):
        config = ["Извините!", "Простите",
                  "Пардон", "Виноват", '']
        print(random.choice(config))


if __name__ == "__main__":
    apologies = Apologies()
    apologies.playApologies()
