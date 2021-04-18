# Base class for Animals

import pygame
import random
import os
import json

import config


class Animal(pygame.sprite.Sprite):
    
    sprite_path_base = 'resources/sprites/animals/'
    movement_constraint = (0, config.Config.RESOLUTION[0])
    
    with open('animal_config.json', 'r') as f:
        config = json.load(f)
    
    types = set(config.keys())


    def __init__(self, animal_type='deer', gender='female'): # args received from subclass e.g. Deer
        super().__init__() # passes to the Sprite.__init__()

        self.animal_type = animal_type
        self.gender = gender

        self.sprite_name_base = '_'.join(self.animal_type, self.gender, 'NUM.png') # "deer_female_NUM.png"
        self.sprite_full_path = os.path.join(Animal.sprite_path_base, self.sprite_name_base)

        self.image = pygame.image.load(self.sprite_full_path)
        self.rect = self.image.get_rect()

        self.head = self.rect.left # later we will update this according to sprite's facing
        self.speed = [0, 0]
    

    ### ACTIONS

    def wander(self): # pick spot and move there.
        print("Finding place...")
        point = random.randint(Animal.movement_constraint[0], Animal.movement_constraint[1]) # target destination
        area = (point-5, point+5) # acceptable range
        print(f"Going to {point}!")

        while self.head < area[0] or self.head > area[1]: # accepts being "close enough"
            if self.head > point:
                self.speed = [-1, 0]
            if self.head < point:
                self.speed = [1, 0]
        self.speed = [0, 0]
        print('Made it!')


    def exit(self): # wander offscreen and cleanup self
        pass


    def eat(self): # eat animation and cleanup nearby food sprite
        pass


    def emote(self, emote_type): # may implement little emote bubbles
        pass


    ### UTILITY

    def draw(self):
        pass