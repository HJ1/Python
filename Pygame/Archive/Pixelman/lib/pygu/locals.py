#! /usr/bin/env python

# PyGU (Python Game Utilities) - A set of python libraries for use with pygame
# Copyright (C) 2007  Michael J. Burns
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#-------------------------------------------



import pygame, os, sys

DATA_PATH = 'data/gui/'
icon_path = DATA_PATH + 'Pygame Icon.gif'

BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)
GRAY   = (150, 150, 150)
BLUE   = (  0,   0, 255)
RED    = (255,   0,   0)
GREEN  = (  0, 255,   0)
YELLOW = (255, 255,   0)
PURPLE = (255, 0,   255)
ORANGE = (255, 200,   0)
BROWN  = (175, 100,   0)
CYAN   = (0,   255, 255)
YELLOW_GREEN  = (150, 255, 0)

innerlayer  = pygame.sprite.RenderUpdates()
middlelayer = pygame.sprite.RenderUpdates()
outerlayer  = pygame.sprite.RenderUpdates()
sprites     = pygame.sprite.Group()

def clear_sprites(sprite, sprites):
    sprite.kill()
    for s in sprites:
        pygame.sprite.Sprite.kill(s)

def save_score(file, score):
    open(file, 'w').write(str(score))
