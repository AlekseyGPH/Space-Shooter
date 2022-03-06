from const import *
import pygame
import random

class Bullet(pygame.sprite.Sprite):

    def __init__(self, startx, starty):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/laserGreen02.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = startx
        self.rect.bottom = starty
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom <= 0:
            self.kill()
