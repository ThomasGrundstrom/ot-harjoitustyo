import pygame
from snakemap.snakemap import snakemap


class Screen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((816, 816))
        pygame.display.set_caption("Pysnake")
        self.clock = pygame.time.Clock()

        self.loop()

    def draw_screen(self):
        black = (0, 0, 0)
        white = (255, 255, 255)
        green = (0, 255, 0)
        red = (255, 0, 0)
        self.screen.fill(white)
        for y in range(12):
            for x in range(12):
                if snakemap.grid[y][x] == 1:
                    pygame.draw.rect(self.screen, black, (y*68, x*68, 68, 68))
                elif snakemap.grid[y][x] == 2:
                    pygame.draw.rect(self.screen, green, (y*68, x*68, 68, 68))
                elif snakemap.grid[y][x] == 3:
                    pygame.draw.rect(self.screen, red, (y*68, x*68, 68, 68))

        if snakemap.gamelost:
            self.losegame()

        pygame.display.flip()
        self.clock.tick(5)

    def loop(self):
        while True:
            snakemap.update()
            self.draw_screen()

    def losegame(self):
        black = (0, 0, 0)
        red = (255, 0, 0)
        font = pygame.font.SysFont("Arial", 28)
        txt = font.render("GAME OVER", True, red)
        self.screen.fill(black)
        self.screen.blit(txt, (330, 300))

screen = Screen()
