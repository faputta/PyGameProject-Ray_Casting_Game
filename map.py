from settings import *

map_constructor = [
    '1111111111111111',
    '1000000000000001',
    '1001100000001101',
    '1000000000000001',
    '1001100001000111',
    '1000000000000011',
    '1010000111000011',
    '1000110000000001',
    '1111111111111111'
]

game_map = dict()
mini_map = set()
for y, row in enumerate(map_constructor):
    for x, obj in enumerate(row):
        if obj != '0':
            mini_map.add((x * MINI_MAP_TILE, y * MINI_MAP_TILE))
        if obj == '1':
            game_map[(x * TILE, y * TILE)] = 1

