from entities.snake import snake
from actions.actions import actions
from entities.apples import apple
from score.scorecounter import scorecounter


class Gamemap:

    # Class that creates the map that the game is played on, and updates the positions of the objects on the map.

    def __init__(self):

        # Constructor of the class that initializes the map as an array and places the objects in their starting positions.

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
        self.gamewon = False
        self.gamelost = False

    def updateavailable(self):

        # Updates the list that contains the coordinates of empty squares on the map.

        tempavailable = []
        for y in range(1, 11):
            for x in range(1, 11):
                if self.grid[y][x] == 0:
                    tempavailable.append((y, x))
        self.zeros = tempavailable
        if len(self.zeros) == 0:
            self.wingame()

    def wingame(self):

        # Stops the snake's movement and sets the state of the game as won.

        snake.set_stationary()
        self.gamewon = True

    def losegame(self):

        # Stops the snake's movement and sets the state of the game as lost.

        snake.set_stationary()
        self.gamelost = True

    def update(self):

        # Updates the positions of the objects on the map according to the inputs the user makes. Updates the state of the game if game is won or lost.

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
        if actions.restarting:
            self.restart()
        return self.grid

    def restart(self):
        self.grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                     [1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1],
                     [1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                     [1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        snake.x = 4
        snake.y = 4
        snake.direction = 1
        snake.moving = False
        snake.changeddirections = False
        snake.positions = [(3, 4), (4, 4)]
        apple.y = 7
        apple.x = 7
        apple.available = []
        scorecounter.score = 0
        self.gamewon = False
        self.gamelost = False
        actions.restarting = False


snakemap = Gamemap()
