import random

from SpeechUtils import speak


class Greetings:

    def playGreetings(self):
        config = ["Здарова, чепуха!", "Привет, мой друг!", "ЧЁ надо?", "Привет, кожаный", "На связи!", "Привет! Сегодня у вас хорошее настроение, или вам просто лень его портить?",
                  " Здравствуйте! Или, как говорят оптимисты, 'привет!'", "What's up", "Как давно мы не виделись!"]
        greeting = random.choice(config)
        print(greeting)
        speak(greeting)


if __name__ == "__main__":
    greetings = Greetings()
    greetings.playGreetings()
