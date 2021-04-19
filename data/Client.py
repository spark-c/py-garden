# Client object to handle pygame variables like SCREEN, CLOCK, etc.

import pygame


class Client():

    def __init__(self, cfg): # pass in Config object
        self.screen = pygame.display.set_mode(cfg.RESOLUTION)
        self.screen_rect = self.screen.get_rect()
        self.bg_color = cfg.BG_COLOR
        self.background = pygame.Surface(cfg.RESOLUTION)
        self.set_background(self.bg_color)

        self.clock = pygame.time.Clock()
        self.fps = 30

    
    def set_background(self, color):
        self.background.fill(color)
