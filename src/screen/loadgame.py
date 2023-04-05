import pygame

class Screen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 960))
        pygame.display.set_caption("Pysnake")
        self.clock = pygame.time.Clock()

        self.loop()
    
    def draw_screen(self):
        black = (0, 0, 0)
        white = (255, 255, 255)
        self.screen.fill(white)
        pygame.display.flip()
        self.clock.tick(60)

    def loop(self):
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()
            self.draw_screen()

if __name__ == "__main__":
    Screen()