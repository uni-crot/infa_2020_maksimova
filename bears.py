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

def fish(screen,x,y,w,h,head):
    s_fish=pygame.Surface((x+w,y+h))
    s_fish.fill((255,255,255))
    s_fish.set_colorkey((255,255,255))
    ellipse(s_fish,(173,216,230), (x+h//2,y,w-h//2,h))
    ellipse(s_fish,(0,0,0), (x+h//2,y,w-h//2,h),1)
    polygon(s_fish,(173,216,230),[(x,y),(x,y+h),(x+h//2,y+h//2)])
    polygon(s_fish,(0,0,0),[(x,y),(x,y+h),(x+h//2,y+h//2)],1)
    circle(s_fish,(30,144,255),(x+3*w//4,y+h//2),5)
    circle(s_fish,(0,0,0),(x+3*w//4,y+h//2),3)
    #polygon(s_fish,(240,128,128),[(x+4*w//5,y+h//5),(x+3*w//4,y),(x+h//2,y-h//6),(x+3*h//2,y)])
    if head==1:
        s_fish=pygame.transform.flip(s_fish, True, False)
    if head==2:
        s_fish=pygame.transform.flip(s_fish, False, True)
    screen.blit(s_fish,(x,y))


def draw_bear(screen, x, y, width, height,dir): #вправо
    bear=pygame.Surface((x+2*width,y+height))
    bear.fill((255,255,255))
    bear.set_colorkey((255,255,255))
    w_head=width//2
    w_hbl=width//2
    h_hl2=height//5
    h_body=height//4*3
    w_arm=width//3
    h_arm=height//8
    h_leg2=height//10
    ellipse(bear,(245,245,245), (x+width//4, y+5, width//2,h_hl2)) #head
    ellipse(bear,(0,0,0), (x+width//4, y+5, width//2,h_hl2),1)
    arc(bear,(0,0,0),(x+width//4,y-2,width//2,h_hl2), math.pi*3/2,math.pi*11/6)
    ellipse(bear,(245,245,245),(x, y+height//7,width//2, h_body)) #body
    ellipse(bear,(0,0,0), (x, y+height//7,width//2, h_body),1)
    circle(bear,(0,0,0),(x+width//5*2,y+height//11),3) #eye
    circle(bear,(0,0,0),(x+width//4*3,y+height//10),3) #nose
    arc(bear,(0,0,0),(x+width//2,y+height//13,3*width,height),math.pi*2/3,math.pi,5)#stick
    ellipse(bear,(245,245,245), (x+width//3, y+height//3,w_arm,h_arm)) #arm
    ellipse(bear,(0,0,0), (x+width//3, y+height//3,w_arm,h_arm),1)
    ellipse(bear,(245,245,245), (x+width//4, y+height//3*2,2*width//5,height//4)) #leg1
    ellipse(bear,(0,0,0), (x+width//4, y+height//3*2,2*width//5,height//4),1)
    ellipse(bear,(245,245,245), (x+width//2, y+height//6*5,width//3,h_leg2)) #leg2
    ellipse(bear,(0,0,0), (x+width//2, y+height//6*5,width//3,h_leg2),1)
    #ice
    ellipse(bear,(80,80,80), (x+width,y+height//2,width//2,height//6))
    ellipse(bear,(0,0,0), (x+width,y+height//2,width//2,height//6),1)
    ellipse(bear,(0,80,60), (x+width+5,y+height//2+5,width//2-10,height//7-4))
    ellipse(bear,(0,0,0),(x+width+5,y+height//2+5,width//2-10,height//7-4),1)
    line(bear,(0,0,0),(x+5*width//4,y+2*height//12),(x+5*width//4,y+height//2),1)
    fish(bear,x+width//2,y+4*height//10,50,15,2)
    fish(bear,width+width//8+2,y+height//3,50,15,2)
    fish(bear,width+2,y+height//3,50,15,2)
    fish(bear,width+2,y+2*height//3,50,15,2)



    if dir==1:
        bear=pygame.transform.flip(bear, True, False)
    screen.blit(bear,(x,y))




draw_bear(screen,100,200,100,150,1)
draw_bear(screen,150,300,200,250,1)
draw_bear(screen,0,250,150,200,0)
draw_bear(screen,350,190,70,120,1)





pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
