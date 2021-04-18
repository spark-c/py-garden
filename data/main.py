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
from data.objects.animals import *


def main(client):

    d = Deer()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
        d.rect = d.rect.move(1, 0)

        client.screen.fill(client.bg_color)
        client.screen.blit(d.image, d.rect)
        pygame.display.flip()

        client.clock.tick(30)

    pygame.display.quit()
