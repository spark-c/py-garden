# Base class for Animals

import pygame as pg
import os


class Animal(pg.sprite.Sprite):
    
    sprites_path = 'resources/sprites/animals/'

    def __init__(self, width, height, sprite_path): # args received from subclass e.g. Deer
        super().__init__(width, height) # passes to the Sprite.__init__()
        self.image = pg.image.load(sprite_path)
        self.rect = self.image.get_rect()