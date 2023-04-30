import pygame


class Startmenuactions:
    def __init__(self):
        pygame.init()

    def check_actions(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(340, 300, 136, 68).collidepoint(event.pos):
                    return "start"


startmenuactions = Startmenuactions()
