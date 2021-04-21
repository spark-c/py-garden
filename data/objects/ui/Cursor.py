# Cursor sprite

import pygame
import os

import data.ObjectManager as om
import config


class Cursor(pygame.sprite.Sprite):

    sprite_path_base = 'resources/sprites/ui/'
    colorkey = config.Config.COLORKEY

    def __init__(self):
        super().__init__()
        self.clicking = False
        self.sprites = {
            'click': pygame.image.load(os.path.join(self.sprite_path_base, 'cursor_1.png')).convert(),
            'not_click': pygame.image.load(os.path.join(self.sprite_path_base, 'cursor_0.png')).convert()
        }
        self.image = self.sprites['not_click']
        self.image.set_colorkey(Cursor.colorkey)
        self.rect = self.image.get_rect()
        self.position = pygame.mouse.get_pos()

        self.join_groups()

        


    def update(self):
        self.position = pygame.mouse.get_pos()

        if self.clicking == False:
            self.image = self.sprites['not_click']
            self.rect = self.image.get_rect()
            self.rect.topleft = self.position
        
        elif self.clicking == True:
            self.image = self.sprites['click']
            self.rect = self.image.get_rect()
            self.rect.topleft = self.position

        self.image.set_colorkey(Cursor.colorkey)

    
    def join_groups(self):
        om.all_sprites.add(self)
        om.cursor.add(self)






