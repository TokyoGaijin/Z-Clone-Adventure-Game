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
        if player.playerRect.colliderect(structs.hitbox):
            if player.playerRect.right >= structs.hitbox.left and player.playerRect.left < structs.hitbox.left:
                player.playerRect.right = structs.hitbox.left
            elif player.playerRect.left <= structs.hitbox.right and player.playerRect.right > structs.hitbox.right:
                player.playerRect.left = structs.hitbox.right
            if player.playerRect.bottom >= structs.hitbox.top and player.playerRect.top < structs.hitbox.top:
                player.playerRect.bottom = structs.hitbox.top
            elif player.playerRect.top <= structs.hitbox.bottom and player.playerRect.bottom > structs.hitbox.bottom:
                player.playerRect.top = structs.hitbox.bottom


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

