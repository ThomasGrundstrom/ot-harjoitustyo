import unittest
from score.scorecounter import Scorecounter


class TestScorecounter(unittest.TestCase):
    def setUp(self):
        self.scorecounter = Scorecounter()

    def test_starting_values(self):
        self.assertEqual(self.scorecounter.score, 0)
        self.assertEqual(self.scorecounter.highscore, 0)

    def test_score_gets_added(self):
        self.scorecounter.add_score()
        self.assertEqual(self.scorecounter.score, 1)
        self.assertEqual(self.scorecounter.highscore, 1)
        self.scorecounter.highscore = 50
        self.scorecounter.add_score()
        self.assertEqual(self.scorecounter.score, 2)
        self.assertEqual(self.scorecounter.highscore, 50)
