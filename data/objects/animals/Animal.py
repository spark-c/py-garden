# Base class for Animals

import pygame
import random
import os
from data import prepare



class Animal(pygame.sprite.Sprite):
    
    sprites_path = 'resources/sprites/animals/'
    movement_constraint = (0, prepare.SCREEN_SIZE[0])

    def __init__(self, sprite_path): # args received from subclass e.g. Deer
        super().__init__() # passes to the Sprite.__init__()
        self.image = pygame.image.load(sprite_path)
        self.rect = self.image.get_rect()
    

    def wander(self): # pick spot and move there.
        
        pass


    def exit(self): # wander offscreen and cleanup self
        pass


    def eat(self): # eat animation and cleanup nearby food sprite
        pass


    def emote(self, emote_type): # may implement little emote bubbles
        pass