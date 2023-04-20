from entities.apples import apple


class Snake:
    def __init__(self):
        self.x = 4
        self.y = 4
        self.up = False
        self.down = False
        self.left = False
        self.right = True
        self.changeddirections = False
        self.positions = [(4, 3), (4, 4)]

    def moveup(self):
        if (self.left or self.right) and not self.changeddirections:
            self.right = False
            self.left = False
            self.up = True
            self.changeddirections = True

    def movedown(self):
        if (self.left or self.right) and not self.changeddirections:
            self.right = False
            self.left = False
            self.down = True
            self.changeddirections = True

    def moveleft(self):
        if (self.up or self.down) and not self.changeddirections:
            self.up = False
            self.down = False
            self.left = True
            self.changeddirections = True

    def moveright(self):
        if (self.up or self.down) and not self.changeddirections:
            self.up = False
            self.down = False
            self.right = True
            self.changeddirections = True

    def move_snake(self):
        if self.up:
            self.y -= 1
        elif self.down:
            self.y += 1
        elif self.left:
            self.x -= 1
        elif self.right:
            self.x += 1
        if self.positions[-1] != (apple.y, apple.x):
            self.positions.pop(0)
        elif self.positions[-1] == (apple.y, apple.x):
            apple.spawn()
        self.positions.append((self.x, self.y))
        self.changeddirections = False


snake = Snake()
