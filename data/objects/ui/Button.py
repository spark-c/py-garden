# Button object building block for UI elements

import pygame

import data.ObjectManager as om


class Button(pygame.sprite.Sprite):

    base_sprite = '/resources/sprites/ui/button_base.png'

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(Button.base_sprite).convert_alpha()
        self.rect = self.image.get_rect()

        self.join_groups()


    def update(self):
        pass


    def join_groups(self):
        om.all_sprites.add(self)
        om.buttons.add(self)


class SpawnButton(Button):
    pass