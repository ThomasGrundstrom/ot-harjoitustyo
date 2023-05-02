import pygame


class Startmenuactions:

    # Class that checks the actions the user makes when the game is in the start menu state.

    def __init__(self):

        # Constructor of the class, that introduces the possibility to use pygame for the class.

        pygame.init()

    def check_actions(self):

        # Observes the actions of the user in the start menu.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(340, 300, 136, 68).collidepoint(event.pos):
                    return "start"


startmenuactions = Startmenuactions()
