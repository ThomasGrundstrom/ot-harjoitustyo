from entities.apples import apple


class Snake:

    # Class that keeps track of the snake's positions and movement direction, and turns the snake.

    def __init__(self):

        # Constructor that initializes the starting position, length, and direction of the snake.

        self.x = 4
        self.y = 4
        self.direction = 1
        self.moving = False
        self.changeddirections = False
        self.positions = [(3, 4), (4, 4)]

    def moveup(self):

        # Changes the snake's movement direction to up, if the current direction is right or left.

        self.moving = True
        if (self.direction == 1 or self.direction == 3) and not self.changeddirections:
            self.direction = 0
            self.changeddirections = True

    def movedown(self):

        # Changes the snake's movement direction to down, if the current direction is right or left.

        self.moving = True
        if (self.direction == 1 or self.direction == 3) and not self.changeddirections:
            self.direction = 2
            self.changeddirections = True

    def moveleft(self):

        # Changes the snake's movement direction to left, if the current direction is up or down.

        if (self.direction == 0 or self.direction == 2) and not self.changeddirections:
            self.direction = 3
            self.changeddirections = True

    def moveright(self):

        # Changes the snake's movement direction to right, if the current direction is up or down.

        self.moving = True
        if (self.direction == 0 or self.direction == 2) and not self.changeddirections:
            self.direction = 1
            self.changeddirections = True

    def move_snake(self):

        # Moves snake towards the direction it's facing. If an apple is eaten, snake gains 1 square in length.

        if self.moving:
            if self.direction == 0:
                self.y -= 1
            elif self.direction == 2:
                self.y += 1
            elif self.direction == 3:
                self.x -= 1
            elif self.direction == 1:
                self.x += 1
            if self.positions[-1] != (apple.y, apple.x):
                self.positions.pop(0)
            elif self.positions[-1] == (apple.y, apple.x):
                apple.spawn()
            self.positions.append((self.x, self.y))
            self.changeddirections = False

    def set_stationary(self):

        # Stops snake's movement, used when game ends.

        self.moving = False


snake = Snake()
