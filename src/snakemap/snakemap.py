from entities.snake import snake

class Gamemap:
    def __init__(self):
        self.grid = [[0 for i in range(10)] for j in range(10)]
        for i in range(10):
            self.grid[i][0] = 1
            self.grid[i][9] = 1
            self.grid[0][i] = 1
            self.grid[9][i] = 1
        self.grid[4][4] = 2
        self.grid[4][3] = 2
    
    def update(self):
        for y in range(10):
            for x in range(10):
                if (y, x) in snake.positions:
                    self.grid[y][x] = 2
                elif (y, x) not in snake.positions and self.grid[y][x] != 1:
                    self.grid[y][x] = 0
        return self.grid

snakemap = Gamemap()