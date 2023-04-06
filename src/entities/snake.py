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

    def eat_apple(self):
        return True

    def move_snake(self):
        if self.up:
            self.y -= 1
        elif self.down:
            self.y += 1
        elif self.left:
            self.x -= 1
        elif self.right:
            self.x += 1
        self.positions.pop(0)
        self.positions.append((self.y, self.x))


snake = Snake()
