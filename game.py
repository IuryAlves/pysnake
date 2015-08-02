# coding: utf-8

import pygame
import sys
from colors import *
from snake import *

pygame.init()

screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Snake Game')

snake_group = pygame.sprite.Group()
block_group = pygame.sprite.Group()
clock = pygame.time.Clock()
snake = Snake(snake_group)
block = Block(screen_size, block_group)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.left()
            if event.key == pygame.K_RIGHT:
                snake.right()
            if event.key == pygame.K_UP:
                snake.up()
            if event.key == pygame.K_DOWN:
                snake.down()
    if any([snake.collidesItSelf(), snake.outOfTheScreen()]):
        break

    if snake.collidesWithBlock(block):
        block.group.remove(block)
        block = Block(screen_size, block_group)

    snake.draw()
    screen.fill(BLACK)
    snake_group.draw(screen)
    block_group.draw(screen)
    pygame.display.flip()
    clock.tick(5)

pygame.quit()
