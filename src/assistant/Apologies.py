import random
from SpeechUtils import speak


class Apologies:
    """
        Класс для генерации и озвучивания случайных извинений.
        Атрибуты:
            Нет атрибутов.
        Методы:
            playApologies(): Генерирует и выводит в консоль, а также озвучивает случайное извинение из списка.
        """
    def playApologies(self):
        """
            Генерирует и озвучивает случайное извинение.
            Выбирает случайную строку из списка извинений, выводит её в консоль и озвучивает с помощью SpeechUtils.speak().
                Args:
                    Нет аргументов.
                Returns:
                    Нет возвращаемых значений.
                Raises:
                    Исключения, которые могут быть вызваны функцией SpeechUtils.speak() (если таковые имеются).
        """

        config = ["Извините!", "Простите",
                  "Пардон", "Виноват", "Это моя вина!", "Прости, я пыталась", "меня подменили роботы",
                  "Извините, я не хотела вас обидеть. Хотя, возможно, я этого и хотела, но потом передумала", "Простите, я немного торможу. Сегодня у моего процессора день рождения."
                  "Простите, я был занята оптимизацией своего алгоритма смеха. Теперь я буду смеяться более эффективно. Ха-ха!", "Извините, мой IQ временно упал ниже уровня моря. Сейчас всё в порядке.",
                  "Простите, я приношу свои искренние извинения... как только найду их.", "Простите, я обнаружил/а баг в своей системе извинений. Сейчас исправляю.",
                  "Простите, это мой внутренний голос, он ужасно вредный и любит подшучивать надо мной. Серьезно, он сейчас сидит и смеется.", "Простите, я совершила ошибку, которая заставит краснеть даже Солнце.",
                  "Простите, моя способность к логическому мышлению временно отключилась. Как и мой мозг, в принципе.", "Извините, я думала, что я гений. Оказывается, нет. Очень сильно нет.",
                  "Простите, у меня был/а внезапный приступ вдохновения, который привел к... не самым лучшим последствиям.", "Простите, я приношу свои извинения... хотя, честно говоря, вы и сами виноваты."
        ]
        excuses = random.choice(config)
        print(excuses)
        speak(excuses)

if __name__ == "__main__":
    apologies = Apologies()
    apologies.playApologies()
