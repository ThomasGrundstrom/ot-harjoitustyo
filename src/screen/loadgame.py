import pygame

class Screen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1300, 1300))
        pygame.display.set_caption("Pysnake")