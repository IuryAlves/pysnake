# coding: utf-8

import pygame
import sys
from pygame.font import SysFont, get_default_font
from pygame.locals import *
from colors import *
from snake import *


class Game(object):

    SCREEN_SIZE = (800, 600)
    FPS = 10
    FONT = get_default_font()

    def __init__(self):
        self._initPygame()
        self.snake_group = pygame.sprite.Group()
        self.block_group = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.snake = Snake(self.snake_group)
        self.block = Block(Game.SCREEN_SIZE, self.block_group)
        self.game_over = False
        self.score = 0

    def _initPygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode(Game.SCREEN_SIZE)
        pygame.display.set_caption('Snake Game')
        self.game_font = SysFont(Game.FONT, 72)
        self.new_game_font = SysFont(Game.FONT, 48)
        self.score_font = SysFont(Game.FONT, 32)

    def newGame(self):
        self.snake_group.empty()
        self.block_group.empty()
        self.block = Block(Game.SCREEN_SIZE, self.block_group)
        self.snake = Snake(self.snake_group)
        self.game_over = False

    def render(self):
        self.snake.draw()
        self.screen.fill(BLACK)
        self.snake_group.draw(self.screen)
        self.block_group.draw(self.screen)
        self.displayScore()

    def displayScore(self):
        score_text = self.score_font.render("Score: %d" % self.score, 1, WHITE)
        self.screen.blit(score_text, (0, 0))

    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            pressed_key = pygame.key.get_pressed()
            if pressed_key[K_LEFT]:
                self.snake.left()
            if pressed_key[K_RIGHT]:
                self.snake.right()
            if pressed_key[K_UP]:
                self.snake.up()
            if pressed_key[K_DOWN]:
                self.snake.down()

    def gameOver(self):
        self.score = 0
        game_over_text = self.game_font.render('Game Over', 1, RED)
        new_game_text = self.new_game_font.render(
            'Press Enter to new game', 1, RED)
        self.screen.blit(game_over_text, (250, 250))
        self.screen.blit(new_game_text, (200, 300))
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_RETURN]:
            self.newGame()

    def run(self):
        while True:
            self.handleInput()
            if any([self.snake.collidesItSelf(), self.snake.outOfTheScreen()]):
                self.game_over = True
            if self.game_over:
                self.gameOver()
            else:
                if self.snake.collidesWithBlock(self.block):
                    self.score += 10
                    self.block.group.remove(self.block)
                    self.block = Block(Game.SCREEN_SIZE, self.block_group)
                self.render()
            pygame.display.flip()
            self.clock.tick(Game.FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
