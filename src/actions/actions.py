import pygame
from entities.snake import snake


class Actions:

    # Class that observes the inputs of the user while the game is running.

    def __init__(self):

        # Constructor that introduces pygame and indicates when game is restarting.

        pygame.init()
        self.restarting = False

    def check_actions(self):

        # Observes the user's inputs and turns the snake's direction. If r key is pressed, restarts the game.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.moveup()
                if event.key == pygame.K_DOWN:
                    snake.movedown()
                if event.key == pygame.K_LEFT:
                    snake.moveleft()
                if event.key == pygame.K_RIGHT:
                    snake.moveright()
                if event.key == pygame.K_r:
                    self.restarting = True


actions = Actions()
