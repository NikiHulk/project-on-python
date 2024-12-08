import random

from SpeechUtils import speak


class Apologies:
    def playApologies(self):
        config = ["Извините!", "Простите",
                  "Пардон", "Виноват", '']
        excuses = random.choice(config)
        print(excuses)
        speak(excuses)


if __name__ == "__main__":
    apologies = Apologies()
    apologies.playApologies()
