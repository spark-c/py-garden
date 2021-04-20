# Cursor sprite

import pygame
import os


class Cursor(pygame.sprite.Sprite):

    sprite_path_base = 'resources/sprites/ui/'

    def __init__(self):
        super().__init__()
        self.clicking = False
        self.sprites = {
            'click': pygame.image.load(os.path.join(self.sprite_path_base, 'cursor_1.png')).convert(),
            'not_click': pygame.image.load(os.path.join(self.sprite_path_base, 'cursor_0.png')).convert()
        }
        self.image = self.sprites['not_click']
        self.rect = self.image.get_rect()
        self.position = pygame.mouse.get_pos()


    def update(self):
        self.position = pygame.mouse.get_pos()

        if self.clicking == False:
            self.image = self.sprites['not_click']
            self.rect = self.image.get_rect()
            self.rect.center = self.position
        
        elif self.clicking == True:
            self.image = self.sprites['click']
            self.rect = self.image.get_rect()
            self.rect.center = self.position






