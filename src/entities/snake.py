class Snake:
    def __init__(self):
        self.length = 2
        self.x = 2
        self.y = 4
        self.up = False
        self.down = False
        self.left = False
        self.right = True
    
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
    
    def add_length(self):
        self.length += 1