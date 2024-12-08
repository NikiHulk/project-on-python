import random

class Apologies:
    def playApologies(self):
        config = ["Извините!", "Простите", "Пардон", "Виноват"]
        apology = random.choice(config)
        print(apology)
        return apology  # Можно вернуть значение, если нужно использовать его в других местах

if __name__ == "__main__":
    apologies = Apologies()
    apologies.playApologies()
