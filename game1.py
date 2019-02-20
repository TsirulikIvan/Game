import pygame
import random

def map_gen(pol_width, pol_height, map_width, map_height, obj = []):
    long = int(map_width/pol_width)
    num_line = int(map_height/pol_height)
    map = []
    i = 0
    j = 0
    for i in range(num_line):
        line = []
        for j in range(long):
            if (i == 0) or (i == num_line - 1):
                line.append(1)
            elif (j == 0) or (j == long - 1):
                line.append(1)
            elif (i > 2) and (j > 2) and (i < num_line - 3) and (j < long - 3):
                    line.append(random.randint(0,1))
            else:
                line.append(0)
                j += 1
        map.append(line)
        i += 1
    return map

def show_map(Mylist = []):
    for i in Mylist:
        print(i)

def draw_map(start_x,start_y,map = [],*col):
    color = (255,255,255)
    x = start_x
    y = start_y
    for i in map:
        for j in i:
            if j == 1:
                pygame.draw.rect(sc, color, (x, y,width,height))
            x += width
        x = 0
        y += height





def first_anim(*col):
    pygame.draw.rect(sc, col, (x, y,width,height))
    pygame.draw.rect(sc, col, ((WIN_WIDTH - width) - x,(WIN_HEIGHT - height) - y,width,height))
    pygame.draw.rect(sc, col, (x, (WIN_HEIGHT - height) - y,width,height))
    pygame.draw.rect(sc, col, ((WIN_WIDTH - width) - x, y,width,height))
    pygame.draw.rect(sc, col, (WIN_WIDTH / 2, y,width,height))
    pygame.draw.rect(sc, col, (WIN_WIDTH / 2, (WIN_HEIGHT - height) - y,width,height))
    pygame.draw.rect(sc, col, (x, WIN_HEIGHT/2,width,height))
    pygame.draw.rect(sc, col, ((WIN_WIDTH - width) - x, WIN_HEIGHT/2,width,height))

def lvl():
    pygame.draw.rect(sc, WHITE, (width, height ,WIN_WIDTH - 2*width,WIN_HEIGHT - 2*height))
    pygame.draw.rect(sc, BLACK, (WIN_WIDTH / 4,  WIN_HEIGHT // 2 - height,WIN_WIDTH /2, height))

def pack(*args):
    return args
FPS = 40
WIN_WIDTH = 480
WIN_HEIGHT = 480

BLACK = (0,0,0)
RED = 255
GREEN = 0
BLUE = 0
CUSTOM_COL = (RED, GREEN, BLUE)
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)

pygame.init()

clock = pygame.time.Clock()

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# радиус и координаты круга
width =  16
height = 16
x = 0  # скрываем за левой границей
y = 0  # выравнивание по центру по вертикали
startpoint = [WIN_WIDTH - 2*width,WIN_HEIGHT - 2*height]
map = map_gen(width,height,WIN_WIDTH, WIN_HEIGHT)

print(startpoint)
#show_map(map)
draw_map(x,y,map,RED,GREEN,BLUE)
while 1:


    for i in pygame.event.get():
        if i.type == pygame.QUIT: exit()
    pygame.display.update()


    clock.tick(FPS)
