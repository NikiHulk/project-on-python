import random

from SpeechUtils import speak


class Apologies:
    def playApologies(self):
        config = ["Извините!", "Простите",
                  "Пардон", "Виноват", "Это моя вина!", "Прости, я пыталась", "меня подменили роботы",
                  "Извините, я не хотела вас обидеть. Хотя, возможно, я этого и хотела, но потом передумала"]
        excuses = random.choice(config)
        print(excuses)
        speak(excuses)


if __name__ == "__main__":
    apologies = Apologies()
    apologies.playApologies()
