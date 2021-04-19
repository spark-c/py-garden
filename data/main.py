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


def main(client):

    d = Animal()
    all_animals = pygame.sprite.Group()
    all_animals.add(d)

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
        client.screen.blit(client.background, client.screen_rect)

        ### DRAW OBJECTS ###
        all_animals.update()
        all_animals.draw(client.screen)

        pygame.display.flip()

        client.clock.tick(client.fps)

    pygame.display.quit()
