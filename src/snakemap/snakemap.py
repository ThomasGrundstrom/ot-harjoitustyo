from entities.snake import snake

class Gamemap:
    def __init__(self):
        self.map = [[0 for i in range(10)] for j in range(10)]
        for i in range(10):
            self.map[i][0] = 1
            self.map[i][9] = 1
            self.map[0][i] = 1
            self.map[9][i] = 1
            for j in range(10):
                if i == snake.y and j == snake.x:
                    self.map[i][j] = 2
    
    def update(self):
        for y in range(10):
            for x in range(10):
                if y == snake.y and x == snake.x:
                    self.map[y][x] = 2
        return self.map

snakemap = Gamemap()