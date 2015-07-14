# coding: utf-8

import os
import pygame
from pygame.locals import RLEACCEL
from pygame import sprite

class Item(sprite.Sprite):

    _base_image_path = 'sprites'

    def __init__(self, position_tuple, *groups):
        sprite.Sprite.__init__(self, *groups)
        self.position_x, self.position_y = position_tuple
        self.image = pygame.image.load(os.path.sep.join([Snake._base_image_path, 'item.png']))
        self.rect = self.image.get_rect()
        self.rect.move_ip(self.position_x, self.position_y)
        self.convert_image()

    def convert_image(self):
        self.image.set_alpha(None, RLEACCEL)
        self.image.convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)


class Snake(sprite.Sprite):

    _base_image_path = 'sprites'

    def __init__(self, position_tuple, *groups):
        sprite.Sprite.__init__(self, *groups)
        self.position_x, self.position_y = position_tuple
        self.image = pygame.image.load(os.path.sep.join([Snake._base_image_path, 'snake.png']))
        self.rect = self.image.get_rect()
        self.rect.move_ip(self.position_x, self.position_y)
        self.convert_image()

    def move(self, side):
        self.convert_image()
        sides = {
            "LEFT": (-10, 0),
            "RIGHT": (10, 0),
            "UP": (0, -10),
            "DOWN": (0, 10)
        }
        self.rect.move_ip(sides[side])

    def convert_image(self):
        self.image.set_alpha(None, RLEACCEL)
        self.image.convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
