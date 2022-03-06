from const import *
import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self,startx,starty):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/space.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image,(480,720))
        self.rect = self.image.get_rect()
