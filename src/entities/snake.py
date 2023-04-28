from entities.apples import apple


class Snake:
    def __init__(self):
        self.x = 4
        self.y = 4
        self.direction = 1
        self.moving = True
        self.changeddirections = False
        self.positions = [(4, 3), (4, 4)]

    def moveup(self):
        if (self.direction == 1 or self.direction == 3) and not self.changeddirections:
            self.direction = 0
            self.changeddirections = True

    def movedown(self):
        if (self.direction == 1 or self.direction == 3) and not self.changeddirections:
            self.direction = 2
            self.changeddirections = True

    def moveleft(self):
        if (self.direction == 0 or self.direction == 2) and not self.changeddirections:
            self.direction = 3
            self.changeddirections = True

    def moveright(self):
        if (self.direction == 0 or self.direction == 2) and not self.changeddirections:
            self.direction = 1
            self.changeddirections = True

    def move_snake(self):
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
        self.moving = False


snake = Snake()
