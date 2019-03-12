import pygame
import random


def map_gen(pol_width, pol_height, map_width, map_height, obj = [ ]):
    f = open('lvl.txt', 'w')
    f.write('Изначальная карта: \n')
    f.write('\n')
    long = int(map_width / pol_width)
    num_line = int(map_height / pol_height)
    map = [ ]
    i = 0
    j = 0
    for i in range(num_line):
        line = [ ]
        tmp = [ ]
        for j in range(long):
            if (i == 0) or (i == num_line - 1):
                line.append(1)
            elif (j == 0) or (j == long - 1):
                line.append(1)
            elif (i > 2) and (j > 2) and (i < num_line - 3) and (j < long - 3):
                    line.append(random.randint(0,6))
            else:
                line.append(0)
                j += 1
        map.append(line)
        i += 1
        f.write(str(line) + '\n')
    f.write('\n')
    f.close()
    return map


def show_map(Mylist = [ ]):
    for i in Mylist:
        print(i)

"""

j = 1 -> Стена
j = 2 -> Дверь горизонт
j = 3 -> Дверь вверх


"""


def draw_map(start_x, start_y, map = [ ], *col):
    color = (255, 255, 255)
    x = start_x
    y = start_y
    for i in map:
        for j in i:
            if (j == 1) | (j == 3):
                pygame.draw.rect(sc, color, (x, y, width, height))
            elif (j == 6):
                pygame.draw.rect(sc, (255, 0, 255), (x, y, width, height / 8))
            elif (j == 2):
                pygame.draw.rect(sc, (255, 160, 0), (x + 7, y + 7, width / 2, height / 2))
            x += width
        x = 0
        y += height


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
    for i in range(len(map[0]) - 1):
        cur_ind = -1
        while (cur_ind <= len(map[i]) - 2):
            try:
                tmp = map[i].index(6,cur_ind + 1,len(map[i]) - 1)
                cur_ind = tmp
                map[i - 1][cur_ind] = 0
                map[i][cur_ind - 1] = 1
                map[i][cur_ind + 1] = 1
                map[i + 1][cur_ind - 1] = random.randint(0,5)
                map[i + 1][cur_ind] = 0
                map[i + 1][cur_ind + 1] = random.randint(0,5)
            except ValueError:
                cur_ind = len(map[i])
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

width = 24
height = 24
x = 0
y = 0
startpoint = [WIN_WIDTH - 2 * width, WIN_HEIGHT - 2 * height]
map = map_gen(width, height, WIN_WIDTH, WIN_HEIGHT)
print(startpoint)
show_map(map)
print('')
draw_map(x, y, map, RED, GREEN, BLUE)
while True:
    sc.fill(BLACK)
    draw_map(x, y, map, RED, GREEN, BLUE)
    for i in pygame.event.get():
        if i.type == pygame.QUIT: exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                map_fin = normal_map(map)
                draw_map(x, y, map_fin, RED, GREEN, BLUE)

    pygame.display.update()

    clock.tick(FPS)
