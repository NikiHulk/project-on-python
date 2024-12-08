import random

class TossCoin:
    def tossCoin(self, num_tosses=1):
        """Подбрасывает монету заданное количество раз (по умолчанию 1 раз)."""
        for _ in range(num_tosses):
            result = random.choice(["орел", "решка"])
            print(f"Монета подброшена: {result}")

if __name__ == "__main__":
    toss = TossCoin()
    num_tosses = int(input("Введите количество подбрасываний монеты: "))  # Запрашиваем количество подбрасываний
    toss.tossCoin(num_tosses)
