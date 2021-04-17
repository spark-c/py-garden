# sets up config / inits

import config


cfg = config.get_config()
SCREEN_SIZE = cfg.RESOLUTION

def init():
    import pygame

    SCREEN = pygame.display.set_mode(SCREEN_SIZE)
    SCREEN_RECT = SCREEN.get_rect()

    pygame.init()
    CLOCK = pygame.time.Clock()