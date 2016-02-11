#! usr/bin/env python

import os, sys
import random

import pygame
from pygame.locals import *

import pygu
from pygu.locals import *

import Locals
from Helper import *


def Logo(screen):
    s = Locals.scale

    intro = pygame.image.load('data/logo 1.bmp')
    intro2 = pygame.image.load('data/logo 2.bmp')
    intro = pygame.transform.scale(intro, (intro.get_width()*s, intro.get_height()*s))
    intro2 = pygame.transform.scale(intro2, (intro2.get_width()*s, intro2.get_height()*s))
    fadeCount = 0
    introCount = 0
    clock = pygame.time.Clock()
    pygame.mixer.music.load('data/Logo.ogg')
    pygame.mixer.music.play()

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                elif event.key == K_RETURN:
                    return
        while 1:
            clock.tick(60)
            background = pygame.Surface(screen.get_size())
            background.fill((0, 0, 0))
            background.set_alpha(255)
               
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()
                    elif event.key == K_RETURN:
                        return

            if fadeCount < 100:
                background.set_alpha(255-fadeCount*3)
                screen.blit(intro, (0, 0))
                screen.blit(background, (0, 0))
                pygame.display.flip()
                fadeCount = fadeCount + 1
                continue
                        
            if introCount < 0:
                introCount = introCount + 1
            else:
                break

        fadeCount = 0
        introCount = 0
        intro = pygame.image.load('data/logo 1.bmp')
        intro2 = pygame.image.load('data/logo 2.bmp')
        intro = pygame.transform.scale(intro, (intro.get_width()*s, intro.get_height()*s))
        intro2 = pygame.transform.scale(intro2, (intro2.get_width()*s, intro2.get_height()*s))

        while 1:
            clock.tick(60)
            background = pygame.Surface(screen.get_size())
            background.fill((0, 0, 0))
            background.set_alpha(255)
               
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()
                    elif event.key == K_RETURN:
                        return
   
            if fadeCount < 90:
                intro.set_alpha(255-fadeCount*4)
                screen.blit(intro2, (0, 0))
                screen.blit(intro, (0, 0))
                pygame.display.flip()
                fadeCount = fadeCount + 1
                continue
                        
            if introCount < 5:
                introCount = introCount + 1
            else:
                break

        fadeCount = 0
        introCount = 0
        intro = pygame.image.load('data/logo 1.bmp')
        intro2 = pygame.image.load('data/logo 2.bmp')
        intro = pygame.transform.scale(intro, (intro.get_width()*s, intro.get_height()*s))
        intro2 = pygame.transform.scale(intro2, (intro2.get_width()*s, intro2.get_height()*s))

        while 1:
            clock.tick(60)
            background = pygame.Surface(screen.get_size())
            background.fill((0, 0, 0))
            background.set_alpha(255)
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()
                    elif event.key == K_RETURN:
                        return

            if fadeCount < 130:
                intro2.set_alpha(255-fadeCount*2)
                screen.blit(background, (0, 0))
                screen.blit(intro2, (0, 0))
                pygame.display.flip()
                fadeCount = fadeCount + 1
                continue
            elif fadeCount == 130:
                fadeCount = fadeCount + 1
                screen.blit(background, (0, 0))
                pygame.display.flip()
                        
            if introCount < 60:
                introCount = introCount + 1
            else:
                return

class Intro:

    def __init__(self, screen):

        self.pos = 160*Locals.scale
        self.image = load_image('Story.bmp', False)

        pygame.mixer.stop()
        pygame.mixer.music.stop()
        pygu.sound.play_sound('data/Intro.ogg', 1.0, True)

        clock = pygame.time.Clock()

        
        while 1:

            clock.tick(50)
            
            event = pygame.event.poll()
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()

                if event.key == K_RETURN:
                    break

            self.pos -= 0.2*Locals.scale
            if self.pos <= -230*Locals.scale:
                break

            screen.fill((0, 0, 0))
            screen.blit(self.image, (0, self.pos))
            pygame.display.flip()
