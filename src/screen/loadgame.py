import pygame
from actions.actions import actions
from entities.snake import snake
from snakemap.snakemap import snakemap

class Screen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Pysnake")
        self.clock = pygame.time.Clock()

        self.loop()

    def draw_screen(self):
        black = (0, 0, 0)
        white = (255, 255, 255)
        green = (0, 255, 0)
        self.screen.fill(white)
        for y in range(10):
            for x in range(10):
                if snakemap.grid[y][x] == 1:
                    pygame.draw.rect(self.screen, black, (y*80, x*80, 80, 80))
                elif snakemap.grid[y][x] == 2:
                    pygame.draw.rect(self.screen, green, (y*80, x*80, 80, 80))

        pygame.display.flip()
        self.clock.tick(2)

    def loop(self):
        while True:
            actions.check_actions()
            snake.move_snake()
            self.draw_screen()


screen = Screen()

if __name__ == "__main__":
    Screen()
