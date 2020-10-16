import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))
rect(screen, (255, 255, 255), (0, 0, 600, 600))
circle(screen, (255, 255, 0), (300, 300),200)
circle(screen, (0, 0, 0), (300, 300),200,5)
circle(screen, (0, 0, 0), (380, 250),25,5)
circle(screen, (255, 0, 0), (380, 250),25)
circle(screen, (0, 0, 0), (380, 250),13)
rect(screen, (0, 0, 0), (200, 400, 200, 40))
circle(screen, (0, 0, 0), (220, 250),25,5)
circle(screen, (255, 0, 0), (220, 250),35)
circle(screen, (0, 0, 0), (220, 250),13)
polygon(screen, (0, 0, 0), [(340,240), (335,230),
                               (500,170), (505,180)])
polygon(screen, (0, 0, 0), [(255,230), (260,215),
                               (100,160), (95,175)])



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
