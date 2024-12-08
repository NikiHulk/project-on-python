import random


class Greetings:

    def playGreetings(self):
        config = ["Здарова, чепуха!", "Привет, мой друг!", "ЧЁ надо?", "Привет, кожаный", "На связи!", "Привет! Сегодня у вас хорошее настроение, или вам просто лень его портить?",
                  " Здравствуйте! Или, как говорят оптимисты, 'привет!'", "What's up", "Как давно мы не виделись!"]
        print(random.choice(config))


if __name__ == "__main__":
    greetings = Greetings()
    greetings.playGreetings()
