import unittest
import pygame
from screen.loadgame import Screen


class TestScreen(unittest.TestCase):
    def setUp(self):
        self.screen = Screen()

    def test_screen_initialization(self):
        self.assertEqual(self.screen.screen.get_width(), 816)
        self.assertEqual(self.screen.screen.get_height(), 816)
        self.assertEqual(pygame.display.get_caption()[0], "Pysnake")
        self.assertEqual(self.screen.black, (0, 0, 0))
        self.assertEqual(self.screen.white, (255, 255, 255))
        self.assertEqual(self.screen.green, (0, 255, 0))
        self.assertEqual(self.screen.red, (255, 0, 0))
        self.assertEqual(self.screen.blue, (0, 255, 255))
        self.assertEqual(self.screen.instartmenu, True)

    def test_screen_color_wingame(self):
        self.screen.wingame()
        self.assertEqual(self.screen.screen.get_at((0, 0)), self.screen.white)
        self.assertEqual(self.screen.screen.get_at(
            (0, 815)), self.screen.white)
        self.assertEqual(self.screen.screen.get_at(
            (815, 0)), self.screen.white)
        self.assertEqual(self.screen.screen.get_at(
            (815, 815)), self.screen.white)

    def test_screen_color_losegame(self):
        self.screen.losegame()
        self.assertEqual(self.screen.screen.get_at((0, 0)), self.screen.black)
        self.assertEqual(self.screen.screen.get_at(
            (0, 815)), self.screen.black)
        self.assertEqual(self.screen.screen.get_at(
            (815, 0)), self.screen.black)
        self.assertEqual(self.screen.screen.get_at(
            (815, 815)), self.screen.black)

    def test_startmenu(self):
        self.screen.draw_screen()
        self.assertEqual(self.screen.screen.get_at((0, 0)), self.screen.white)
        self.assertEqual(self.screen.screen.get_at(
            (0, 815)), self.screen.white)
        self.assertEqual(self.screen.screen.get_at(
            (815, 0)), self.screen.white)
        self.assertEqual(self.screen.screen.get_at(
            (815, 815)), self.screen.white)
        self.assertEqual(self.screen.screen.get_at(
            (340, 300)), self.screen.green)
        self.assertEqual(self.screen.screen.get_at(
            (700, 250)), self.screen.green)
        self.assertEqual(self.screen.screen.get_at(
            (650, 100)), self.screen.green)
        self.assertEqual(self.screen.screen.get_at(
            (450, 100)), self.screen.green)
        self.assertEqual(self.screen.screen.get_at(
            (200, 50)), self.screen.green)
        self.assertEqual(self.screen.screen.get_at(
            (150, 50)), self.screen.green)
        self.assertEqual(self.screen.screen.get_at(
            (100, 150)), self.screen.green)
        self.assertEqual(self.screen.screen.get_at(
            (150, 350)), self.screen.green)
        self.assertEqual(self.screen.screen.get_at(
            (150, 500)), self.screen.green)
        self.assertEqual(self.screen.screen.get_at(
            (300, 450)), self.screen.green)
        self.assertEqual(self.screen.screen.get_at(
            (500, 450)), self.screen.red)
