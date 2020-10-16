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
pygame.draw.line(surface1,(245, 245, 220,200),(150,145),(450,150),20)
pygame.draw.line(surface1,(245, 245, 220, 200),(300,0),(290,300),20)
pygame.draw.circle(surface1, (245, 245, 220, 250), (300, 150),20)
screen.blit(surface1, (0,0))
#bear
ellipse(screen,(245,245,245), (87, 267,100,60))
ellipse(screen,(0,0,0), (87,267,100,60),1)
ellipse(screen,(245,245,245), (0, 300,150,270))
ellipse(screen,(0,0,0), (0, 300,150,270),1)
circle(screen,(0,0,0),(130,286),3)
circle(screen,(0,0,0),(185,290),3)
arc(screen, (0,0,0),(-90,290,300,20),math.pi*5/3, math.pi*11/6)
arc(screen,(0,0,0),(150,300,900,300),math.pi*2/3,math.pi,5) #stick
arc(screen,(0,0,0),(95,270,20,20),math.pi/6, math.pi*3/2) #ear
ellipse(screen,(245,245,245), (95, 270,20,20))
line(screen,(0,0,0),(103,288),(113,274),1)

ellipse(screen,(245,245,245), (130, 385,65,30))
ellipse(screen,(0,0,0), (130, 385,65,30),1)
ellipse(screen,(245,245,245), (90, 500,100,80))
ellipse(screen,(0,0,0), (90, 500,100,80),1)
ellipse(screen,(245,245,245), (155, 555,80,30))
ellipse(screen,(0,0,0), (155, 555,80,30),1)
#ice
ellipse(screen,(80,80,80), (285, 480,170,60))
ellipse(screen,(0,0,0), (285, 480,170,60),1)
ellipse(screen,(0,80,60), (300, 500,140,40))
ellipse(screen,(0,0,0), (300, 500,140,40),1)
line(screen,(0,0,0),(375,320),(375,510),1)
#fish
polygon(screen, (173,216,230),[(350,610),(340,595),(340,625)])
polygon(screen, (0,0,0),[(350,610),(340,595),(340,625)],1)
ellipse(screen, (173,216,230),(350,600,70,20))
ellipse(screen, (0,0,0),(350,600,70,20), 1)
circle(screen, (30,144,255),(400,610),5)
circle(screen, (0,0,0),(401,611),2)
polygon(screen,(255,255,255), [(400,609),(401,608),(399,607),(398,606)])
polygon(screen,(240,128,128),[(396,600),(393,590),(367,592),(380,600)])
polygon(screen,(240,128,128),[(400,618),(406,625),(400,630),(396,618)])
polygon(screen,(240,128,128),[(365,618),(355,630),(375,627),(372,616)])
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
