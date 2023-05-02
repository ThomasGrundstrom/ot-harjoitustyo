import random
from score.scorecounter import scorecounter


class Apple:

    # Class that manages the apple that's on the screen.

    def __init__(self):

        # Constructor that initializes the starting positions of the apple.

        self.y = 7
        self.x = 7
        self.available = []

    def set_available(self, available):

        # Sets the available squares that an apple can spawn.
        # Args: available: List of the coordinates of the squares that have a value of 0 on the map.

        self.available = available

    def spawn(self):

        # Adds 1 to the scorecounter, spawns an apple in a random place in one of the available squares on the map.

        scorecounter.add_score()
        if len(self.available) > 0:
            position = random.randint(0, len(self.available) - 1)
            self.y = self.available[position][0]
            self.x = self.available[position][1]
            return self.available[position]
        return "game won"


apple = Apple()
