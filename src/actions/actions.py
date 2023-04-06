import pygame
from entities.snake import snake


class Actions:
    def __init__(self):
        pygame.init()

    def check_actions(self):
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


actions = Actions()
