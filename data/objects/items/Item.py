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
        self.image = pygame.image.load(os.path.join(Item.sprite_path_base, self.item_type + '.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pygame.mouse.get_pos()
        self.y = self.rect.center[1]

        self.speed = [0, 0]
        self.gravity_counter = 0
        self.max_y = self.get_max_y()

        self.join_groups()


    def update(self): # item falling to the ground
        if self.rect.bottom < self.max_y: # if the item is not on the ground
            self.speed = [0, 1]
            if self.rect.bottom + self.speed[1] + self.gravity_counter > self.max_y: # check whether it would pass the ground in the next frame
                self.speed = [0, 0]
                self.gravity_counter = 0
                self.rect.bottom = self.max_y # land cleanly
            else:
                self.gravity_counter += config.Config.GRAVITY_INCREMENT
                self.rect = self.rect.move(self.speed[0], int(self.speed[1] + self.gravity_counter)) # int() rounds the speed down until it hits next number


    def get_max_y(self):
        highest = 0
        for sprite in om.grounds.sprites():
            if sprite.rect.topleft[0] < self.y < sprite.rect.topright[0]: 
                if sprite.rect.top > highest:
                    highest = sprite.rect.top 

        return highest


    def join_groups(self):
        om.all_sprites.add(self)
        om.items.add(self)
        
        