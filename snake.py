# coding: utf-8

import pygame
from colors import WHITE


segment_width = 15
segment_height = 15
segment_margin = 3


class Snake(list):

    def __init__(self, group, *args, **kwargs):
        super(Snake, self).__init__(*args, **kwargs)
        self.group = group

        self.x = segment_width + segment_margin
        self.y = 0

        self.create_segments()

    def create_segments(self):
        for i in range(15):
            x = 250 - (segment_width + segment_margin) * i
            y = 30
            snake_segment = SnakeSegment(x, y)
            self.append(snake_segment)
            self.group.add(snake_segment)

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

    def draw(self):
        # Get rid of last segment of the snake
        # .pop() command removes last item in list
        old_segment = self.pop()
        self.group.remove(old_segment)

        x = self[0].rect.x + self.x
        y = self[0].rect.y + self.y

        snake_segment = SnakeSegment(x, y)

        # Insert new segment into the list
        self.insert(0, snake_segment)
        self.group.add(snake_segment)


class SnakeSegment(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(SnakeSegment, self).__init__()

        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
