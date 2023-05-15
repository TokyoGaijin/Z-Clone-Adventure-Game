import pygame
import colorswatch as cs

class Surface():
    def __init__(self, sizeX, sizeY, FPS, winName = "PyGame Surface"):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.winName = winName
        self.FPS = FPS
        self.CLOCK = pygame.time.Clock()
        self.screenSize = (sizeX, sizeY)
        self.SURFACE = pygame.display.set_mode(self.screenSize)
        self.BG = cs.z_ground["pygame"]
        self.inPlay = True
        self.fullscreen = False
        pygame.display.set_caption(self.winName)

    def update(self):
        self.CLOCK.tick(self.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.inPlay = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.inPlay = False
        if keys[pygame.K_F11]:
            if self.fullscreen:
                self.SURFACE = pygame.display.set_mode(self.screenSize, pygame.FULLSCREEN)
            else:
                self.SURFACE = pygame.display.set_mode(self.screenSize)


        pygame.display.update()
        self.SURFACE.fill(self.BG)