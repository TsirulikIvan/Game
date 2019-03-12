import pygame
import random
import os


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
            sc.blit(text1, (x, y))
            if (j == 1) | (j == 3):
                sc.blit(text2, (x, y))
            elif (j == 6):
                sc.blit(text_d_h, (x, y))
                sc.blit(text_d_h1, (x + width / 2, y))
            elif (j == 2):
                sc.blit(text3, (x, y))
            elif (j == 12):
                sc.blit(text_d_v, (x, y))
                sc.blit(text_d_v1, (x + width - 4, y))
            elif (j == 18):
                sc.blit(text1, (x, y))
            x += width
        x = 0
        y += height

def enemy_spawn(sig_val = 18):
    global my_map
    global ind_i
    global ind_j
    try:
        ene_i = ind_i - random.randint(4, 6)
        print(ene_i)
        ene_j = ind_j + random.randint(-3, 3)
        print(ene_j)
        my_map[int(ene_i)][int(ene_j)] = sig_val
    except IndexError:
        print('Spawn Error')


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
INT_WIDTH = 260
BLACK = (0, 0, 0)
RED = 255
GREEN = 0
BLUE = 0
CUSTOM_COL = (RED, GREEN, BLUE)
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)

print(os.getcwd())
text1 = pygame.image.load('crystal_floor5.png')
text2 = pygame.image.load('wall_vines0.png')
text3 = pygame.image.load('key1.png')
text_p = pygame.image.load('player1.png')
text_d_h = pygame.image.load('door1hor.png')
text_d_h1 = pygame.image.load('door2hor.png')
text_d_v = pygame.image.load('door1vert.png')
text_d_v1 = pygame.image.load('door2vert.png')
pygame.init()

clock = pygame.time.Clock()
enemy_timer = 0

sc = pygame.display.set_mode((WIN_WIDTH + INT_WIDTH, WIN_HEIGHT))

width = 32
height = 32
x = 0
y = 0
x_hero = width
y_hero = height
my_map = map_gen(width, height, WIN_WIDTH, WIN_HEIGHT)
my_map = normal_map(my_map)
tmp_surf = pygame.Surface((INT_WIDTH, 30))
tmp_surf.fill(BLACK)

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 25)
speed_x = width / 2
speed_y = height / 2
key_count = 0
while True:
    if (enemy_timer == 100):
        enemy_timer = 0
    text_surface = my_font.render('Кол-во ключей: ' + str(key_count), False, (RED, 0, 0))

    draw_map(x, y, my_map, RED, GREEN, BLUE)
    sc.blit(tmp_surf, (WIN_WIDTH + 10, 0))
    sc.blit(tmp_surf, (WIN_WIDTH + 10, WIN_HEIGHT - 100))
    sc.blit(text_p, (x_hero, y_hero))
    sc.blit(text_surface, (WIN_WIDTH + 10, 0))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_a:
                x_hero -= speed_x
                if (my_map[int(y_hero / height)][int(x_hero / width)] == 1) | (
                        my_map[int(y_hero / height)][int(x_hero / width)] == 3):
                    x_hero += speed_x
            elif i.key == pygame.K_d:
                x_hero += speed_x
                if (my_map[int(y_hero / height)][int(x_hero / width)] == 1) | (
                        my_map[int(y_hero / height)][int(x_hero / width)] == 3):
                    x_hero -= speed_x
            elif i.key == pygame.K_s:
                y_hero += speed_y
                if (my_map[int(y_hero / height)][int(x_hero / width)] == 1) | (
                        my_map[int(y_hero / height)][int(x_hero / width)] == 3):
                    y_hero -= speed_y
            elif i.key == pygame.K_w:
                y_hero -= speed_y
                if (my_map[int(y_hero / height)][int(x_hero / width)] == 1) | (
                        my_map[int(y_hero / height)][int(x_hero / width)] == 3):
                    y_hero += speed_y
            elif i.key == pygame.K_1:
                pygame.image.save(sc, os.path.join('img1.jpeg'))
    ind_i = y_hero / height
    ind_j = x_hero / width
    obj = my_map[int(ind_i)][int(ind_j)]
    if (obj == 2):
        if (key_count < 8):
            my_map[int(ind_i)][int(ind_j)] = 0
            sc.blit(text3, (WIN_WIDTH + key_count * width, 64))
            key_count += 1
        else:
            text2_surf = my_font.render('У меня нет места!', False, (RED, 0, 0))
            sc.blit(text2_surf, (WIN_WIDTH + 10, WIN_HEIGHT - 100))
    elif (obj == 6) & (key_count != 0):
        sf = pygame.Surface((16, 16))
        sf.fill(BLACK)
        sc.blit(sf, (WIN_WIDTH + (key_count - 1) * width, 64))
        key_count -= 1
        my_map[int(ind_i)][int(ind_j)] = 12
    elif (obj == 6) & (key_count == 0):
        y_hero -= speed_y
    enemy_timer += 1
    pygame.display.update()
    clock.tick(FPS)
