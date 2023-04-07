import pygame
from actions.actions import actions
from entities.snake import snake
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
        self.screen.fill(white)
        for y in range(12):
            for x in range(12):
                if snakemap.grid[y][x] == 1:
                    pygame.draw.rect(self.screen, black, (y*68, x*68, 68, 68))
                elif snakemap.grid[y][x] == 2:
                    pygame.draw.rect(self.screen, green, (y*68, x*68, 68, 68))

        pygame.display.flip()
        self.clock.tick(2)

    def loop(self):
        while True:
            actions.check_actions()
            snake.move_snake()
            snakemap.update()
            self.draw_screen()


screen = Screen()
