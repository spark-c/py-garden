# main game loop

import sys
import pygame

from data.prepare import init
from data.objects.animals.Deer import Deer


def main():
    init()

    d = Deer()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
        d.rect = d.rect.move(1,0)
        SCREEN.blit(d.image, d.rect)
        pygame.display.flip()
        CLOCK.tick(30)
