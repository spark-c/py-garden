# Ground object

import pygame
import os

import config


class Ground(pygame.sprite.Sprite):

    
    def __init__(self, floor_level=40, width=None, start=0):
        super().__init__()
        self.width = width if width else config.Config.RESOLUTION[0]
        self.height = floor_level
        if start + self.width > config.Config.RESOLUTION[0]: # if the width would spill offscreen,
            self.width = config.Config.RESOLUTION[0] - start # reduce width accordingly

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.left = start

        self.rect.bottom = config.Config.RESOLUTION[1]

    
    def update(self):
        pass
