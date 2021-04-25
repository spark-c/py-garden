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
        self.fps = cfg.CLIENT_FPS

        ### PLAYER / GAME VARS ###
        self.food_bag = 999
        self.total_food_eaten = 0

    
    def set_background(self, color):
        self.background.fill(color)
