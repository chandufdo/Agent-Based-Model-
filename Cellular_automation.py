# Group members

# S 14860 - Roshimali Shashiprabha
# S 14969 - Hiruni Kavindya
# S 14972 - Chandula Fernando
# S 15002 - Piyumi Perera


import random
from random import randint
import pygame
from copy import deepcopy

RES = WIDTH, HEIGHT = 600, 600
TILE = 20
W, H = WIDTH // TILE, HEIGHT // TILE
FPS = 10

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

nf = [[0 for i in range(W)] for j in range(H)]
cf = [[randint(0, 1) for i in range(W)] for j in range(H)]


def check_cell(cf, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if cf[j][i]:
                count = count + 1

    if cf[y][x]:
        count = count - 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0


while True:
    surface.fill(pygame.Color('white'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Drawing the grid
    [pygame.draw.line(surface, pygame.Color('black'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
    [pygame.draw.line(surface, pygame.Color('black'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]

    # drawing live cells
    for x in range(1, W - 1):
        for y in range(1, H - 1):
            if cf[y][x]:
                pygame.draw.rect(surface, pygame.Color('blue'), (x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2))
            nf[y][x] = check_cell(cf, x, y)

    cf = deepcopy(nf)

    pygame.display.flip()
    clock.tick(FPS)


