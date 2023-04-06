import pygame
from actions.actions import actions
from entities.snake import snake


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
        self.screen.fill(white)
        pygame.display.flip()
        self.clock.tick(60)

    def loop(self):
        while True:
            actions.check_actions()
            snake.move_snake()
            self.draw_screen()


screen = Screen()

if __name__ == "__main__":
    Screen()
