import random

from SpeechUtils import speak


class TossCoin:
    def tossCoin(self, num_tosses=1):
        """Подбрасывает монету заданное количество раз (по умолчанию 1 раз)."""
        for _ in range(num_tosses):
            result = random.choice(["орел", "решка"])
            if result == "орёл":
                print(f"Монета подброшена: {result}")
                speak(f"Монета подброшена, вам выпал {result}")
            else:
                print(f"Монета подброшена: {result}")
                speak(f"Монета подброшена, вам выпала {result}")

if __name__ == "__main__":
    toss = TossCoin()
    speak("Введите количество подбрасываний монеты")
    num_tosses = int(input("Введите количество подбрасываний монеты: "))  # Запрашиваем количество подбрасываний
    toss.tossCoin(num_tosses)
