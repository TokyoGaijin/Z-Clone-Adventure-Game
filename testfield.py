import pygame
import colorswatch
import surface
import player
import gamemap

import time

SURFACE = surface.Surface(256, 240, 60, winName = "TestWin")
player = player.Player(SURFACE.SURFACE, SURFACE.sizeX / 2, SURFACE.sizeX / 2)
map = gamemap.Screen(SURFACE.SURFACE)

def init():
    map.init()
    map.build_maps()

def check_collisions():
    for structs in map.current_map:
        if player.playerRect.colliderect(structs.hitbox):
            print(player.playerRect, structs.hitbox)
            if player.playerRect.right - 1 >= structs.hitbox.left and player.playerRect.left < structs.hitbox.left:
                player.playerRect.right = structs.hitbox.left + 1
            elif player.playerRect.left <= structs.hitbox.right - 1 and player.playerRect.right - 1 > structs.hitbox.right - 1:
                player.playerRect.left = structs.hitbox.right - 1
            if player.playerRect.bottom - 1 >= structs.hitbox.top and player.playerRect.top < structs.hitbox.top:
                player.playerRect.bottom = structs.hitbox.top + 1
            elif player.playerRect.top <= structs.hitbox.bottom - 1 and player.playerRect.bottom - 1 > structs.hitbox.bottom - 1:
                player.playerRect.top = structs.hitbox.bottom - 1
            time.sleep(0.1)
            


def update():
    player.update()
    check_collisions()

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

