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


import sys, os

import pygame
from pygame.locals import *

from image import *
from locals import *
import font


"Just used for the buttons, sliders, and textbars."
class Cursor:

    def __init__(self, use_image):

        self.image = pygame.Surface((1, 1))
        self.rect = pygame.Rect(0, 0, 1, 1)

    def update(self):
        self.rect.topleft = pygame.mouse.get_pos()





"Uses only pygame.draw."
class BasicButton:

    def __init__(self, text, font, command, pos, text_color, fill_color=BLACK, line_color=WHITE, fill_select=BLACK, line_select=GRAY):

        self.font = font
        try:
            self.text = self.font.render(text, 1, text_color)
            self.shadow = self.font.render(text, 1, BLACK)
        except:
            try:
                self.text = self.font.render(text)
                self.shadow = self.font.render(text)
            except:
                raise SystemExit, "Unknown problem with the button module."

        if self.text.get_width() >= 1:
            self.image = pygame.Surface((100, 27))
        if self.text.get_width() >= 90:
            self.image = pygame.Surface((160, 27))
        if self.text.get_width() >= 145:
            self.image = pygame.Surface((230, 27))
        self.image.fill(fill_color)

        self.pos = pos
        self.rect = self.image.get_rect(topleft = self.pos)

        self.cur_fill_color = fill_color
        self.cur_line_color = line_color

        self.fill_select = fill_select
        self.line_select   = line_select
        
        self.line_color = line_color
        self.fill_color = fill_color

        self.cursor = Cursor(False)
        self.command = command

        self.normpos = self.rect
        self.selectpos = self.image.get_rect(topleft = self.pos).move(3, 3)


    def render(self, screen):

        self.cursor.update()
        mousebutton = pygame.mouse.get_pressed()

        self.image.fill(self.cur_fill_color)
        pygame.draw.rect(self.image, self.cur_line_color,
                         [0, 0, self.image.get_width(), self.image.get_height()], 1)

        screen.blit(self.image, self.rect)
        screen.blit(self.text, (self.rect.center[0] - self.text.get_width()/2, self.rect.center[1] - self.text.get_height()/2))

        if self.cursor.rect.colliderect(self.rect):
            if mousebutton[0]:
                self.rect = self.selectpos
                if self.command is not None:
                    self.command()
            else:
                self.rect = self.normpos
            self.cur_fill_color = self.fill_select
            self.cur_line_color = self.line_select
        else:
            self.rect = self.normpos
            self.cur_fill_color = self.fill_color
            self.cur_line_color = self.line_color





"Uses the button images I've created."
class Button:

    def __init__(self, text, font, command, pos, button_color, text_color, sound=None):

        self.font = font
        self.text_ren = text
        try:
            self.text = self.font.render(text, 1, text_color)
            self.shadow = self.font.render(text, 1, BLACK)
        except:
            try:
                self.text = self.font.render(text)
                self.shadow = self.font.render(text)
            except:
                raise SystemExit, "Unknown problem with the button module."

        if self.text.get_width() >= 1:
            self.size = 1
        if self.text.get_width() >= 1:
            self.size = 1
        if self.text.get_width() >= 90:
            self.size = 2
        if self.text.get_width() >= 90:
            self.size = 2
        if self.text.get_width() >= 145:
            self.size = 3
        if self.text.get_width() >= 145:
            self.size = 3

        self.sound = sound

        self.non_selected_image = load(DATA_PATH + '%s_button%s_nonselected.png' % (button_color, self.size))
        self.selected_image = load(DATA_PATH + '%s_button%s_selected.png' % (button_color, self.size))
        self.pressed_image = load(DATA_PATH + '%s_button%s_pressed.png' % (button_color, self.size))
        self.image = self.non_selected_image

        self.pos = pos
        self.rect = self.image.get_rect(topleft = self.pos)

        self.cursor = Cursor(False)
        self.command = command

        self.text_color = text_color

        self.normpos = self.rect
        self.selectpos = self.image.get_rect(topleft = self.pos).move(3, 3)
        self.text_indent = 0

        self.selected = False
        self.commanding = False


    def render(self, screen):

        try:
            self.text = self.font.render(str(self.text_ren), 1, self.text_color)
        except:
            try:
                self.text = self.font.render(str(self.text_ren))
            except pygame.get_error():
                raise SystemExit, pygame.get_error()
                

        self.cursor.update()
        mousebutton = pygame.mouse.get_pressed()

        screen.blit(self.image, self.rect)
        screen.blit(self.shadow, (self.rect.center[0] + self.text_indent + 1 - self.text.get_width()/2, self.rect.center[1] + self.text_indent + 1 - self.text.get_height()/2))
        screen.blit(self.text, (self.rect.center[0] + self.text_indent - self.text.get_width()/2, self.rect.center[1] + self.text_indent - self.text.get_height()/2))

        if self.cursor.rect.colliderect(self.rect):
            self.image = self.selected_image
            if mousebutton[0]:
                if not self.selected and self.sound is not None:
                    self.sound.play()
                self.selected = True
                self.image = self.pressed_image
                self.text_indent = 2
            else:
                if self.command is not None and self.selected and not self.commanding:
                    self.command()
                    self.commanding = True
                self.selected = False         
                self.text_indent = 0
        else:
            self.commanding = False
            self.text_indent = 0
            self.selected = False
            self.rect = self.normpos
            self.image = self.non_selected_image



    def change_text(self, text):
        self.text = self.font.render(text, 1, self.text_color)





"A slider. Maximum value is 100."
class Slider:

    def __init__(self, pos, value, button_color):

        self.non_selected_image = load(DATA_PATH + '%s_slider_button.png' % button_color)
        self.selected_image = load(DATA_PATH + '%s_slider_button_active.png' % button_color)
        self.slider_image = load(DATA_PATH + 'slider.png')
        self.image = self.slider_image
        self.buttonimage = self.non_selected_image

        self.pos = pos
        self.rect = self.image.get_rect(topleft = self.pos)
        self.buttonrect = self.selected_image.get_rect(topleft = (pos[0] + value, pos[1]))

        self.cursor = Cursor(False)
        self.value = value

        self.normpos = self.rect

        self.selected = False
        self.commanding = False


    def render(self, screen):

        self.value = self.buttonrect.left - self.rect.left
                

        self.cursor.update()
        mousebutton = pygame.mouse.get_pressed()

        screen.blit(self.image, self.rect)
        screen.blit(self.buttonimage, self.buttonrect)

        if self.cursor.rect.colliderect(self.buttonrect):
            self.buttonimage = self.selected_image
            if mousebutton[0]:
                self.selected = True

        if self.cursor.rect.colliderect(self.rect):
            if mousebutton[0]:
                self.selected = True

        if not mousebutton[0]:
            self.selected = False
            self.buttonimage = self.non_selected_image

        if self.selected:
            self.buttonrect.centerx = self.cursor.rect.centerx


        self.buttonrect = self.buttonrect.clamp(self.rect)




"This works like a button but uses only text instead."
class Link:

    def __init__(self, text, font, command, pos, text_color, fill_color=BLACK):

        self.font = font
        try:
            self.text = self.font.render(text, 1, text_color)
            self.select = self.font.render(text, 1, fill_color)
        except:
            try:
                self.text = self.font.render(text)
                self.select = self.font.render(text)
            except:
                raise SystemExit, "Unknown problem with the button module."

        self.image = self.text

        self.selected_image = self.select
        self.normal_image = self.text

        self.pos = pos
        self.rect = self.image.get_rect(topleft = self.pos)

        self.text_color = text_color
        self.fill_color = fill_color

        self.cursor = Cursor(False)
        self.command = command


    def render(self, screen):

        self.cursor.update()
        mousebutton = pygame.mouse.get_pressed()

        screen.blit(self.image, self.rect)

        if self.cursor.rect.colliderect(self.rect):
            self.image = self.selected_image
            if mousebutton[0]:
                if self.command is not None:
                    self.command()
        else:
            self.image = self.normal_image



"A simple input box."
class Textbox:

    def __init__(self, text, font, size, pos, text_color=BLACK, fill_color=WHITE, line_color=BLACK):

        self.font = font
        self.key_pressed = False
        self.size = size
        self.pos = pos
        self.text = text
        self.ren = self.font.render(self.text + '|', 1, (0, 0, 0))
        self.rect = Rect(pos[0], pos[1], size[0], size[1])
        self.cursor = Cursor(False)
        self.selected = False
        self.highlight = ''
        self.frame = 0
        self.clock = pygame.time.Clock()
        self.fill_color = fill_color
        self.line_color = line_color
        self.text_color = text_color


    def render(self, screen):
        self.frame += 1
        self.cursor.update()
        mousebutton = pygame.mouse.get_pressed()

        if self.cursor.rect.colliderect(self.rect):
            if mousebutton[0]:
                self.selected = True
        if not self.cursor.rect.colliderect(self.rect):
            if mousebutton[0]:
                self.selected = False

        if self.selected:
            self.highlight = '|'
        else:
            self.highlight = ''

        if self.frame >= 100:
            self.frame = 0

        pygame.draw.rect(screen, self.fill_color, [self.pos[0], self.pos[1],
                                                   self.size[0], self.size[1]])
        pygame.draw.rect(screen, self.line_color, [self.pos[0], self.pos[1],
                                                   self.size[0], self.size[1]], 1)
        self.ren = self.font.render(self.text + self.highlight, 1, self.text_color)
        screen.blit(self.ren, (self.pos[0] + 2, self.pos[1]))


    def update(self, event):

        if self.selected:
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    self.text = self.text[:-1]
                if event.key is not K_BACKSPACE:
                    if self.ren.get_width() < self.size[0] - 5:
                        self.text = self.text + event.unicode
            


"A quick easy way to put text up on the screen."
def RenderText(surface, text, position, color, font=None, style=None,
               blend=True, shadow_color=(0,0,0)):

    if font is None:
        font = font.Font(None, size)

    ren = font.render(text, blend, color)
    xpos = position[0]
    ypos = position[1]

    if position[0] == 'centered':
        xpos = surface.get_width()/2 - ren.get_width()/2
    if position[1] == 'centered':
        ypos = surface.get_height()/2 - ren.get_height()/2

    if style == None or style == 'regular':

        ren = font.render(text, blend, color)
        surface.blit(ren, (xpos, ypos))

    if style == 'shadow':

        ren = font.render(text, blend, shadow_color)
        surface.blit(ren, (xpos + 1, ypos + 1))
        
        ren = font.render(text, blend, color)
        surface.blit(ren, (xpos, ypos))


