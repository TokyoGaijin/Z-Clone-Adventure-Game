import pygame
import colorswatch as cs
import os

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

        self.stand_sprite = [pygame.image.load(os.path.join("hero", "hero_stand_front.png")), pygame.image.load(os.path.join("hero", "hero_stand_left.png")), pygame.image.load(os.path.join("hero", "back_hero_walk_1.png")),
                             pygame.transform.flip(pygame.image.load(os.path.join("hero", "hero_stand_left.png")), True, False)]
        self.stand_dir = {"up": self.stand_sprite[2], "down": self.stand_sprite[0], "left": self.stand_sprite[1], "right": self.stand_sprite[3]}

        self.walk_front_anim = [pygame.image.load(os.path.join("hero", f"front_hero_walk_{i}.png")) for i in range(3)]
        self.walk_back_anim = [pygame.image.load(os.path.join("hero", f"back_hero_walk_{i}.png")) for i in range(3)]
        self.walk_left_anim = [pygame.image.load(os.path.join("hero", f"left_hero_walk_{i}.png")) for i in range(3)]
        self.walk_right_anim = [pygame.transform.flip(pygame.image.load(os.path.join("hero", f"left_hero_walk_{i}.png")), True, False) for i in range(3)]
        self.current_anim = []
        self.isWalking = False
        self.direction = "down"
        self.sword = self.swordRect
        self.rectColor = cs.green["pygame"]
        self.swordColor = cs.gray["pygame"]
        self.speed = 8
        self.attack_timer = 0
        self.isAttacking = False
        self.current_frame = 0
        self.current_timer = 0
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
        self.direction = direction
        self.update_sword(direction)


    def attack(self):
        pygame.draw.rect(self.surface, self.swordColor, self.sword)

    def animate_walk(self, direction):
        if self.current_frame >= 3:
            self.current_frame = 0
        factor = 5
        self.current_timer += 1

        if direction == "right":
            self.current_anim = self.walk_right_anim
        if direction == "left":
            self.current_anim = self.walk_left_anim
        if direction == "up":
            self.current_anim = self.walk_back_anim
        if direction == "down":
            self.current_anim = self.walk_front_anim

        self.surface.blit(self.current_anim[self.current_frame], (self.posX, self.posY))

        if self.current_timer % factor == 0:
            self.current_frame += 1



    def controls(self):
        self.isWalking = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.move("left")
            self.isWalking = True
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.move("right")
            self.isWalking = True
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.move("up")
            self.isWalking = True
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.move("down")
            self.isWalking = True



    def update(self):
        self.speed = 2
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.attack_timer += 1
        else:
            self.attack_timer = 0

        if 0 < self.attack_timer <= 10:
            self.isAttacking = True
        else:
            self.isAttacking = False

        if self.isWalking:
            self.animate_walk(self.direction)

        self.controls()


    def draw(self):
        if not self.isWalking:
            self.surface.blit(self.stand_dir[self.direction], (self.posX, self.posY))
        if self.isAttacking:
            self.attack()