# main game loop

import sys
import pygame

from data.Client import Client
import data.StateManager as sm
import config


### INIT ###
cfg = config.get_config()
client = Client(cfg)

pygame.init()

### IMPORT SPRITES ###
from data.objects.animals.Animal import *
from data.objects.environment.Ground import *


def main(client):

    
    client.screen.blit(client.background, client.screen_rect)
    
    g = Ground(floor_level=60)
    ground_group = pygame.sprite.Group(g)
    ground_group.draw(client.screen)
    
    d = Animal(ground=g)
    e = Animal(ground=g)

    ### GROUPS ###
    all_animals = pygame.sprite.Group(d, e)

    sm.idle.add(d, e)

    ### MAIN LOOP ###
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()

        ### EVENTS ###
        for sprite in sm.idle.sprites():
            sprite.idle()
        
        for sprite in sm.wandering.sprites():
            sprite.wander()


        ### DRAW ENVIRONMENT ###


        ### DRAW OBJECTS ###
        all_animals.update()
        all_animals.clear(client.screen, client.background)
        all_animals.draw(client.screen)

        pygame.display.flip()

        client.clock.tick(client.fps)

    pygame.display.quit()
