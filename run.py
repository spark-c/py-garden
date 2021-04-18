# Main for py-garden

import sys
import os

from data.main import main, cfg, client

if __name__ == '__main__':
    main(client)
    sys.exit()

# Code below is just leftover from initial testing

# def enforce_screenspace(obj):
#     if obj.top < 0:
#         obj.top = 1
#     if obj.bottom > height:
#         obj.bottom = height
#     if obj.left < 0:
#         obj.left = 0
#     if obj.right > width:
#         obj.right = width



# while True:
#     for event in pg.event.get():
#         if event.type == pg.QUIT: pg.diplay.quit(), sys.exit()
#         if event.type == pg.KEYDOWN:
#             print(event.key, "DOWN")
#             if event.key == pg.K_w: speed[1] = -1
#             if event.key == pg.K_s: speed[1] = 1
#             if event.key == pg.K_a: speed[0] = -1
#             if event.key == pg.K_d: speed[0] = 1
#         if event.type == pg.KEYUP:
#             print(event.key, "UP")
#             if event.key == pg.K_w: speed[1] = 0
#             if event.key == pg.K_s: speed[1] = 0
#             if event.key == pg.K_a: speed[0] = 0
#             if event.key == pg.K_d: speed[0] = 0
 
#     deer.rect = deer.rect.move(speed * deer.speed_mod)
#     enforce_screenspace(deer.rect)
    
#     screen.fill(bg_color)
#     screen.blit(deer.image, deer.rect)
#     pg.display.flip()

#     clock.tick(60)
