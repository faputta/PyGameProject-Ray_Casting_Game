import pygame
import player
from settings import *
from map import game_map
from math import sin, cos


def converting(first, second):
    return first // TILE * TILE, second // TILE * TILE


def ray_casting(screen, player_pos, player_angle, textures):
    texture_v, texture_h = 1, 1
    x_p, y_p = player_pos
    pos_in_block = {'left': x_p - x_p // TILE * TILE,
                    'top': y_p - y_p // TILE * TILE,
                    'right': TILE - (x_p - x_p // TILE * TILE),
                    'bottom': TILE - (y_p - y_p // TILE * TILE)}

    for ray in range(NUMBER_OF_RAYS):
        cur_angle = player_angle - HALF_FIELD_OF_VIEW + ANGLE_BETWEEN_RAYS * ray
        cos_ray, sin_ray = cos(cur_angle), sin(cur_angle)
        vd, hd = float('inf'), float('inf')

        # Верикальные прямые
        for i in range(MAX_DISTANCE):
            if cos_ray > 0:
                vd = pos_in_block['right'] / cos_ray + TILE / cos_ray * i + 1
            elif cos_ray < 0:
                vd = pos_in_block['left'] / -cos_ray + TILE / -cos_ray * i + 1

            x_v, y_v = vd * cos_ray + x_p, vd * sin_ray + y_p
            tile_v = converting(x_v, y_v)
            if tile_v in game_map:
                texture_v = game_map[tile_v]
                break

        # Горизонтальные прямые
        for i in range(MAX_DISTANCE):
            if sin_ray > 0:
                hd = pos_in_block['bottom'] / sin_ray + TILE / sin_ray * i + 1
            elif sin_ray < 0:
                hd = pos_in_block['top'] / -sin_ray + TILE / -sin_ray * i + 1

            x_h, y_h = hd * cos_ray + x_p, hd * sin_ray + y_p
            tile_h = converting(x_h, y_h)
            if tile_h in game_map:
                texture_h = game_map[tile_h]
                break

        if hd > vd:
            ray_length = vd
            offset = y_v % TILE
            texture = texture_v
        else:
            ray_length = hd
            offset = x_h % TILE
            texture = texture_h

        ray_length += cos(player_angle - cur_angle)
        display_height = DISPLAY_COEF / (ray_length + 0.00001)

        textures[texture].set_alpha(int(display_height * 255))
        wall_column = textures[texture].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_WIDTH)
        wall_column = pygame.transform.scale(wall_column, (SCALE, int(display_height))).convert_alpha()
        screen.blit(wall_column, (ray * SCALE, HALF_HEIGHT - display_height // 2))

        # ray_length += cos(player_angle - cur_angle)
        # display_height = DISPLAY_COEF / (ray_length + 0.00001)
        # c = 255 / (1 + ray_length ** 2 * 0.0002)
        # colour = (c // 3, c // 2, c)
        # pygame.draw.rect(screen, colour, (ray * SCALE, HALF_HEIGHT - display_height // 2, SCALE, display_height))

        # ray_length *= cos(player_angle - cur_angle)
        # to_x = ray_length * cos(cur_angle) + x_p
        # to_y = ray_length * sin(cur_angle) + y_p
        # pygame.draw.line(screen, 'green', (x_p, y_p), (to_x, to_y))
