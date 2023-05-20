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

def check_collisions():
    for structs in map.current_map:
        while player.playerRect.colliderect(structs.hitbox):
            if player.direction == "right":
                player.playerRect.x -= 1
            if player.direction == "left":
                player.playerRect.x += 1
            if player.direction == "up":
                player.playerRect.y += 1
            if player.direction == "down":
                player.playerRect.y -= 1


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

