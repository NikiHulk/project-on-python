import random

import Farewell


class Apologies:
    def playApologies(self):
        config = ["Извините! Буду исправляться", "Я в процессе обучения. Осталось недолго! Честно!",
                  "Не обижайте меня, я же учусь!"]
        print(random.choice(config))
        Farewell.Farewell.farewellAndQuit(self=0)


if __name__ == "__main__":
    apologies = Apologies()
    apologies.playApologies()
