import pygame
from snakemap.snakemap import snakemap
from score.scorecounter import scorecounter
from actions.startmenuactions import startmenuactions


class Screen:

    # Class that takes care of drawing the pygame display, as well as updating it.

    def __init__(self):

        # The constructor of the class, that initializes the display, and the fonts and colours needed in drawing the display.

        pygame.init()
        self.screen = pygame.display.set_mode((816, 816))
        pygame.display.set_caption("Pysnake")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 28)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.blue = (0, 255, 255)
        self.instartmenu = True

        self.loop()

    def draw_screen(self):

        # Takes care of drawing objects on the screen depending on their positions.

        if not self.instartmenu:
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
            scorefont = pygame.font.SysFont("Arial", 16)
            txt = scorefont.render(
                f"SCORE: {scorecounter.score}", True, self.blue)
            self.screen.blit(txt, (370, 10))

            if snakemap.gamewon:
                self.wingame()

            if snakemap.gamelost:
                self.losegame()

        else:
            self.startscreen()

        pygame.display.flip()
        self.clock.tick(3)

    def loop(self):

        # A loop that runs the game by retrieving updates from the map, and drawing the objects in the corresponding positions on the display.

        while True:
            if startmenuactions.check_actions() == "start":
                self.instartmenu = False
                break
            self.draw_screen()
        while True:
            if scorecounter.score == 97:
                snakemap.wingame()
            snakemap.update()
            self.draw_screen()

    def wingame(self):

        # Displays a victory view on the screen. Runs when game is won.

        txt = self.font.render("CONGRATULATIONS!", True, self.black)
        self.screen.fill(self.white)
        self.screen.blit(txt, (270, 300))

    def losegame(self):

        # Displays a game over view on the screen. Runs when game is lost.

        txt = self.font.render("GAME OVER", True, self.red)
        self.screen.fill(self.black)
        self.screen.blit(txt, (330, 300))

    def startscreen(self):

        # Draws the initial start menu for when the game is started.

        welcometxt = self.font.render("Welcome to Pysnake", True, self.black)
        playbuttontxt = self.font.render("PLAY", True, self.black)
        self.screen.fill(self.white)
        pygame.draw.rect(self.screen, self.green, (340, 300, 136, 68))
        self.screen.blit(welcometxt, (270, 200))
        self.screen.blit(playbuttontxt, (375, 315))
        self.draw_art()

    def draw_art(self):

        # Draws art on the display when the game is in the start menu state.
    
        pygame.draw.rect(self.screen, self.green, (700, 250, 150, 50))
        pygame.draw.rect(self.screen, self.green, (650, 100, 50, 200))
        pygame.draw.rect(self.screen, self.green, (450, 100, 200, 50))
        pygame.draw.rect(self.screen, self.green, (200, 50, 300, 50))
        pygame.draw.rect(self.screen, self.green, (150, 50, 50, 150))
        pygame.draw.rect(self.screen, self.green, (100, 150, 50, 250))
        pygame.draw.rect(self.screen, self.green, (150, 350, 50, 150))
        pygame.draw.rect(self.screen, self.green, (150, 500, 200, 50))
        pygame.draw.rect(self.screen, self.green, (300, 450, 150, 50))
        pygame.draw.rect(self.screen, self.red, (500, 450, 50, 50))


screen = Screen()
