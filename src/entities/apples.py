import random


class Apple:
    def __init__(self):
        self.y = 7
        self.x = 7

    def spawn(self):
        y = random.randint(1, 8)
        x = random.randint(1, 8)
        self.y = y
        self.x = x
