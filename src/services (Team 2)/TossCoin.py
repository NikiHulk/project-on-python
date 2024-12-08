import random

from SpeechUtils import speak


class TossCoin:

    def tossCoin():
        config = ["орел","решка"]
        TossCoinResult = random.choice(config)
        if TossCoinResult == "решка":
            print(f"Вам выпала {TossCoinResult}")
            speak(f"Вам выпала {TossCoinResult}")
        if TossCoinResult == "орёл":
            print(f"Вам выпал {TossCoinResult}")
            speak(f"Вам выпал {TossCoinResult}")


if __name__ == "__main__":
    toss = TossCoin()
    toss.tossCoin()