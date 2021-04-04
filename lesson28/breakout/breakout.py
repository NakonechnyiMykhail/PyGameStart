import random
from datetime import datetime, timedelta

import os
import time
import pygame
from pygame.rect import Rect

import config as c
from ball import Ball
from brick import Brick
from button import Button
from game import Game
from paddle import Paddle
from text_object import TextObject
import colors


class Breakout(Game):
    def __init__(self):
        pass

    def add_life(self):
        pass

    def set_points_per_brick(self, points):
        """ setter """
        self.points_per_brick = points

    # def get_points(self):
    #     """ getter """
    #     return self.points_per_brick

    def change_ball_speed(self):
        pass

    def create_menu(self):
        def on_play(button):
            pass

        def on_quit(button):
            pass


    def create_objects(self):
        self.create_bricks()
        self.create_paddle()
        self.create_ball()
        self.create_labels()
        self.create_menu()

    def create_labels(self):
        pass

    def create_bricks(self):
        pass

    def create_paddle(self):
        pass

    def create_ball(self):
        pass

    def handle_ball_collisions(self):
        def intersect(obj, ball):
            pass

    def update(self):
        pass

    def show_message(self):
        pass

def main():
    Breakout.run()

if __name__ == '__main__':
    main()


    
