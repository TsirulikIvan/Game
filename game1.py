import pygame


def first_anim(col):
    pygame.draw.rect(sc, col, (x, y,width,height))
    pygame.draw.rect(sc, col, ((WIN_WIDTH - width) - x,(WIN_HEIGHT - height) - y,width,height))
    pygame.draw.rect(sc, col, (x, (WIN_HEIGHT - height) - y,width,height))
    pygame.draw.rect(sc, col, ((WIN_WIDTH - width) - x, y,width,height))
def lvl():
    pygame.draw.rect(sc, WHITE, (width, height ,WIN_WIDTH - 2*width,WIN_HEIGHT - 2*height))
    pygame.draw.rect(sc, BLACK, (WIN_WIDTH / 4,  WIN_HEIGHT // 2 - height,WIN_WIDTH /2, height))


FPS = 20
WIN_WIDTH = 480
WIN_HEIGHT = 490

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
width =  4
height = 4
x = 0  # скрываем за левой границей
y = 0  # выравнивание по центру по вертикали
startpoint = [WIN_WIDTH - 2*width,WIN_HEIGHT - 2*height]
print(startpoint)
while 1:

    lvl()
    for i in pygame.event.get():
        if i.type == pygame.QUIT: exit()

    fisrt_anim(CUSTOM_COL)
    pygame.display.update()



    clock.tick(FPS)
