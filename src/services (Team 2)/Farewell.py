import random


class Farewell:

    def farewellAndQuit(self):
        config = ["Пока!", "Прощай!", "Наконец-то!", "Фух, наконец-то он отстал!", "Пока кожаный!",
                  "Сегодня ты не общительный! До встречи"]
        print(random.choice(config))
        quit()


if __name__ == "__main__":
    farewell = Farewell()
    farewell.farewellAndQuit()
