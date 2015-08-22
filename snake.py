# coding: utf-8

import random
import pygame
from colors import *


segment_width = 15
segment_height = 15
segment_margin = 0


class Snake(list):

    def __init__(self, group, *args, **kwargs):
        super(Snake, self).__init__(*args, **kwargs)
        self.group = group

        self.x = segment_width + segment_margin
        self.y = 0

        self.createSegments()

    def createSegments(self):
        for i in range(15):
            x = 250 - (segment_width + segment_margin) * i
            y = 30
            self.add_segment(x, y, len(self) -1)

    def collidesWithBlock(self, block):
        if self[0].rect.collidelist([block.rect]) != -1:
            self.add_segment(block.rect.x, block.rect.y)
            return True
        return False

    def outOfTheScreen(self):
        return self[0].rect.x > 790 or self[0].rect.x < 16 or \
            self[0].rect.y < 12 or self[0].rect.y > 570

    def collidesItSelf(self):
        return self[0].rect.collidelist([segment.rect for segment in self[1:]]) != -1

    def left(self):
        self.x = (segment_width + segment_margin) * -1
        self.y = 0

    def right(self):
        self.x = (segment_width + segment_margin)
        self.y = 0

    def down(self):
        self.x = 0
        self.y = (segment_height + segment_margin)

    def up(self):
        self.x = 0
        self.y = (segment_height + segment_margin) * -1

    def add_segment(self, x, y, list_position=0):
        snake_segment = Segment(x, y)
        self.insert(list_position, snake_segment)
        self.group.add(snake_segment)

    def draw(self):
        # Get rid of last segment of the snake
        # .pop() command removes last item in list
        old_segment = self.pop()
        self.group.remove(old_segment)

        x = self[0].rect.x + self.x
        y = self[0].rect.y + self.y
        self.add_segment(x, y)

class Segment(pygame.sprite.Sprite):

    def __init__(self, x, y, color=WHITE):
        super(Segment, self).__init__()

        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Block(Segment):

    colors = [RED, GREEN, BLUE]

    def __init__(self, screen_size, group):
        self.group = group
        x = random.randrange(screen_size[0])
        y = random.randrange(screen_size[1])
        color = random.choice(Block.colors)
        super(Block, self).__init__(x, y, color=color)
        self.group.add(self)
