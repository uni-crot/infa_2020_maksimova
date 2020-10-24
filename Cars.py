import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((360, 520))
screen.fill((185, 211, 238))
polygon(screen, (96, 123, 139), [(0,330), (360, 330), (360,520), (0,520)])

# ширина и высота в отдельных координатах
width=360
height=520
# поверхность для прозрачности
surface = pygame.Surface((width,height), pygame.SRCALPHA)

#функция для здания
def building(colour,x,y,width,height):
    polygon(screen,colour,[(x,y),(x+width,y),(x+width,y+height),(x,y+height)]) #само здвние
    for i in range (0,9):
        rect(screen, (255,255,0),(x+width//8+width//2,y+width//8+i*(width//4+width//8),width//4,width//4))
        rect(screen, (255,255,0),(x+width//8,y+width//8+i*(width//4+width//8),width//4,width//4))
#функция для фона
def background(x,y, size):
    # дома слева
    building((159, 182, 205),x+10*size, y+ 10*size,70*size,330*size)
    building((150, 205, 205),x+90*size, y+30*size,80*size,320*size)
    building((198, 226, 255),x+60*size, y+80*size,90*size,310*size)
    # дома справа
    building((202, 225, 255),x+270*size, y+10*size,80*size,330*size)
    building((122, 197, 205),x+240*size, y+90*size,80*size,310*size)

#Функция для домов одного цвета
def background_onecolour(x,y, size, COLOUR):
    # дома слева
    polygon(surface,  COLOUR, [(x+10*size, y+ 10*size), (x+80*size, y+10*size), (x+80*size, y+340*size), (x+10*size, y+340*size)])
    #screen.blit(surface, (0, 0))
    polygon(surface,  COLOUR, [(x+90*size, y+30*size), (x+170*size, y+30*size), (x+170*size, y+350*size), (x+90*size, y+350*size)])
    #screen.blit(surface, (0, 0))
    polygon(surface,  COLOUR, [(x+60*size, y+80*size), (x+150*size, y+80*size), (x+150*size, y+390*size), (x+60*size, y+390*size)])
    #screen.blit(surface, (0, 0))
    # дома справа
    polygon(surface,  COLOUR, [(x+270*size, y+10*size), (x+350*size, y+10*size), (x+350*size, y+340*size), (x+270*size, y+340*size)])
    #screen.blit(surface, (0, 0))
    polygon(surface,  COLOUR, [(x+240*size, y+90*size), (x+320*size, y+90*size), (x+320*size, y+400*size), (x+240*size, y+400*size)])
    #screen.blit(surface, (0, 0))

    polygon(surface,  COLOUR, [(x, y), (x+360*size, y), (x+360*size, y+330*size), (x, y+330*size)])
    #screen.blit(surface, (0, 0))

    pygame.draw.ellipse(surface, COLOUR, (x+80*size, y+130*size, 400*size, 80*size))
    #screen.blit(surface, (0, 0))
    pygame.draw.ellipse(surface, COLOUR, (x+40*size, y+30*size, 210*size, 70*size))
    #screen.blit(surface, (0, 0))
    pygame.draw.ellipse(surface, COLOUR, (x+200*size, y-10*size, 210*size, 50*size))
    screen.blit(surface, (0, 0))
    pygame.draw.ellipse(surface, COLOUR, (x+20*size, y+410*size, 110*size, 25*size))
    screen.blit(surface, (0, 0))
    pygame.draw.ellipse(surface, COLOUR, (x+25*size, y+445*size, 110*size, 25*size))
    screen.blit(surface, (0, 0))
    pygame.draw.ellipse(surface, COLOUR, (x-60*size, y+380*size, 110*size, 25*size))
    screen.blit(surface, (0, 0))
# функция для машины
def car(screen, x,y,size,dir):
    surf=pygame.Surface((x+160*size,y+65*size))
    surf.fill((255,255,255))
    surf.set_colorkey((255,255,255))
# выхлопная труба
    pygame.draw.ellipse(surf, (28, 28, 28), (x-10*size, y+10*size, 20*size, 7*size))
# корпус машины
    polygon(surf, (139, 26, 26), [(x,y), (x+(150*size), y),(x+(150*size),y+(30*size)), (x,y+(30*size))])
    polygon(surf, (139, 26, 26), [(x+(30*size),y-(25*size)), (x+(105*size), y-25*size),(x+105*size,y), (x+30*size,y)]) #верх
# окна
    polygon(surf, (248, 248, 255), [(x+35*size,y-20*size), (x+60*size, y-20*size), (x+60*size,y-5*size), (x+35*size,y-5*size)])
    polygon(surf, (248, 248, 255), [(x+75*size,y-20*size), (x+100*size, y-20*size), (x+100*size,y-5*size), (x+75*size,y-5*size)])
# колеса
    pygame.draw.ellipse(surf, (28, 28, 28), (x+10*size, y+20*size, 35*size, 20*size))
    pygame.draw.ellipse(surf, (28, 28, 28), (x+105*size, y+20*size, 35*size, 20*size))
    if dir==1:
        surf=pygame.transform.flip(surf, True, False)
    screen.blit(surf,(x-10*size,y-25*size))

        #тело кода
background_onecolour(-10, 0, 0.75, (0,0,0,20))
background_onecolour(120, 0, 0.75, (0,0,0,20))
background(120, 100, 0.7)
background(-50, 110, 0.7)
car(screen,50,200, 0.4,0)
car(screen,20,250, 0.5,0)
car(screen,100,250, 0.5,0)
car(screen,140,230, 0.5,1)
car(screen,220,200,0.75,1)
car(screen,10,210,0.6,1)




pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          finished = True

pygame.quit()
