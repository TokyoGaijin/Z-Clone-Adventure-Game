import pygame
import colorswatch as cs

class Player(object):
    def __init__(self, surface, startX, startY):
        self.surface = surface
        self.posX = startX
        self.posY = startY
        self.size = 16 # for refactoring purposes, a size of 16x16
        self.sword_width = 3
        self.swordX = self.posX + 6
        self.swordY = self.posY + self.size
        self.playerRect = pygame.Rect(self.posX, self.posY, self.size, self.size)
        self.swordRect = pygame.Rect(self.swordX, self.swordY, self.sword_width, self.size)
        self.swordSideRect = pygame.Rect(self.swordX, self.swordY, self.size, self.sword_width)
        self.sword = self.swordRect
        self.rectColor = cs.green["pygame"]
        self.swordColor = cs.gray["pygame"]
        self.speed = 2
        self.attack_timer = 0
        self.isAttacking = False
        self.sword_strength = 1
        self.health = 3


    def update_sword(self, direction):
        if direction == "down":
            self.sword = self.swordRect
            self.swordRect.x = self.posX + 6
            self.swordRect.y = self.posY + self.size
        if direction == "up":
            self.sword = self.swordRect
            self.swordRect.x = self.posX + 6
            self.swordRect.y = self.posY - self.size
        if direction == "left":
            self.sword = self.swordSideRect
            self.swordSideRect.x = self.posX - self.size
            self.swordSideRect.y = self.posY + 6
        if direction == "right":
            self.sword = self.swordSideRect
            self.swordSideRect.x = self.posX + self.size
            self.swordSideRect.y = self.posY + 6

    def move(self, direction):
        if direction == "left":
            self.playerRect.x -= self.speed
        if direction == "right":
            self.playerRect.x += self.speed
        if direction == "up":
            self.playerRect.y -= self.speed
        if direction == "down":
            self.playerRect.y += self.speed

        self.posX, self.posY = self.playerRect.x, self.playerRect.y
        self.update_sword(direction)

    def attack(self):
        pygame.draw.rect(self.surface, self.swordColor, self.sword)



    def controls(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.move("left")
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.move("right")
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.move("up")
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.move("down")

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.attack_timer += 1
        else:
            self.attack_timer = 0

        if self.attack_timer > 0 and self.attack_timer <= 10:
            self.isAttacking = True
        else:
            self.isAttacking = False

        self.controls()


    def draw(self):
        pygame.draw.rect(self.surface, self.rectColor, self.playerRect)
        if self.isAttacking:
            self.attack()