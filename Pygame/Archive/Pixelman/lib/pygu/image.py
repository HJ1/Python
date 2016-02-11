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



import os

import pygame
from pygame.locals import *


"Quickly loads an image, and converts an transparency in it."
def load(file, colorkey=False):
    "Loads an image."
    file = file
    try:
        image = pygame.image.load(file)
    except pygame.error:
        raise SystemExit, 'Unable to load: "%s"'%file
    if colorkey:
        colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image.convert_alpha()



"Loads multiple images and sets a colorkey at (0, 0) in the image."
def load_transparent_images(*files):
    "Loads multiple transparent images."
    imgs = []
    for file in files:
        imgs.append(load(file, colorkey=True))
    return imgs



"Loads multiple images."
def load_regular_images(*files):
    "Loads multiple images."
    imgs = []
    for file in files:
        imgs.append(load(file, colorkey=False))
    return imgs


"Loads a shapstrip."
def load_shapestrip(name, width):
    "Loads a shapestrip."
    img = load(name)
    fw = img.get_width()
    num=fw/width
    imgs=[]
    for x in xrange(int(num)):
	surf = pygame.Surface((width,img.get_height()))
	surf = surf.convert_alpha()
	surf.fill((255,255,255,0))
	surf.blit(img,(0,0),(x*width,0,width,img.get_height()))
	imgs.append(surf)
    return imgs
