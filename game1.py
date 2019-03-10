import pygame
import random

def map_gen(pol_width, pol_height, map_width, map_height, obj = []):
    f = open('lvl.txt', 'w')
    f.write('Изначальная карта: \n')
    f.write('\n')
    long = int(map_width / pol_width)
    num_line = int(map_height / pol_height)
    map = []
    i = 0
    j = 0
    for i in range(num_line):
        line = []
        tmp = []
        for j in range(long):
            if (i == 0) or (i == num_line - 1):
                line.append(1)
            elif (j == 0) or (j == long - 1):
                line.append(1)
            elif (i > 2) and (j > 2) and (i < num_line - 3) and (j < long - 3):
                    line.append(random.randint(0,4))
            else:
                line.append(0)
                j += 1
        map.append(line)
        i += 1
        f.write(str(line) + '\n')
    f.write('\n')
    f.close()
    return map

def show_map(Mylist = []):
    for i in Mylist:
        print(i)

#j = 1 -> Стена
#j = 2 -> Моб
#j = 3 -> Дверь горизонт
#j = 4 -> Дверь вверх
def draw_map(start_x, start_y, map = [], *col):
    color = (255, 255, 255)
    x = start_x
    y = start_y
    for i in map:
        for j in i:
            if (j == 1):
                pygame.draw.rect(sc, color, (x, y, width, height))
            elif (j == 2):
                pygame.draw.rect(sc, (255, 0, 255), (x, y, width, height))
            elif (j == 0):
                pygame.draw.rect(sc, (0, 0, 0), (x, y, width, height))
            x += width
        x = 0
        y += height

def norm_frame(lst = []):

    return 0

def form_zone(ind = 3, z_w = 3, z_h = 3, lst =[]):
    for num_fr in range(ind, len(lst[0]) - 1, h):
        fr = []
        for i in range(num_fr, z_h + z_w, 1):
            tmp = lst[i][ind : ind + z_w : 1]
            fr.extend(tmp)
    return fr

def first_anim(*col):
    pygame.draw.rect(sc, col, (x, y, width, height))
    pygame.draw.rect(sc, col, ((WIN_WIDTH - width) - x, (WIN_HEIGHT - height) - y, width, height))
    pygame.draw.rect(sc, col, (x, (WIN_HEIGHT - height) - y, width, height))
    pygame.draw.rect(sc, col, ((WIN_WIDTH - width) - x, y, width, height))
    pygame.draw.rect(sc, col, (WIN_WIDTH / 2, y,width,height))
    pygame.draw.rect(sc, col, (WIN_WIDTH / 2, (WIN_HEIGHT - height) - y, width, height))
    pygame.draw.rect(sc, col, (x, WIN_HEIGHT / 2, width, height))
    pygame.draw.rect(sc, col, ((WIN_WIDTH - width) - x, WIN_HEIGHT / 2,width,height))

def lvl():
    pygame.draw.rect(sc, WHITE, (width, height, WIN_WIDTH - 2 * width, WIN_HEIGHT - 2 * height))
    pygame.draw.rect(sc, BLACK, (WIN_WIDTH / 4,  WIN_HEIGHT // 2 - height, WIN_WIDTH /2, height))

def normal_map(map = []):
    f = open('lvl.txt', 'a')
    f.write('Вариант нормализации карты: \n')
    f.write('\n')
    flag = 0
    for i in map:
        cur_ind = -1
        if (flag > 2) and (flag < len(map) - 4):
            while (cur_ind <= len(i) - 1):
                try:
                    tmp = i.index(2,cur_ind + 1,len(i) - 1)
                    cur_ind = tmp
                    if (cur_ind >= len(i) - 5):
                        i[cur_ind + 1] = 0
                        i[cur_ind + 2] = 0
                    else:
                        i[cur_ind + 1] = random.randint(0, 1)
                        i[cur_ind + 2] = random.randint(0, 1)
                except ValueError:
                    cur_ind = len(i)
        if (flag % 3 == 0):
            print(i)
            for item in range(len(i)):
                i[item] = random.randint(0, 1)
            print(i)
            f.write(str(i) + '\n')
            flag += 1
            continue
        f.write(str(i) + '\n')
        print('')
        flag += 1
    f.write('\n')
    f.close()
    return map

FPS = 40
WIN_WIDTH = 480
WIN_HEIGHT = 480

BLACK = (0, 0, 0)
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
width =  24
height = 24
x = 0  # скрываем за левой границей
y = 0  # выравнивание по центру по вертикали
startpoint = [WIN_WIDTH - 2 * width, WIN_HEIGHT - 2 * height]
map = map_gen(width, height, WIN_WIDTH, WIN_HEIGHT)

print(startpoint)
show_map(map)
print('')
draw_map(x, y, map, RED, GREEN, BLUE)
while True:

    for i in pygame.event.get():
        if i.type == pygame.QUIT: exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                map_fin = normal_map(map)
                draw_map(x, y, map_fin, RED, GREEN, BLUE)

    pygame.display.update()

    clock.tick(FPS)
