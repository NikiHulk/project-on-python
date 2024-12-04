import random

import Farewell


class Apologies:
    def playApologies(self):
        config = ["Извините!", "Простите",
                  "Пардон", "Виноват", '']
        print(random.choice(config))
        Farewell.Farewell.farewellAndQuit(self=0)


if __name__ == "__main__":
    apologies = Apologies()
    apologies.playApologies()
