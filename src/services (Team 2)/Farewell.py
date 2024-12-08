import random
import sys  # Импортируем sys для использования sys.exit()

from SpeechUtils import speak


class Farewell:
    def farewellAndQuit(self):
        config = ["Пока!", "Прощай!", "Наконец-то!", "Фух, наконец-то он отстал!",
                  "Пока, кожаный!", "Сегодня ты не общительный! До встречи"]
        farewellMassage = random.choice(config)
        print(farewellMassage)
        speak(farewellMassage)
        sys.exit()  # Завершаем программу с использованием sys.exit()

if __name__ == "__main__":
    farewell = Farewell()
    farewell.farewellAndQuit()
