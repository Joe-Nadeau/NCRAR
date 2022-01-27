# Code author: Joseph K. Nadeau

import pygame as pg
import sys, time
import pandas as pd
import numpy as np
from pygame.constants import MOUSEBUTTONDOWN, USEREVENT


WHITE = pg.Color(255, 255, 255)
BLACK = pg.Color(0, 0, 0)

# create a sprite object
class Subject(pg.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y):
        super().__init__()
        self.image = pg.Surface([width,height])
        self.color = BLACK
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.beep = pg.mixer.Sound("beep-3.wav")
    def beepit(self):
        self.beep.play()
    def flashit(self, color):
        self.color = color
        self.image.fill(self.color)
    def update(self):
        pass

def main():

    # create an event to be called in time.set_timer() later
    FLASHBLACK = USEREVENT + 1

    #initialize pygame
    pg.init()
    clock = pg.time.Clock()

    # create the screen
    screen = pg.display.set_mode((1000, 800))
    WHITE = pg.Color(255, 255, 255)
    BLACK = pg.Color(0, 0, 0)
    screen.fill(WHITE)

    # create a sprite in the form of a black square on the screen
    square_black = Subject(400, 400, 700, 400)
    square_group = pg.sprite.Group()
    square_group.add(square_black)

    # Title and Icon
    pg.display.set_caption("Flash_Beep")

    # Game Loop
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                square_black.beepit()
                square_black.flashit(WHITE)
                # square_black.flashit_black(BLACK)
                
                
        pg.display.flip()
        square_group.draw(screen)
        square_group.update()
        clock.tick(60)

main()
