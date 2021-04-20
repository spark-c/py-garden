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
pygame.mouse.set_visible(False)

### IMPORT SPRITES ###
from data.objects.animals.Animal import *
from data.objects.environment.Ground import *
from data.objects.ui.Cursor import Cursor


def main(client):

    
    client.screen.blit(client.background, client.screen_rect)
    all_sprites = pygame.sprite.Group()
    
    g = Ground(floor_level=60)
    ground_group = pygame.sprite.Group(g)
    ground_group.draw(client.screen)
    
    d = Animal(ground=g)
    e = Animal(ground=g)

    cursor = Cursor()
    cursor_group = pygame.sprite.Group(cursor)

    ### GROUPS ###
    all_animals = pygame.sprite.Group(d, e)

    sm.idle.add(d, e)

    ### MAIN LOOP ###
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor.clicking = True
            if event.type == pygame.MOUSEBUTTONUP:
                cursor.clicking = False

        ### EVENTS ###
        for sprite in sm.idle.sprites():
            sprite.idle()
        
        for sprite in sm.wandering.sprites():
            sprite.wander()

        all_sprites.add(\
            all_animals.sprites(),
            ground_group.sprites(),
            cursor_group.sprites()
        )

        ### DRAW ENVIRONMENT ###


        ### DRAW OBJECTS ###
        all_sprites.update()

        all_animals.clear(client.screen, client.background)
        cursor_group.clear(client.screen, client.background)
        all_animals.draw(client.screen)

        ground_group.draw(client.screen)

        cursor_group.draw(client.screen)


        pygame.display.flip()

        client.clock.tick(client.fps)

    pygame.display.quit()
