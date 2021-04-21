# Item base class

import pygame
import os

import data.ObjectManager as om
import config

class Item(pygame.sprite.Sprite):

    sprite_path_base = 'resources/sprites/items/'

    def __init__(self, item_type='apple'):
        super().__init__()
        
        self.item_type = item_type
        self.image = pygame.image.load(os.path.join(Item.full_path, self.item_type)).convert_alpha()
        self.rect = self.image.get_rect()


        self.join_groups()


    def update(self):
        pass


    def join_groups(self):
        om.all_sprites.add(self)
        om.items.add(self)
        
        