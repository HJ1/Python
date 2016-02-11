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


import pygame
from pygame.locals import *


"A sprite's rect minus the camera's rect."
def Relative_Rect(actor, camera):
    return Rect(actor.rect.x - camera.rect.x, actor.rect.y - camera.rect.y,
                actor.rect.width, actor.rect.height)



"The camera that follows a sprite on the screen."
class Camera:

    def __init__(self, screen, sprite, world_size):

        self.rect = Rect(0, 0, screen.get_width(), screen.get_height())
        self.screen = screen
        self.sprite = sprite
        self.world_size = world_size
        self.center_sprite = True


    "Moves the camera."
    def update(self):

        "Centers the camera on the sprite."
        if self.center_sprite == True:
            self.rect.center = self.sprite.rect.center


        "Don't move the camera off the screen."
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > self.world_size[1]:
            self.rect.bottom = self.world_size[1]
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.world_size[0]:
            self.rect.right = self.world_size[0]


    "Draws a sprite."
    def draw_sprite(self, sprite):
        if sprite.rect.left <= self.rect.right and sprite.rect.right >= self.rect.left:
            self.screen.blit(sprite.image, Relative_Rect(sprite, self))


    "Draws a sprite group."
    def draw_group(self, group):
        sprites = group.sprites()
        for s in sprites:
            if s.rect.left <= self.rect.right and s.rect.right >= self.rect.left:
                group.spritedict[s] = self.screen.blit(s.image, Relative_Rect(s, self))

    "Draws a sprite group."
    def draw_list(self, list):
        for s in list:
            self.screen.blit(s.image, Relative_Rect(s, self))

