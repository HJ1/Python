#! usr/bin/env python

import os.path

import pygame
from pygame.locals import *

import pygu
from pygu.locals import *

import Locals

def load_image(file, colorkey=False):
    file = os.path.join('data', file)
    try:
        image = pygu.image.load(file, colorkey)
    except pygame.get_error():
        print 'Unable to load: ' + file
    image = pygame.transform.scale(image, (image.get_width()*Locals.scale, image.get_height()*Locals.scale))
    return image.convert_alpha()

def load_screen(screen):
    img = load_image('Load.bmp')
    screen.blit(img, (0, 0))
    pygame.display.flip()
    pygame.time.wait(500)
