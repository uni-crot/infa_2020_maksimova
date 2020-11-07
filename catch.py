import pygame
from pygame.draw import *
import random
import datetime
import math

pygame.init()

# экран и основные переменные
FPS = 40
width = 1100
height = 700
screen = pygame.display.set_mode((width, height))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

# инициализация шрифта для очков
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

score = 0  # инициализация счета по шарам
points = 0 # счет по прямоугольникам
n = 4 # количество шаров
balls = [] # массив шаров, где balls[i][j] это число x, если j=0; y, если j=1; r если j=2 i-го шара
# массив скоростей шаров, где i - номер шара, j - если 0, то количество пикселей по ОХ, если 1 - то по ОУ
balls_speeds = []
balls_colors = [] # массив цветов
rects = [] # массив прямоугольников, где rects[i][j] это число x при j=0; y, если j=1, ширина, если j=2; высота, если j=3 i-го прямоугольника
rects_speeds = [] # массив скоростей прямоугольника
rects_colors = []

hsfile = open('highscores.txt', 'a') #открытие файла, в котором будут результаты игры


def init_balls(): #инициализация 4 случайных шаров
    for i in range(n):
        balls.append([random.randint(100, width),random.randint(100, height),random.randint(10, 100)])
        balls_speeds.append([random.randint(-4, 5), random.randint(-4, 5)])
        balls_colors.append(COLORS[random.randint(0, 5)])

def init_rects(): #инициализация случайных прямоугольников
    for i in range (n):
        rects.append([random.randint(100, width),random.randint(100, height-30),random.randint(50, 200),random.randint(50,200)])
        rects_speeds.append([random.randint(-4, 5), random.randint(-4, 5)])
        rects_colors.append(COLORS[random.randint(0, 5)])

def update_balls(): #для передвижения шаров и отражения шаров от рамок экрана
    for i in range(n):
        balls[i][0] += balls_speeds[i][0]
        balls[i][1] += balls_speeds[i][1]
        if balls[i][0] <= balls[i][2]:
            balls_speeds[i][0] = random.randint(0, 5)
        if balls[i][1] <= balls[i][2]:
            balls_speeds[i][1] = random.randint(0, 5)
        if balls[i][0] + balls[i][2] >= width:
            balls_speeds[i][0] = random.randint(-4, 0)
        if balls[i][1] + balls[i][2] >= height:
            balls_speeds[i][1] = random.randint(-4, 0)

def update_rects(): #для передвижения прямоугольников и отражения от рамок экрана
    for i in range(n):
        rects[i][0] += rects_speeds[i][0]+math.cos(math.pi/(i+1))
        rects[i][1] += rects_speeds[i][1]+math.sin(math.pi/(i+1))
        if rects[i][0] <= rects[i][2]:
            rects_speeds[i][0] = random.randint(0, 5)
        if rects[i][1] <= 0:
            rects_speeds[i][1] = random.randint(0, 5)
        if rects[i][0] + rects[i][2] >= width:
            rects_speeds[i][0] = random.randint(-4, 0)
        if rects[i][1] + rects[i][3] >= height:
            rects_speeds[i][1] = random.randint(-4, 0)

# обновляем счет
def update_score(event, score):
    eventX = event.pos[0]
    eventY = event.pos[1]
    for i in range(n):
        x = balls[i][0]
        y = balls[i][1]
        r = balls[i][2]
        if ((x-eventX)**2+(y-eventY)**2)<=r**2 :
            score=score+1
            balls[i] = [random.randint(100, 1100),random.randint(100, 900),random.randint(10, 100)]
            balls_speeds[i] = [random.randint(-4, 5), random.randint(-4, 5)]
            balls_colors [i]= COLORS[random.randint(0, 5)]
    return score

def update_points(event, points):
    eventX = event.pos[0]
    eventY = event.pos[1]
    for i in range(n):
        x1 = rects[i][0]
        y1 = rects[i][1]
        w1 = rects[i][2]
        h1 = rects[i][3]
        if (((eventX<=(x1+w1)) and (eventX>=x1)) and ((eventY<=(y1+h1)) and (eventY>= y1)))== True:
            points=points+1
            rects[i] = [random.randint(100, width),random.randint(100, height-30),random.randint(50, 200),random.randint(50,200)]
            rects_speeds[i] = [random.randint(-4, 5), random.randint(-4, 5)]
            rects_colors [i]= COLORS[random.randint(0, 5)]
    return points

# выводим счет на экран
def print_score(score):
    scoreText = myfont.render(str(score), False, WHITE)
    screen.blit(scoreText, (0, 0))
def print_points(points):
    pointsText = myfont.render(str(points), False, WHITE)
    screen.blit(pointsText, (0, 20))
# отрисовываем все элементы
def draw(score,points):
    screen.fill(BLACK)
    print_score(score)
    print_points(points)
    for i in range(n):
        circle(screen, balls_colors[i], (balls[i][0], balls[i][1]), balls[i][2])
        rect(screen,rects_colors[i], (rects[i][0], rects[i][1],rects[i][2],rects[i][3]))
    pygame.display.update()

def update_highscores(score): #запись результатов игры
    time = datetime.datetime.now()
    temp = str(time.day) + "." + str(time.month) + "." + str(time.year) + " " + str(time.hour) + ":" + str(time.minute) + ":" + str(time.second) + " score :" + str(score) +"\n"
    hsfile.write(temp)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

init_balls()
init_rects()
#основоной цикл
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            update_highscores(score)
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            score = update_score(event, score)
            points = update_points(event, points)
    update_balls()
    update_rects()
    draw(score,points)

pygame.quit()
