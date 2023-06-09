import pygame
import colorswatch as cs
import os


class world_object(object):
    def __init__(self, surface, posX, posY, objType = None):
        self.surface = surface
        self.posX = posX
        self.posY = posY
        self.objType = objType
        self.tree_dead = pygame.image.load(os.path.join("tiles", "tree_dead.png"))
        self.tree_sakura = pygame.image.load(os.path.join("tiles", "tree_sakura.png"))
        self.tree_green = pygame.image.load(os.path.join("tiles", "tree_green.png"))
        self.size = 16
        self.tree_size = (16, 12, 8, 4)
        self.hitbox = pygame.Rect(self.posX, self.posY, self.size, self.size)
        self.objRect = pygame.Rect(self.posX, self.posY, self.size, self.size)
        self.treeLeafRect = pygame.Rect(self.posX, self.posY, self.tree_size[0], self.tree_size[1])
        self.treeTrunkRect = pygame.Rect(self.treeLeafRect.x + self.tree_size[3], self.treeLeafRect.y +
                                         self.treeLeafRect.height, self.tree_size[2], self.tree_size[3])
        self.rect = pygame.Rect(self.posX, self.posY, self.size, self.size)
        self.greentree_color = cs.jungle["pygame"]
        self.sakuratree_color = cs.sakura["pygame"]
        self.browntree_color = cs.shit["pygame"]
        self.trunk_color = cs.brown["pygame"]


    def draw(self):
        color = None
        # if "tree" in self.objType:
        #     if "green" in self.objType:
        #         color = self.greentree_color
        #     elif "sakura" in self.objType:
        #         color = self.sakuratree_color
        #     elif "brown" in self.objType:
        #         color = self.browntree_color
        #     pygame.draw.rect(self.surface, color, self.treeLeafRect)
        #     pygame.draw.rect(self.surface, self.trunk_color, self.treeTrunkRect)
        tree_image = None
        if "tree" in self.objType:
            if "green" in self.objType:
                tree_image = self.tree_green
            elif "sakura" in self.objType:
                tree_image = self.tree_sakura
            elif "brown" in self.objType:
                tree_image = self.tree_dead

        self.surface.blit(tree_image, (self.posX, self.posY))
