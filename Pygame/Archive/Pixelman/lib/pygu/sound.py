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


def load_sound(file, volume = 1.0):
    'Loads a sound file.'
    file = file
    try:
        sound = pygame.mixer.Sound(file)
        sound.set_volume(volume)
        return sound
    except pygame.error:
        print 'Warning, unable to load, ', file

        
def play_sound(file, volume = 1.0, loop=False):
    'Plays a sound file.'
    file = file
    try:
        sound = pygame.mixer.Sound(file)
        sound.set_volume(volume)
        if loop is True:
            return sound.play(-1)
        else:
            return sound.play()
    except pygame.error:
        print 'Warning, unable to load, ', file



def load_music(file, volume = 1.0):
    'Loads a music file.'
    file = file
    try:
        pygame.mixer.music.load(file)
        pygame.mixer.music.set_volume(volume)
    except pygame.error:
        print 'Warning, unable to load, ', file


def play_music(loop = False, volume = 1.0):
    try:
        if loop == True:
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.play()
        pygame.mixer.music.set_volume(volume)
    except:
        print 'No music could be found.'
