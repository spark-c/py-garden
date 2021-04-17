# Base class for Flora

from pygame.sprite import Sprite


class Flora(Sprite):
    
    flora_path = 'resources/sprites/flora/'

    def __init__(self):
        super().__init__()