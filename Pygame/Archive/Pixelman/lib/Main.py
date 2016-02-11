#! usr/bin/env python

import sys, os

import pygame
from pygame.locals import *

import Game
import Menu
import Intro

import pygu
from Helper import *
import Locals

unl_levels = os.path.expanduser('~/levels.pixelman')
if os.path.exists(unl_levels):
    unl_levels = int(open(unl_levels).read())
else:
    unl_levels = open(unl_levels, 'w').write(str(1))

def run():

    pygame.init()

    pygu.display.center_window()

    pygame.mouse.set_visible(0)
    screen = pygu.display.screen((192*Locals.scale, 160*Locals.scale), 'Pixelman', None, False)

    img = load_image('Load.bmp')
    screen.blit(img, (0, 0))
    pygame.display.flip()
    pygame.time.wait(500)

    Intro.Logo(screen)
    Intro.Intro(screen)
    Menu.Menu(screen)
    
