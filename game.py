# coding: utf-8

import pygame
import sys
from colors import *
from snake import *

pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption('Snake Game')

group = pygame.sprite.Group()
clock = pygame.time.Clock()
snake = Snake(group)
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        # Set the speed based on the key pressed
        # We want the speed to be enough that we move a full
        # segment, plus the margin.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.left()
            if event.key == pygame.K_RIGHT:
                snake.right()
            if event.key == pygame.K_UP:
                snake.up()
            if event.key == pygame.K_DOWN:
                snake.down()
    snake.draw()
    screen.fill(BLACK)

    group.draw(screen)

    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(5)

pygame.quit()
