import random


class Apple:
    def __init__(self):
        self.y = 7
        self.x = 7
        self.available = []
    
    def set_available(self, available):
        self.available = available

    def spawn(self):
        position = random.randint(0, len(self.available) - 1)
        self.y = self.available[position][0]
        self.x = self.available[position][1]


apple = Apple()
