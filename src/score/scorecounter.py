class Scorecounter:

    # Class that keeps track of the score.

    def __init__(self):

        # Constructor that initially sets the score and high score to 0.

        self.score = 0
        self.highscore = 0

    def add_score(self):

        # Adds 1 to the score. Changes the high score when necessary.

        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score


scorecounter = Scorecounter()
