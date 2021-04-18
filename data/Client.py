# Client object to handle pygame variables like SCREEN, CLOCK, etc.

import pygame


class Client():

    def __init__(self, cfg): # pass in Config object
        self.screen = pygame.display.set_mode(cfg.RESOLUTION)
        self.screen_rect = self.screen.get_rect()
        self.bg_color = cfg.BG_COLOR
        self.clock = pygame.time.Clock()
