import pygame
import random


def map_gen(pol_width, pol_height, map_width, map_height, obj = [ ]):
    f = open('lvl.txt', 'w')
    f.write('First map: \n')
    f.write('\n')
    long = int(map_width / pol_width)
    print(long)
    num_line = int(map_height / pol_height)
    print(num_line)
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
                pygame.draw.rect(sc, (255, 160, 0), (x + int(width / 4), y, width / 2, height / 2))
            elif (j == 7):
                pygame.draw.rect(sc, (255, 0, 255), (x, y, width / 8, height))
            x += width
        x = 0
        y += height


def normal_map(map = []):
    f = open('lvl.txt', 'a')
    f.write('Normal map: \n')
    f.write('\n')
    for i in range(len(map[0]) - 1):
        cur_ind = -1
        while (cur_ind <= len(map[i]) - 2):
            try:
                tmp = map[i].index(6,cur_ind + 1,len(map[i]) - 1)
                cur_ind = tmp
                map[i - 1][cur_ind] = 0
                map[i][cur_ind - 1] = 1
                map[i][cur_ind + 1] = 1
                map[i][cur_ind - 2] = 1
                map[i][cur_ind + 2] = 1
                map[i + 1][cur_ind - 1] = random.randint(0,5)
                map[i + 1][cur_ind] = 0
                map[i + 1][cur_ind + 1] = random.randint(0,5)
            except ValueError:
                cur_ind = len(map[i])
        f.write(str(map[i]) + '\n')
    f.write('\n')
    f.close()
    return map


FPS = 40
WIN_WIDTH = 840
WIN_HEIGHT = 840
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

width = 30
height = 30
x = 0
y = 0
x_hero = width
y_hero = height
map = map_gen(width, height, WIN_WIDTH, WIN_HEIGHT)
map = normal_map(map)
draw_map(x, y, map, RED, GREEN, BLUE)

speed_x = width / 2
speed_y = height / 2
key_count = 0
while True:
    sc.fill(BLACK)
    draw_map(x, y, map, RED, GREEN, BLUE)
    pygame.draw.rect(sc, (0, 255, 0), (x_hero, y_hero, width / 2, height / 2))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_a:
                x_hero -= speed_x
                if (map[int(y_hero / height)][int(x_hero / width)] == 1) | (
                        map[int(y_hero / height)][int(x_hero / width)] == 3):
                    x_hero += speed_x
            elif i.key == pygame.K_d:
                x_hero += speed_x
                if (map[int(y_hero / height)][int(x_hero / width)] == 1) | (
                        map[int(y_hero / height)][int(x_hero / width)] == 3):
                    x_hero -= speed_x
            elif i.key == pygame.K_s:
                y_hero += speed_y
                if (map[int(y_hero / height)][int(x_hero / width)] == 1) | (
                        map[int(y_hero / height)][int(x_hero / width)] == 3):
                    y_hero -= speed_y
            elif i.key == pygame.K_w:
                y_hero -= speed_y
                if (map[int(y_hero / height)][int(x_hero / width)] == 1) | (
                        map[int(y_hero / height)][int(x_hero / width)] == 3):
                    y_hero += speed_y
    ind_i = y_hero / height
    ind_j = x_hero / width
    obj = map[int(ind_i)][int(ind_j)]
    #print('x = ' + str(x_hero) + ' y = ' + str(y_hero) + ' indI = ' + str(ind_i) + ' indJ = ' + str(
   #     ind_j) + ' obj = ' + str(obj))
    if (obj == 2):
        map[int(ind_i)][int(ind_j)] = 0
        key_count += 1
    elif (obj == 6) & (key_count != 0):
        key_count -= 1
        map[int(ind_i)][int(ind_j)] = 7
    elif (obj == 6) & (key_count == 0):
        y_hero -= speed_y

    pygame.display.update()
    clock.tick(FPS)
