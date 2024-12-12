import random

from SpeechUtils import speak


class TossCoin:
    def tossCoin(num_tosses=1):
        """Подбрасывает монету заданное количество раз (по умолчанию 1 раз)."""
        for _ in range(num_tosses):
            result = random.choice(["орел", "решка"])
            if result == "орёл":
                print(f"Монета подброшена: {result}")
                speak(f"Монета подброшена, вам выпал {result}")
            else:
                print(f"Монета подброшена: {result}")
                speak(f"Монета подброшена, вам выпала {result}")


