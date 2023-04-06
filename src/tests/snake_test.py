import unittest
from entities.snake import Snake


class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()

    def test_snake_starting_values(self):
        self.assertEqual(self.snake.length, 2)
        self.assertEqual(self.snake.x, 2)
        self.assertEqual(self.snake.y, 4)
        self.assertEqual(self.snake.up, False)
        self.assertEqual(self.snake.down, False)
        self.assertEqual(self.snake.left, False)
        self.assertEqual(self.snake.right, True)

    def test_snake_turns_correctly(self):
        self.snake.moveleft()
        self.assertEqual(self.snake.left, False)
        self.assertEqual(self.snake.right, True)
        self.snake.moveup()
        self.assertEqual(self.snake.up, True)
        self.assertEqual(self.snake.right, False)
        self.snake.movedown()
        self.assertEqual(self.snake.down, False)
        self.assertEqual(self.snake.up, True)
        self.snake.moveleft()
        self.assertEqual(self.snake.left, True)
        self.assertEqual(self.snake.up, False)
        self.snake.moveright()
        self.assertEqual(self.snake.right, False)
        self.assertEqual(self.snake.left, True)
        self.snake.movedown()
        self.assertEqual(self.snake.down, True)
        self.assertEqual(self.snake.left, False)
        self.snake.moveup()
        self.assertEqual(self.snake.up, False)
        self.assertEqual(self.snake.down, True)
        self.snake.moveright()
        self.assertEqual(self.snake.right, True)
        self.assertEqual(self.snake.down, False)

    def test_adding_length_works(self):
        snake = Snake()
        snake.add_length()
        self.assertEqual(snake.length, 3)

    def test_moving_snake_works(self):
        snake = Snake()
        self.assertEqual(snake.y, 4)
        self.assertEqual(snake.x, 2)
        self.assertEqual(snake.right, True)
        snake.move_snake()
        self.assertEqual(snake.y, 4)
        self.assertEqual(snake.x, 3)
        snake.moveup()
        snake.move_snake()
        self.assertEqual(snake.y, 3)
        self.assertEqual(snake.x, 3)