import random
import sys  # Импортируем sys для использования sys.exit()

class Farewell:
    def farewellAndQuit(self):
        config = ["Пока!", "Прощай!", "Наконец-то!", "Фух, наконец-то он отстал!",
                  "Пока, кожаный!", "Сегодня ты не общительный! До встречи"]
        print(random.choice(config))
        sys.exit()  # Завершаем программу с использованием sys.exit()

if __name__ == "__main__":
    farewell = Farewell()
    farewell.farewellAndQuit()
