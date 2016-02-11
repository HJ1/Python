#! usr/bin/env python

import os, sys
import random

import pygame
from pygame.locals import *

import pygu
from pygu.locals import *

from Helper import *
import Locals

class Platform(pygu.sprite.Sprite):

    def __init__(self, pos, check_fall, check_ceiling, check_sides):
        
        pygu.sprite.Sprite.__init__(self)
        self.image = load_image('Pixel Block.bmp', colorkey = True)
        self.rect = self.image.get_rect(topleft = pos)

        self.check_fall = check_fall
        self.check_ceiling = check_ceiling
        self.check_sides = check_sides


class Spikes(pygu.sprite.Sprite):

    def __init__(self, pos):
        
        pygu.sprite.Sprite.__init__(self)
        self.image = load_image('Spikes.bmp', colorkey = True)
        self.rect = self.image.get_rect(topleft = pos)


class Coin(pygu.sprite.Sprite):

    def __init__(self, pos):
        
        pygu.sprite.Sprite.__init__(self)
        self.images = [load_image('Coin 1.bmp', colorkey = True),
                       load_image('Coin 2.bmp', colorkey = True),
                       load_image('Coin 3.bmp', colorkey = True),
                       load_image('Coin 2.bmp', colorkey = True)]
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft = pos)

        self.frame = 0

    def update(self, surface):
        self.frame += 1
        self.image = self.images[self.frame/6%4]


class Boom(pygu.sprite.Sprite):

    def __init__(self, pos):
        
        pygu.sprite.Sprite.__init__(self)
        self.image = load_image('Boom.bmp', colorkey = True)
        self.rect = self.image.get_rect(center = pos)

        self.life = 0

    def update(self, surface):
        self.life += 1
        if self.life >= 40:
            self.kill()
        if not self.life & 2:
            self.image = pygame.transform.flip(self.image, 0, 1)


class VIRUS_DIE(pygu.sprite.Sprite):

    def __init__(self, pos):
        
        pygu.sprite.Sprite.__init__(self)
        self.images = [load_image('VIRUS Die 1.bmp', colorkey = True),
                       load_image('VIRUS Die 2.bmp', colorkey = True),
                       load_image('VIRUS Die 3.bmp', colorkey = True),
                       load_image('VIRUS Die 4.bmp', colorkey = True)]
        self.image = self.images[0]
        self.rect = self.image.get_rect(center = pos)

        self.life = 0

    def update(self, surface):
        self.life += 1
        if self.life >= 16:
            self.kill()
        self.image = self.images[self.life/4%4]



class Bomber(pygu.sprite.Sprite):

    def __init__(self, pos):
    
        pygu.sprite.Sprite.__init__(self)
        self.leftimages = [load_image('Bomber 1.bmp'), load_image('Bomber 2.bmp')]
        self.rightimages = [pygame.transform.flip(load_image('Bomber 1.bmp'), 1, 0),
                            pygame.transform.flip(load_image('Bomber 2.bmp'), 1, 0)]
        self.image = self.leftimages[0]
        self.rect = self.image.get_rect(topleft = pos)

        self.speed = -1*Locals.scale
        self.frame = 0


    def update(self, surface):

        self.rect.move_ip(self.speed, 1*Locals.scale)
        self.frame += 1

        if self.speed > 0:
            self.image = self.rightimages[self.frame/5%2]
        if self.speed < 0:
            self.image = self.leftimages[self.frame/5%2]

        for platform in pygu.sprite.spritecollide(self, self.platforms, 0):
            if platform.check_fall:
                self.check_fall(platform)
            if platform.check_sides:
                self.check_rightwalk(platform)
                self.check_leftwalk(platform)

    def check_fall(self, other):
        if pygu.sprite.Sprite.check_top(self, other, 6*Locals.scale, -3*Locals.scale):
            self.rect.bottom = other.rect.top

    def check_leftwalk(self, other):
        if pygu.sprite.Sprite.check_left(self, other, -1*Locals.scale, 6*Locals.scale):
            self.rect.left = other.rect.right + 2*Locals.scale
            self.speed = 1*Locals.scale

    def check_rightwalk(self, other):
        if pygu.sprite.Sprite.check_right(self, other, 1*Locals.scale, 6*Locals.scale):
            self.rect.right = other.rect.left - 2*Locals.scale
            self.speed = -1*Locals.scale


class VIRUS(pygu.sprite.Sprite):

    def __init__(self, pos):
    
        pygu.sprite.Sprite.__init__(self)
        self.leftimages = [load_image('VIRUS 1.bmp'), load_image('VIRUS 2.bmp')]
        self.rightimages = [pygame.transform.flip(load_image('VIRUS 1.bmp'), 1, 0),
                            pygame.transform.flip(load_image('VIRUS 2.bmp'), 1, 0)]
        self.image = self.leftimages[0]
        self.rect = self.image.get_rect(topleft = pos)

        self.speed = -1*Locals.scale
        self.frame = 0
        self.hp = 5


    def kill(self):
        self.hp -= 1
        if self.hp <= 0:
            pygame.sprite.Sprite.kill(self)
            VIRUS_DIE(self.rect.center)


    def update(self, surface):

        self.rect.move_ip(self.speed, 1*Locals.scale)
        self.frame += 1

        if self.speed > 0:
            self.image = self.rightimages[self.frame/5%2]
        if self.speed < 0:
            self.image = self.leftimages[self.frame/5%2]

        if self.speed > 0:
            if self.hp == 3:
                self.speed = 2*Locals.scale
            if self.hp == 2:
                self.speed = 3*Locals.scale
            if self.hp == 1:
                self.speed = 4*Locals.scale
        if self.speed < 0:
            if self.hp == 3:
                self.speed = -2*Locals.scale
            if self.hp == 2:
                self.speed = -3*Locals.scale
            if self.hp == 1:
                self.speed = -4*Locals.scale

        for platform in self.platforms:
            if self.rect.colliderect(platform.rect):
                if platform.check_fall:
                    self.check_fall(platform)
                if platform.check_sides:
                    self.check_rightwalk(platform)
                    self.check_leftwalk(platform)

    def check_fall(self, other):
        if pygu.sprite.Sprite.check_top(self, other, 6*Locals.scale, -3*Locals.scale):
            self.rect.bottom = other.rect.top

    def check_leftwalk(self, other):
        if pygu.sprite.Sprite.check_left(self, other, -1*Locals.scale, 6*Locals.scale):
            self.rect.left = other.rect.right + 2
            self.speed = -self.speed

    def check_rightwalk(self, other):
        if pygu.sprite.Sprite.check_right(self, other, 1*Locals.scale, 6*Locals.scale):
            self.rect.right = other.rect.left - 2
            self.speed = -self.speed
