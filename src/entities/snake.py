from entities.apples import apple

class Snake:
    def __init__(self):
        self.x = 4
        self.y = 4
        self.up = False
        self.down = False
        self.left = False
        self.right = True
        self.positions = [(4, 3), (4, 4)]

    def moveup(self):
        if self.left or self.right:
            self.right = False
            self.left = False
            self.up = True

    def movedown(self):
        if self.left or self.right:
            self.right = False
            self.left = False
            self.down = True

    def moveleft(self):
        if self.up or self.down:
            self.up = False
            self.down = False
            self.left = True

    def moveright(self):
        if self.up or self.down:
            self.up = False
            self.down = False
            self.right = True

    def move_snake(self):
        if self.up:
            self.x -= 1
        elif self.down:
            self.x += 1
        elif self.left:
            self.y -= 1
        elif self.right:
            self.y += 1
        if not self.positions[-1] == (apple.y, apple.x):
            self.positions.pop(0)
        elif self.positions[-1] == (apple.y, apple.x):
            apple.spawn()
        self.positions.append((self.y, self.x))


snake = Snake()
