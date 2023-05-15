import pygame
import colorswatch
import surface
import player
import gamemap

SURFACE = surface.Surface(256, 240, 60, winName = "TestWin")
player = player.Player(SURFACE.SURFACE, SURFACE.sizeX / 2, SURFACE.sizeX / 2)
map = gamemap.Screen(SURFACE.SURFACE)

def init():
    map.init()
    map.build_maps()


def update():
    player.update()


def draw():
    player.draw()
    map.draw()


def run():
    init()
    while SURFACE.inPlay:

        update()
        draw()
        SURFACE.update()


run() if __name__ == '__main__' else None

