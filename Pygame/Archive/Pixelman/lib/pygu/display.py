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
from font import *



"A quick screen that has about all the features you'll want to use."
def screen(size, caption=None, icon_file=None, fullscreen=False):

    if caption is not None:
        pygame.display.set_caption(caption)
    else:
        pass

    if icon_file is not None:
        pygame.display.set_icon(pygame.image.load(icon_file))
    else:
        pygame.display.set_icon(pygame.image.load(icon_path))

    if fullscreen:
        screen = pygame.display.set_mode(size, pygame.FULLSCREEN|SWSURFACE)
    else:
        screen = pygame.display.set_mode(size, HWSURFACE)

    return screen


"Easy toggle fullscreen."
def toggle_fullscreen():
    screen = pygame.display.get_surface()
    tmp = screen.convert()
    caption = pygame.display.get_caption()
    
    w,h = screen.get_width(),screen.get_height()
    flags = screen.get_flags()
    bits = screen.get_bitsize()
    
    pygame.display.init()
    
    screen = pygame.display.set_mode((w,h),flags^FULLSCREEN,bits)
    screen.blit(tmp,(0,0))
    pygame.display.set_caption(*caption)
    
    return screen


"Center's the window to the center of the computer screen."
def center_window():
    os.environ['SDL_VIDEO_CENTERED'] = '1'


"Draws pygame.sprite.RenderUpdates."
def draw_sprites(surface):
    innerlayer.draw(surface)
    middlelayer.draw(surface)
    outerlayer.draw(surface)


"Updates sprites."
def update_sprites(surface):
    innerlayer.update(surface)
    middlelayer.update(surface)
    outerlayer.update(surface)


"A simple load screen to use when a game is loading."
def load(screen):

    font = Font(None, 17)
    screen.fill(BLACK)

    ren = font.render('Now Loading...', 1, WHITE)
    screen.blit(ren, (screen.get_width() - ren.get_width() - 10,
                      screen.get_height() - ren.get_height() - 5))

    pygame.display.flip()

    
