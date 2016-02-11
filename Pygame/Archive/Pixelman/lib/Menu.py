#! usr/bin/env python

import os, sys
import random

import pygame
from pygame.locals import *

import pygu
from pygu.locals import *

import Game, Level_Select, Locals
from Helper import *


class Menu:

    def __init__(self, screen):

        s = Locals.scale
        self.option = 2
        self.cursor_pos = (62*s, 91*s)
        self.image = load_image('Menu.bmp', False)
        self.cursor = load_image('Cursor.bmp', True)

        pygame.mixer.stop()
        pygu.sound.play_sound('data/Menu.ogg', 1.0, True)


        while 1:
            
            event = pygame.event.poll()
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()

                if event.key == K_DOWN:
                    if self.option > 1:
                        self.option -= 1
                        self.cursor_pos = (62*s, 102*s)
                if event.key == K_UP:
                    if self.option < 2:
                        self.option += 1
                        self.cursor_pos = (62*s, 91*s)

                if event.key == K_RETURN:
                    if self.option == 2:
                        Level_Select.Level_Select(screen, 1)
                    if self.option == 1:
                         sys.exit()
                     
            screen.blit(self.image, (0, 0))
            screen.blit(self.cursor, self.cursor_pos)
            pygame.display.flip()
