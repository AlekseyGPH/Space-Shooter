import pygame
from const import *

class Shield(pygame.sprite.Sprite):

    def __init__(self, ship):
        pygame.sprite.Sprite.__init__(self)
        self.ship = ship
        self.image = pygame.image.load('images/shield1.png')
        self.rect = self.image.get_rect()
        self.rect.center = self.ship.rect.center
        self.hide = False
        self.radius = self.rect.width // 2
        self.last_update = pygame.time.get_ticks()
        self.ship.shield = True
        

    def update(self):
        if self.hide:
            self.rect.center = (self.ship.rect.centerx,
                                SCREEN_HEIGHT + self.rect.height // 2)
            self.ship.shield = False
        else:
            self.rect.center = self.ship.rect.center
        now = pygame.time.get_ticks()
        if now - self.last_update > 10000:
            self.last_update = now
            self.hide = True


