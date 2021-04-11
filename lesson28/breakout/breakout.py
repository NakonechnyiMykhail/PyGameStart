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

special_effects = dict(
    long_paddle = (
        colors.ORANGE,
        lambda g: g.paddle.bounds.inflate_ip(c.paddle_width // 2, 0),
        lambda g: g.paddle.bounds.inflate_ip(-c.paddle_width // 2, 0)
    ),
    slow_ball = (
        colors.AQUAMARINE2,
        lambda g: g.change_ball_speed(-1),
        lambda g: g.change_ball_speed(1)
    ),
    tripple_points = (
        colors.DARKSEAGREEN4,
        lambda g: g.set_points_per_brick(3),
        lambda g: g.set_points_per_brick(1)
    ),
    extra_life = (
        colors.GOLD1,
        lambda g: g.add_life(),
        lambda g: None
    )
)

assert os.path.isfile('sound_effects/brick_hit.wav')

class Breakout(Game):
    def __init__(self):
        
        
        self.bricks = None
        self.paddle = None
        self.ball = None

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
        w = c.brick_width
        h = c.brick_height
        brick_count = c.screen_width // (w + 1)
        offset_x = (c.screen_width - brick_count * (w + 1) ) // 2

        bricks = []
        for row in range(c.row_count):
            for col in range(brick_count):
                effect = None
                brick_color = c.brick_color
                index = random.randint(0, 10)
                if index < len(special_effects):
                    brick_color, start_effect_func, reset_effect_func = list(special_effects.values())[index]
                    effect = start_effect_func, reset_effect_func
                
                brick = Brick(  offset_x + col * (w + 1),   # pos -> x
                                c.offset_y + row * (h + 1), # pos -> y
                                w,
                                h,
                                brick_color,
                                effect
                                )
                bricks.append(brick)
                self.objects.append(brick)
        self.bricks = bricks

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


    
