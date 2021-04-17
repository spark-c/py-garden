# Main for py-garden

import sys
import pygame as pg
from data.objects.animals import Deer


def fix_runaway(obj):
    if obj.top < 0:
        obj.top = 1
    if obj.bottom > height:
        obj.bottom = height
    if obj.left < 0:
        obj.left = 0
    if obj.right > width:
        obj.right = width


pg.init()
clock = pg.time.Clock()

window_size = width, height = 640, 360
speed = [0, 0]
black = 0, 0, 0

screen = pg.display.set_mode(window_size)

deer = Deer()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        if event.type == pg.KEYDOWN:
            print(event.key, "DOWN")
            if event.key == pg.K_w: speed[1] = -1
            if event.key == pg.K_s: speed[1] = 1
            if event.key == pg.K_a: speed[0] = -1
            if event.key == pg.K_d: speed[0] = 1
        if event.type == pg.KEYUP:
            print(event.key, "UP")
            if event.key == pg.K_w: speed[1] = 0
            if event.key == pg.K_s: speed[1] = 0
            if event.key == pg.K_a: speed[0] = 0
            if event.key == pg.K_d: speed[0] = 0
 
    deer.rect = deer.rect.move(speed * deer.speed_mod)
    fix_runaway(deer.rect)
    
    screen.fill(black)
    screen.blit(deer.image, deer.rect)
    pg.display.flip()

    clock.tick(60)
