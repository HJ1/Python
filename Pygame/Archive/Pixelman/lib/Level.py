#! usr/bin/env python

import os, sys
import random

import pygame
from pygame.locals import *

import pygu
from pygu.locals import *

from Player import *
from Game_Objects import *
import Locals

class Level:
    
    def __init__(self, level):

        file = open(level, 'r')
        section = None
        row = column = 0
        self.name = ''
        self.dialogue = []

        while 1:
            # per line
            line = file.readline()
            if line == '':
                break
            else:
                line = line.strip()
            if line == '' or line.startswith('#'):
                continue
            if line.startswith('Title: '):
                self.name = line[7:]
                print line
                continue

            if line.startswith('Layout'):
                section = 'layout'
                continue
            
            if section == 'layout':
                column = 0
                for char in line:
                    if char == "P":
                       self.player = Player((column, row-7))
                    if char == "W":
                       Platform((column, row), True, True, True)
                    if char == "w":
                       Platform((column, row), False, True, True)
                    if char == "X":
                       Platform((column, row), True, False, True)
                    if char == "x":
                       Platform((column, row), False, False, True)

                    if char == "c":
                       Coin((column, row))
                    if char == "b":
                       Bomber((column, row-8))
                    if char == "B":
                       VIRUS((column, row-(39*Locals.scale)))
                    if char == "s":
                       Spikes((column, row))

                    column += 8*Locals.scale
                row += 8*Locals.scale
                column = -8*Locals.scale

            if line.startswith('Dialogue'):
                section = 'dialogue'
                continue

            if section == 'dialogue':
                self.dialogue = self.dialogue + [str(line)]
