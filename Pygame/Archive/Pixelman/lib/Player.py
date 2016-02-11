#! usr/bin/env python

import pygame
from pygame.locals import *

import pygu
from pygu.locals import *

import Game, Locals
from Helper import *

class Player(pygu.sprite.Sprite):

    def __init__(self, pos):

        pygu.sprite.Sprite.__init__(self)

        self.rightimages = [load_image('Pixelman 1.bmp', True),
                            load_image('Pixelman 2.bmp', True),
                            load_image('Pixelman 3.bmp', True)]
        self.leftimages = [pygame.transform.flip(load_image('Pixelman 1.bmp', True), 1, 0),
                           pygame.transform.flip(load_image('Pixelman 2.bmp', True), 1, 0),
                           pygame.transform.flip(load_image('Pixelman 3.bmp', True), 1, 0)]
        self.image = self.rightimages[0]
        self.rect = self.image.get_rect(topleft = pos)

        self.jump_sound = pygu.sound.load_sound('data/Jump.wav', 0.7)
        self.land_sound = pygu.sound.load_sound('data/Land.wav', 0.7)
        self.coin_sound = pygu.sound.load_sound('data/Coin.wav', 0.7)

        self.jump_speed = 0
        self.jumping = False
        self.kup_fall_speed = 0.35*Locals.scale
        self.kdown_fall_speed = 0.18*Locals.scale
        self.max_fallspeed = -4*Locals.scale

        self.walk_speed = 1*Locals.scale
        self.facing = 1
        
        self.anim_delay = 5
        self.frame = 0


    def step(self, moving):
        self.frame += 1
        if moving: self.facing = moving

        self.move(moving*self.walk_speed, -self.jump_speed)

        if self.jump_speed < -1.5:
            self.jumping = True

        "Stand."
        if self.facing > 0:
            self.image = self.rightimages[0]
            if self.jumping:
                self.image = self.rightimages[2]
        if self.facing < 0:
            self.image = self.leftimages[0]
            if self.jumping:
                self.image = self.leftimages[2]

        "Walk."
        if moving > 0:
            self.image = self.rightimages[self.frame/self.anim_delay%2]
        if moving < 0:
            self.image = self.leftimages[self.frame/self.anim_delay%2]

        "Jump."
        if self.facing > 0:
            if self.jumping:
                self.image = self.rightimages[2]
        if self.facing < 0:
            if self.jumping:
                self.image = self.leftimages[2]

        if self.rect.left <= 0:
            self.rect.left = 0
                

    def jump(self):
        if not self.jumping:
            self.jump_speed = 4*Locals.scale
            self.jumping = True
            self.jump_sound.play()


    def check_fall(self, other):
        if pygu.sprite.Sprite.check_top(self, other, 6*Locals.scale, self.jump_speed):
            if self.jumping: self.land_sound.play()
            self.rect.bottom = other.rect.top
            self.jumping = False
            self.jump_speed = 0

    def check_fall_on_spikes(self, other):
        if pygu.sprite.Sprite.check_top(self, other, 6*Locals.scale, self.jump_speed):
            self.image = load_image('Pixelman 4.bmp', True)
            Game.DEAD = True

    def check_jump(self, other):
        if pygu.sprite.Sprite.check_bottom(self, other, 6*Locals.scale, self.jump_speed):
            self.rect.top = other.rect.bottom

    def check_leftwalk(self, other, moving):
        if pygu.sprite.Sprite.check_left(self, other, moving, 6*Locals.scale):
            self.rect.left = other.rect.right

    def check_rightwalk(self, other, moving):
        if pygu.sprite.Sprite.check_right(self, other, moving, 6*Locals.scale):
            self.rect.right = other.rect.left
