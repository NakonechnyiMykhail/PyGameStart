import pygame
import sys
import random
import time

from pygame.locals import *

FPS = 5
pygame.init()
fpsClock = pygame.time.Clock()

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480


class Snake(object):
    def __init__(self):
        pass

class Apple(object):
    def __init__(self):
        pass

if __name__ == '__main__':
    snake = Snake()
    apple = Apple()

    while True:
        #...
        pygame.display.flip()
        pygame.display.update()
        fpsClock.tick(FPS + snake.length/3)
