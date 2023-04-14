from entities.snake import snake
from actions.actions import actions
from entities.apples import apple


class Gamemap:
    def __init__(self):
        self.grid = [[0 for i in range(12)] for j in range(12)]
        for i in range(12):
            self.grid[i][0] = 1
            self.grid[i][11] = 1
            self.grid[0][i] = 1
            self.grid[11][i] = 1
        self.grid[4][4] = 2
        self.grid[4][3] = 2
        self.grid[7][7] = 3
        self.zeros = []

    def updateavailable(self):
        tempavailable = []
        for y in range(1, 11):
            for x in range(1, 11):
                if self.grid[y][x] == 0:
                    tempavailable.append((y, x))
        self.zeros = tempavailable

    def update(self):
        actions.check_actions()
        snake.move_snake()
        self.updateavailable()
        apple.set_available(self.zeros)
        for y in range(12):
            for x in range(12):
                if (y, x) in snake.positions:
                    self.grid[y][x] = 2
                elif (y, x) not in snake.positions and self.grid[y][x] != 1:
                    self.grid[y][x] = 0
                if y == apple.y and x == apple.x and not (apple.y, apple.x) in snake.positions:
                    self.grid[y][x] = 3
        return self.grid


snakemap = Gamemap()
