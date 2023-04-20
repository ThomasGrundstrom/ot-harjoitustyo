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
        self.gamelost = False

    def updateavailable(self):
        tempavailable = []
        for y in range(1, 11):
            for x in range(1, 11):
                if self.grid[y][x] == 0:
                    tempavailable.append((y, x))
        self.zeros = tempavailable

    def losegame(self):
        self.gamelost = True

    def update(self):
        actions.check_actions()
        snake.move_snake()
        if snake.positions[-1][0] == 0 or snake.positions[-1][0] == 11:
            self.losegame()
        if snake.positions[-1][1] == 0 or snake.positions[-1][1] == 11:
            self.losegame()
        for i in range(len(snake.positions)):
            for j in range(i+1, len(snake.positions)):
                if snake.positions[i] == snake.positions[j]:
                    self.losegame()
        self.updateavailable()
        apple.set_available(self.zeros)
        for y in range(12):
            for x in range(12):
                if (y, x) in snake.positions:
                    self.grid[y][x] = 2
                elif (y, x) not in snake.positions and self.grid[y][x] != 1:
                    self.grid[y][x] = 0
                if y == apple.y and x == apple.x and (apple.y, apple.x) not in snake.positions:
                    self.grid[y][x] = 3
        return self.grid


snakemap = Gamemap()
