#! usr/bin/env python

import os, sys
import random

import pygame
from pygame.locals import *

import pygu
from pygu.locals import *


from Helper import *
import Locals

class Credits:

    def __init__(self, screen):

        self.pos = 160*Locals.scale
        self.image = load_image('Credits.bmp', False)

        pygame.mixer.stop()
        pygu.sound.play_sound('data/Credits.ogg', 1.0, True)

        clock = pygame.time.Clock()

        
        while 1:

            clock.tick(50)
            
            event = pygame.event.poll()
            if event.type == QUIT:
                sys.exit()

            self.pos -= 0.2*Locals.scale
            if self.pos <= -730*Locals.scale:
                break

            screen.fill((0, 0, 0))
            screen.blit(self.image, (0, self.pos))
            pygame.display.flip()
