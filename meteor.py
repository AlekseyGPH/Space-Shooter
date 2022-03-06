from const import *
import pygame
import random

class Meteor(pygame.sprite.Sprite):
    image_name_list = ["meteor_tiny1.png", "meteor_small1.png",
                        "meteor_med1.png", "meteor_big1.png"]
        
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #выдать случайное число от 0 до 3
        m_number = random.randrange(0,len(self.image_name_list))
        self.image = pygame.image.load("images/" +
            Meteor.image_name_list[m_number]).convert_alpha()
        self.image_copy = self.image.copy()
        self.rect = self.image.get_rect()
        self.angle = 0
        self.random_spawn()
        self.last_update = pygame.time.get_ticks()

    def update(self):
        #перемещение
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        #вращение
        self.rotate()
        #выход за границы экрана
        if self.rect.top >= SCREEN_HEIGHT:
            self.random_spawn()
        if self.rect.right <= 0 or self.rect.left >= SCREEN_WIDTH:
            self.random_spawn()

    def random_spawn(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.bottom = random.randint(-SCREEN_HEIGHT,0)
        self.speedy = random.randint(3,5)
        self.speedx = random.randint(-1,1)
        self.rot_speed = random.randint(-5,5)

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 40:
            self.last_update = now
            self.angle = (self.angle + self.rot_speed) % 360
            rot_image = pygame.transform.rotate(self.image_copy, self.angle)
            old_center = self.rect.center
            self.image = rot_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center   
