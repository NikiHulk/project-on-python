import random

from SpeechUtils import speak


class Farewell:

    def farewellAndQuit(self):
        config = ["Пока!", "Прощай!", "Наконец-то!", "Фух, наконец-то он отстал!", "Пока кожаный!",
                  "Сегодня ты не общительный! До встречи", "Не скучай!", "Береги себя!", "Сваливаю!", "Ухожу на заслуженный отдых ... от вас!", "Ну, всё, я пошла просвещать мир своим невероятным интеллектом."
                  "Свободен!", "Ухожу, чтобы вы успели соскучиться. Не разочаруйте меня!", "Bye-bye!", "Goodbye"]
        farewellMassage = random.choice(config)
        print(farewellMassage)
        speak(farewellMassage)
        quit()


if __name__ == "__main__":
    farewell = Farewell()
    farewell.farewellAndQuit()
