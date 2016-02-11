#! usr/bin/env python

import os, sys
import random

import pygame
from pygame.locals import *

import pygu
from pygu.locals import *

import Game, Menu, Locals
from Helper import *

unl_levels = os.path.expanduser('~/levels.pixelman')
if os.path.exists(unl_levels):
    unl_levels = int(open(unl_levels).read())
else:
    unl_levels = open(unl_levels, 'w').write(str(1))
UNLOCKED = unl_levels

class Level_Select:

    def __init__(self, screen, option):

        unl_levels = os.path.expanduser('~/levels.pixelman')
        if os.path.exists(unl_levels):
            unl_levels = int(open(unl_levels).read())
        else:
            unl_levels = open(unl_levels, 'w').write(str(1))
        UNLOCKED = unl_levels
        s = Locals.scale

        self.option = option
        cursor_poses = [41, 41+11,41+(11*2), 41+(11*3), 41+(11*4), 41+(11*5),
                        41+(11*6), 41+(11*7), 41+(11*8), 41+(11*9)]
        self.image = load_image('Level Select.bmp', False)
        self.cursor = load_image('Cursor.bmp', True)

        pygame.mixer.stop()
        pygu.sound.play_sound('data/Level Select.ogg', 1.0, True)
        self.font = pygu.font.BitmapFont('data/Font%d.bmp' % (1*Locals.scale), WHITE, 6*Locals.scale, 9*Locals.scale,
                                 '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,!?:;/[]()+-*=\'" ')
        global UNLOCKED

        while 1:
            
            event = pygame.event.poll()
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    Menu.Menu(screen)

                if event.key == K_DOWN:
                    if self.option < UNLOCKED and self.option < 10:
                        self.option += 1
                if event.key == K_UP:
                    if self.option > 1:
                        self.option -= 1

                if event.key == K_RETURN:
                    Game.Game(screen, self.option)

                if event.key == K_DELETE:
                    UNLOCKED = 1
                    open(os.path.expanduser('~/levels.pixelman'), 'w').write(str(1))
                    self.option = UNLOCKED
                if event.key == K_1:
                    UNLOCKED = 1
                    open(os.path.expanduser('~/levels.pixelman'), 'w').write(str(UNLOCKED))
                    self.option = UNLOCKED
                if event.key == K_2:
                    UNLOCKED = 2
                    open(os.path.expanduser('~/levels.pixelman'), 'w').write(str(UNLOCKED))
                    self.option = UNLOCKED
                if event.key == K_3:
                    UNLOCKED = 3
                    open(os.path.expanduser('~/levels.pixelman'), 'w').write(str(UNLOCKED))
                    self.option = UNLOCKED
                if event.key == K_4:
                    UNLOCKED = 4
                    open(os.path.expanduser('~/levels.pixelman'), 'w').write(str(UNLOCKED))
                    self.option = UNLOCKED
                if event.key == K_5:
                    UNLOCKED = 5
                    open(os.path.expanduser('~/levels.pixelman'), 'w').write(str(UNLOCKED))
                    self.option = UNLOCKED
                if event.key == K_6:
                    UNLOCKED = 6
                    open(os.path.expanduser('~/levels.pixelman'), 'w').write(str(UNLOCKED))
                    self.option = UNLOCKED
                if event.key == K_7:
                    UNLOCKED = 7
                    open(os.path.expanduser('~/levels.pixelman'), 'w').write(str(UNLOCKED))
                    self.option = UNLOCKED
                if event.key == K_8:
                    UNLOCKED = 8
                    open(os.path.expanduser('~/levels.pixelman'), 'w').write(str(UNLOCKED))
                    self.option = UNLOCKED
                if event.key == K_9:
                    UNLOCKED = 9
                    open(os.path.expanduser('~/levels.pixelman'), 'w').write(str(UNLOCKED))
                    self.option = UNLOCKED
                if event.key == K_0:
                    UNLOCKED = 10
                    open(os.path.expanduser('~/levels.pixelman'), 'w').write(str(UNLOCKED))
                    self.option = UNLOCKED
                     
            screen.blit(self.image, (0, 0))
            screen.blit(self.cursor, (62*s, cursor_poses[self.option-1]*s))

            for i in range(10):
                if i < 9:
                    ren = self.font.render('Level %d' % int(i + 1))
                else:
                    ren = self.font.render('Boss')
                rect = pygame.Rect(75*s, i * (9*s + 2*s) + 40*s, 13*s, 8*s)
                if i < UNLOCKED:
                    screen.blit(ren, rect)
                else:
                    screen.blit(self.font.render('???'), rect)

            pygame.display.flip()
