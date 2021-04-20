# Item base class

import pygame


class Item(pygame.sprite.Sprite):

    sprite_path base = 'resources/sprites/items/'

    def __init__(self):
        super().__init__()
        
        self.item_type = item_type
        
        