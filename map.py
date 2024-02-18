from settings import *
import pygame

map_constructor = [
    [1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 2],
    [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

MAP_WIDTH = len(map_constructor[0]) * TILE
MAP_HEIGHT = len(map_constructor) * TILE
game_map = dict()
mini_map = set()
collision_walls = []
for y, row in enumerate(map_constructor):
    for x, obj in enumerate(row):
        if obj:
            mini_map.add((x * MINI_MAP_TILE, y * MINI_MAP_TILE))
            collision_walls.append(pygame.Rect(x * TILE, y * TILE, TILE, TILE))
        if obj == 1:
            game_map[(x * TILE, y * TILE)] = 1
        if obj == 2:
            game_map[(x * TILE, y * TILE)] = 2