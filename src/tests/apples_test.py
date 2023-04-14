import unittest
from entities.apples import Apple

class TestApple(unittest.TestCase):
    def setUp(self):
        self.apple = Apple()
    
    def test_apple_starting_spawn(self):
        self.assertEqual(self.apple.y, 7)
        self.assertEqual(self.apple.x, 7)
        self.assertEqual(self.apple.available, [])
    
    def test_apple_set_available(self):
        self.apple.set_available([(1, 1), (1, 2), (1, 3)])
        self.assertEqual(self.apple.available, [(1, 1), (1, 2), (1, 3)])
    
    def test_available_list_empty(self):
        self.assertEqual(self.apple.spawn(), "game won")
    
    def test_apple_spawn_after_eaten(self):
        self.apple.set_available([(1, 1)])
        self.assertEqual(self.apple.spawn(), (1, 1))
    
    def test_apples_spawn_correctly(self):
        self.apple.set_available([(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)])
        self.assertEqual(self.apple.spawn() in self.apple.available, True)