# coding: utf-8

import pygame
import os
from pygame import sprite
from pygame.locals import *
from snake import Snake, Item


class Game(object):

    FPS = 16
    SCREEN_SIZE = (640, 460)
    NAME = "PySnake"

    keys = {
        K_LEFT: False,
        K_RIGHT: False,
        K_UP: False,
        K_DOWN: False,
        K_RETURN: False,
        27: False
    }

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(Game.NAME)
        self.screen = pygame.display.set_mode(Game.SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.group = sprite.RenderUpdates()
        self.background = pygame.image.load(os.path.sep.join(["sprites", "background.jpg"])).convert()
        self.screen.blit(self.background, (0, 0))
        self.snake = Snake((0, 10), self.group)
        self.items = [Item((50, 50), self.group)]

    def run(self):
        pygame.display.flip()
        while True:
            self.clock.tick(Game.FPS)

            for e in pygame.event.get([KEYUP, KEYDOWN]):
                valor = (e.type == KEYDOWN)
                if e.key in Game.keys:
                    Game.keys[e.key] = valor

            if Game.keys[K_LEFT]:
                self.snake.move("LEFT")
            elif Game.keys[K_RIGHT]:
                self.snake.move("RIGHT")
            elif Game.keys[K_DOWN]:
                self.snake.move("DOWN")
            elif Game.keys[K_UP]:
                self.snake.move("UP")

            if self.snake.rect.collidelistall(self.items):
                print "collidiu"

            self.group.clear(self.screen, self.background)
            pygame.display.update(self.group.draw(self.screen))

if __name__ == '__main__':
    game = Game()
    game.run()
