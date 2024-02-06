from settings import *

map_constructor = [
    '1111111111111111',
    '1001000000000001',
    '1001100000001101',
    '1000000000000001',
    '1110000000000001',
    '1000111100010001',
    '1010100100110001',
    '1000100000000001',
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

