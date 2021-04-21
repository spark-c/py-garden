# main game loop

import sys
import pygame

from data.Client import Client
import data.StateManager as sm
import data.ObjectManager as om
import config


### INIT ###
cfg = config.get_config()
client = Client(cfg)

pygame.init()
pygame.mouse.set_visible(False)

### IMPORT SPRITES ###
from data.objects.animals.Animal import *
from data.objects.environment.Ground import *
from data.objects.items.Item import *
from data.objects.ui.Cursor import Cursor


def main(client):

    g = Ground(floor_level=60)
    
    d = Animal(ground=g)
    e = Animal(ground=g)

    # a = Item()

    cursor = Cursor()


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


        ### UPDATE OBJECTS ###
        om.all_sprites.update()


        ### DRAW OBJECTS ###
        client.screen.blit(client.background, client.screen_rect)

        om.animals.clear(client.screen, client.background)
        om.cursor.clear(client.screen, client.background)

        om.grounds.draw(client.screen)
        om.animals.draw(client.screen)
        om.items.draw(client.screen)
        om.cursor.draw(client.screen)


        pygame.display.flip()

        client.clock.tick(client.fps)

    pygame.display.quit()
