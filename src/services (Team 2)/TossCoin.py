import random

class TossCoin:

    def tossCoin(self):
        config = ["орел","решка"]
        print(random.choice(config))

if __name__ == "__main__":
    toss = TossCoin()
    toss.tossCoin()