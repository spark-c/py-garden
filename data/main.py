# main game loop

import sys
import pygame

from data.Client import Client
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
    
    ground_group = pygame.sprite.Group()
    ga = Ground(floor_level=300, width=200, start=200)
    gb = Ground(floor_level=100, width=100)
    ground_group.add(ga)
    ground_group.add(gb)
    ground_group.draw(client.screen)
    
    d = Animal(ground=ga)
    e = Animal(ground=gb)
    all_animals = pygame.sprite.Group()
    all_animals.add(d)
    all_animals.add(e)

    ### MAIN LOOP ###
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()

        ### EVENTS ###
        for sprite in all_animals.sprites():
            sprite.wander()

        ### DRAW ENVIRONMENT ###


        ### DRAW OBJECTS ###
        all_animals.update()
        all_animals.clear(client.screen, client.background)
        all_animals.draw(client.screen)

        pygame.display.flip()

        client.clock.tick(client.fps)

    pygame.display.quit()
