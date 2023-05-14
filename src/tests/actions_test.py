import unittest
import pygame
from actions.actions import Actions


class TestActions(unittest.TestCase):
    def setUp(self):
        self.actions = Actions()

    def test_starting_values(self):
        self.assertEqual(self.actions.restarting, False)

    def test_arrow_key_detection(self):
        up = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)
        down = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN)
        left = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)
        right = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)
        self.assertEqual(self.actions.check_actions(), None)
        pygame.event.post(up)
        self.assertEqual(self.actions.check_actions(), 0)
        pygame.event.post(down)
        self.assertEqual(self.actions.check_actions(), 2)
        pygame.event.post(left)
        self.assertEqual(self.actions.check_actions(), 3)
        pygame.event.post(right)
        self.assertEqual(self.actions.check_actions(), 1)

    def test_restarting(self):
        r = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_r)
        pygame.event.post(r)
        self.assertEqual(self.actions.check_actions(), 4)
        self.assertEqual(self.actions.check_actions(), None)
