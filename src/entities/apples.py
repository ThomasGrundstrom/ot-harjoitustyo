import random


class Apple:
    def __init__(self):
        self.coordinates = [0, 0]

    def spawn(self):
        y = random.randint(1, 15)
        x = random.randint(1, 15)
        self.coordinates[0] = y
        self.coordinates[1] = x
