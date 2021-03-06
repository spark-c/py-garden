# Base class for Animals

import pygame
import random
import os
import json

import data.StateManager as sm
import data.ObjectManager as om
import config


class Animal(pygame.sprite.Sprite):
    
    sprite_path_base = 'resources/sprites/animals/'
    movement_constraint = (0, config.Config.RESOLUTION[0])
    
    with open('data/objects/animals/animal_config.json', 'r') as f:
        config = json.load(f)
    
    types = set(config.keys())

    


    def __init__(self, ground=None, animal_type='deer', gender='female'): # args received from subclass e.g. Deer
        super().__init__() # passes to the Sprite.__init__()
        fps = config.Config.CLIENT_FPS

        self.animal_type = animal_type
        self.gender = gender

        self.sprite_name_base = self.animal_type + '_' + self.gender + 'NUM.png' # "deer_female_NUM.png"
        self.sprite_full_path = os.path.join(os.getcwd(), Animal.sprite_path_base, self.sprite_name_base)

        self.image = pygame.image.load(self.sprite_full_path.replace('NUM', '0')).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.bottom = ground.rect.top if ground else config.Config.RESOLUTION[1] - 41

        self.head = self.rect.left # later we will update this according to sprite's facing
        self.speed = [0, 0]

        self.speed_mod = int(Animal.config[animal_type]['speed_mod'])
        self.movement_constraint = (ground.rect.left, ground.rect.right) if ground else (0, config.Config.RESOLUTION[0])
        self.dest_point = None
        self.dest_area = None

        self.state_constraints = {
            'idle': {
                'min_frames': int(Animal.config[animal_type]['min_idle_seconds']) * fps,
                'max_frames': int(Animal.config[animal_type]['max_idle_seconds']) * fps
            },
            'eating': {
                'min_frames': int(Animal.config[animal_type]['min_eating_seconds']) * fps,
                'max_frames': int(Animal.config[animal_type]['max_eating_seconds']) * fps
            }
        }

        self.state = 'idle'
        self.frames_in_state = 0
        self.state_exit_trigger = 60 # wait 1 second after init, then wander

        self.nearby_food = pygame.sprite.Group()
        self.in_eating_range = pygame.sprite.Group()
        self.food_eaten = 0

        self.join_groups()




    

    ### ACTIONS ###

    def wander(self): # pick spot and move there.
        if self.dest_point == None:
            food = self.check_nearby_food()
            if food:
                print('Food nearby!')
                self.dest_point = food
            else:
                print('I don\'t see food')
                self.dest_point = random.randint(self.movement_constraint[0], self.movement_constraint[1]) # target destination

            self.dest_area = (self.dest_point-2, self.dest_point+2) # acceptable range

        if self.head < self.dest_area[0] or self.head > self.dest_area[1]: # accepts being "close enough"
            if self.head > self.dest_point:
                self.speed = [-1, 0]
            if self.head < self.dest_point:
                self.speed = [1, 0]
        else:
            self.dest_point = None
            self.speed = [0, 0]

            if len(self.in_eating_range) > 0:
                self.change_state('eating')
            else:
                self.change_state('idle')
        
        if len(self.in_eating_range) > 0: # repeated so that we will notice if we accidentally walk over food
            self.dest_point = None
            self.speed = [0, 0]
            self.change_state('eating')


    def idle(self):
        if len(self.nearby_food.sprites()) > 0 or self.frames_in_state > self.state_exit_trigger: # if food is nearby or if it's time to wander
            self.change_state('wandering')
        else:
            self.frames_in_state += 1
    
    
    def exit(self): # wander offscreen and cleanup self
        pass


    def eat(self): # eat animation and cleanup nearby food sprite
        if self.frames_in_state > self.state_exit_trigger:
            for item in self.in_eating_range.sprites():
                if item.alive(): # to prevent another animal getting food_eaten credit despite item being already gone
                    item.kill()
                    self.food_eaten += 1
            self.change_state('idle')
        else:
            self.frames_in_state += 1


    def emote(self, emote_type): # may implement little emote bubbles
        pass


    def check_nearby_food(self): # check whether there is food nearby. returns coords or None.
        for item in om.items.sprites():
            if item.rect.bottom == self.rect.bottom and abs(item.rect.center[0] - self.rect.center[0]) < 200:
                return item.rect.center[0]

        return None 


    ### UTILITY ###
    def change_state(self, state):
        self.frames_in_state = 0

        if state != 'wandering':
            self.set_exit_trigger(state)

        sm.swap_state_group(self, state)
        self.state = state



    def set_exit_trigger(self, state):
        self.state_exit_trigger = random.randint(\
            self.state_constraints[state]['min_frames'],\
            self.state_constraints[state]['max_frames'])
        print(f"Exiting state {self.state} in {self.state_exit_trigger // 60}")


    def update(self):
        self.rect = self.rect.move([s * self.speed_mod for s in self.speed])
        self.head = self.rect.left


    def join_groups(self):
        om.all_sprites.add(self)
        om.animals.add(self)
        sm.idle.add(self)