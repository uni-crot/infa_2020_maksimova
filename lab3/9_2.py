import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 700))
rect(screen, (0, 255, 255), (0, 0, 500, 400))
rect(screen, (245, 245, 245), (0, 400, 500, 300))
line(screen, (0,0,0), (0,400),(500,400),2)
#sun
surface1 = screen.convert_alpha()
surface1.fill([0,0,0,0])
pygame.draw.circle(surface1, (245, 245, 220, 200), (300, 150), 150,25)
circle(surface1, (240, 230, 140, 150), (295, 150),30)
pygame.draw.line(surface1,(245, 245, 220,200),(150,145),(450,150),20)
pygame.draw.line(surface1,(245, 245, 220, 200),(300,0),(290,300),20)
screen.blit(surface1, (0,0))

bear=pygame.display.set_mode((400,400))
ellipse(bear,(245,245,245), (87, 267,100,60))
ellipse(bear,(0,0,0), (87,267,100,60),1)
ellipse(bear,(245,245,245), (0, 300,150,270))
ellipse(bear,(0,0,0), (0, 300,150,270),1)
circle(bear,(0,0,0),(130,286),3)
circle(bear,(0,0,0),(185,290),3)
arc(bear, (0,0,0),(-90,290,300,20),math.pi*5/3, math.pi*11/6)
arc(bear,(0,0,0),(150,300,900,300),math.pi*2/3,math.pi,5) #stick
arc(bear,(0,0,0),(95,270,20,20),math.pi/6, math.pi*3/2) #ear
ellipse(bear,(245,245,245), (95, 270,20,20))
line(bear,(0,0,0),(103,288),(113,274),1)
ellipse(bear,(245,245,245), (130, 385,65,30))
ellipse(bear,(0,0,0), (130, 385,65,30),1)
ellipse(bear,(245,245,245), (90, 500,100,80))
ellipse(bear,(0,0,0), (90, 500,100,80),1)
ellipse(bear,(245,245,245), (155, 555,80,30))
ellipse(bear,(0,0,0), (155, 555,80,30),1)
screen.blit(bear, (0,0))





pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
