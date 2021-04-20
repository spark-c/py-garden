# Handles Groups/States

import pygame
import random


### GROUPS FOR STATE MANAGEMENT ###
wandering = pygame.sprite.Group()
idle = pygame.sprite.Group()
# bored = pygame.sprite.Group()
eating = pygame.sprite.Group()

### FUNCTIONS ###
def swap_state_group(obj, new_state):
    old_state = obj.state

    if old_state == 'idle':
        idle.remove(obj)
    elif old_state == 'wandering':
        wandering.remove(obj)
    elif old_state == 'eating':
        eating.remove(obj)
    # elif old_state == 'bored':
    #     bored.remove(obj)

    if new_state == 'idle':
        idle.add(obj)
        return
    elif new_state == 'wandering':
        wandering.add(obj)
        return
    elif new_state == 'eating':
        eating.add(obj)
        return
    # elif new_state == 'bored':
    #     bored.add(obj)
    #     return