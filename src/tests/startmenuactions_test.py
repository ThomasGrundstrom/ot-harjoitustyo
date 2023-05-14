import unittest
import pygame
from actions.startmenuactions import Startmenuactions

class TestStartmenuactions(unittest.TestCase):
    def setUp(self):
        self.startmenuactions = Startmenuactions()
    
    def test_mouseclicks(self):
        self.assertEqual(self.startmenuactions.check_actions(), None)
        clickinside = pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=(340, 300))
        clickoutside = pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=(0, 0))
        pygame.event.post(clickinside)
        self.assertEqual(self.startmenuactions.check_actions(), "start")
        pygame.event.post(clickoutside)
        self.assertEqual(self.startmenuactions.check_actions(), None)