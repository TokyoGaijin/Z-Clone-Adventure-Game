import pygame
import colorswatch
import surface
import player

SURFACE = surface.Surface(256, 240, 60, winName = "TestWin")
player = player.Player(SURFACE.SURFACE, SURFACE.sizeX / 2, SURFACE.sizeX / 2)

def init():
    pass


def update():
    player.update()


def draw():
    player.draw()


def run():
    while SURFACE.inPlay:

        update()
        draw()
        SURFACE.update()


run() if __name__ == '__main__' else None

