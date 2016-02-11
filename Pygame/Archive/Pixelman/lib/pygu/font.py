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


import os, sys

import pygame
from pygame.locals import *

from locals import *

font_path = DATA_PATH + 'Arial Rounded MT Bold (TrueType).ttf'


def Font(file, size):
    'Load\'s a font.'
    file = file
    try:
        font = pygame.font.Font(font_path, size)
    except file == None or pygame.get_error():
        file = locals.DEFAULT_FONT
        font = pygame.font.Font(file, size)
        print 'Unable to load, ', file, '. Using default font instead.'
    return font



class BitmapFont:
    def __init__(self, file, color, width, height, chars):
	self.char_w = width
	self.char_h = height
	images = load_font_image(file, width, height, color, (0, 255, 0))
	
	self.letters = {}
	count = 0
	for char in chars:
	    self.letters[char] = images[count]
	    count+=1
	del images
	del count
	
    def render(self,text,background=-1):
	textlen = len(text)
	surf = pygame.Surface((textlen*self.char_w,self.char_h))
	surf.fill((2,255,2))
	if textlen == 0:
	    return surf
		
	if background == -1:
	    colorkey = (2,255,2)
	    surf.set_colorkey(colorkey,pygame.RLEACCEL)
	else:
	    surf.fill(background)
			
	count = 0
	for c in text:
	    try:
		letter = self.letters[c]
	    except KeyError:
		letter = self.letters[' ']
	    surf.blit(letter,(count*self.char_w,0))
	    count+=1
	return surf



def load_font_image(img, w, h, color, colorkey=(0, 0, 0)):
    fullimg = pygame.image.load(img)
    color_mask = pygame.Surface((fullimg.get_width(), fullimg.get_height()))
    color_mask.fill(color)
    color_mask.set_alpha(250)
    fullimg.blit(color_mask, (0, 0))
    colorkey_topleft = fullimg.get_at((0,0))
    (t,t,fw,fh) = fullimg.get_rect()
	
    pieces = fw/w
    images = []
    i=0
    while i < pieces:
	new = pygame.Surface((w,h))
	new.blit(fullimg,(0,0),(i*w,0,w,h))
	#new.convert()
	if colorkey is not None:
	    new.set_colorkey(fullimg.get_at((0, 0)), pygame.RLEACCEL)
	images.append(new)
	i+=1
    return images
