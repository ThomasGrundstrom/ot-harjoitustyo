import unittest
from entities.snake import Snake


class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()

    def test_snake_starting_values(self):
        self.assertEqual(self.snake.x, 4)
        self.assertEqual(self.snake.y, 4)
        self.assertEqual(self.snake.direction, 1)
        self.assertEqual(self.snake.moving, False)
        self.assertEqual(self.snake.changeddirections, False)
        self.assertEqual(self.snake.positions, [(3, 4), (4, 4)])

    def test_snake_turns_correctly(self):
        self.snake.moveleft()
        self.assertEqual(self.snake.direction, 1)
        self.snake.move_snake()
        self.snake.moveup()
        self.assertEqual(self.snake.direction, 0)
        self.snake.move_snake()
        self.snake.movedown()
        self.assertEqual(self.snake.direction, 0)
        self.snake.move_snake()
        self.snake.moveleft()
        self.assertEqual(self.snake.direction, 3)
        self.snake.move_snake()
        self.snake.moveright()
        self.assertEqual(self.snake.direction, 3)
        self.snake.move_snake()
        self.snake.movedown()
        self.assertEqual(self.snake.direction, 2)
        self.snake.move_snake()
        self.snake.moveup()
        self.assertEqual(self.snake.direction, 2)
        self.snake.move_snake()
        self.snake.moveright()
        self.assertEqual(self.snake.direction, 1)

    def test_moving_snake_works(self):
        self.assertEqual(self.snake.moving, False)
        self.assertEqual(self.snake.changeddirections, False)
        self.snake.moveright()
        self.assertEqual(self.snake.moving, True)
        self.snake.move_snake()
        self.assertEqual(self.snake.changeddirections, False)
        self.assertEqual(self.snake.y, 4)
        self.assertEqual(self.snake.x, 5)
        self.snake.moveup()
        self.snake.move_snake()
        self.assertEqual(self.snake.y, 3)
        self.assertEqual(self.snake.x, 5)

    def test_snake_body_moves_correctly(self):
        self.assertEqual(self.snake.positions, [(3, 4), (4, 4)])
        self.snake.moveright()
        self.snake.move_snake()
        self.assertEqual(self.snake.positions, [(4, 4), (5, 4)])

    def test_snake_stops_moving(self):
        self.assertEqual(self.snake.moving, False)
        self.snake.moveright()
        self.assertEqual(self.snake.moving, True)
        self.snake.set_stationary()
        self.assertEqual(self.snake.moving, False)
