import pygame
from snakemap.snakemap import snakemap


class Screen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((816, 816))
        pygame.display.set_caption("Pysnake")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 28)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)

        self.loop()

    def draw_screen(self):
        self.screen.fill(self.white)
        for y in range(12):
            for x in range(12):
                if snakemap.grid[y][x] == 1:
                    pygame.draw.rect(self.screen, self.black,
                                     (y*68, x*68, 68, 68))
                elif snakemap.grid[y][x] == 2:
                    pygame.draw.rect(self.screen, self.green,
                                     (y*68, x*68, 68, 68))
                elif snakemap.grid[y][x] == 3:
                    pygame.draw.rect(self.screen, self.red,
                                     (y*68, x*68, 68, 68))

        if snakemap.gamewon:
            self.wingame()

        if snakemap.gamelost:
            self.losegame()

        pygame.display.flip()
        self.clock.tick(3)

    def loop(self):
        while True:
            snakemap.update()
            self.draw_screen()

    def wingame(self):
        txt = self.font.render("CONGRATULATIONS!", True, self.black)
        self.screen.fill(self.white)
        self.screen.blit(txt, (330, 300))

    def losegame(self):
        txt = self.font.render("GAME OVER", True, self.red)
        self.screen.fill(self.black)
        self.screen.blit(txt, (330, 300))


screen = Screen()
