import math

import pygame
from settings import *
from collections import deque


class Sprites:
    def __init__(self):
        self.sprites_parameters = {
            'purple_planet': {
                'sprite': pygame.image.load('data/decorating sprites/11 planets/methane-barren.png').convert_alpha(),
                'angles_of_view': None,
                'shift': 0.8,
                'scale': 1.2,
                'animation': False,
                'start_animation_dist': 800,
                'animation_speed': 10
            },

            'red_planet': {
                'sprite': pygame.image.load('data/decorating sprites/11 planets/desert.png').convert_alpha(),
                'angles_of_view': None,
                'shift': 0.8,
                'scale': 0.7,
                'animation': False,
                'start_animation_dist': 800,
                'animation_speed': 10
            },

            'grey_planet': {
                'sprite': pygame.image.load('data/decorating sprites/11 planets/barren-charred.png').convert_alpha(),
                'angles_of_view': None,
                'shift': 0.8,
                'scale': 0.9,
                'animation': False,
                'start_animation_dist': 800,
                'animation_speed': 10
            },
            'red_dragon': {
                'sprite': pygame.image.load(f'data/red dragon/tile0.png').convert_alpha(),
                'angles_of_view': None,
                'shift': 0.8,
                'scale': 0.7,
                'animation': deque(
                    [pygame.image.load(f'data/red dragon/tile{i}.png').convert_alpha() for i in range(2)]
                ),
                'start_animation_dist': 800,
                'animation_speed': 10
            },
            'grey_dragon': {
                'sprite': pygame.image.load(f'data/grey dragon/tile0.png').convert_alpha(),
                'angles_of_view': None,
                'shift': 0.6,
                'scale': 0.9,
                'animation': deque(
                    [pygame.image.load(f'data/grey dragon/tile{i}.png').convert_alpha() for i in range(3)]
                ),
                'start_animation_dist': 800,
                'animation_speed': 10
            }
        }

        self.sprite_objects = [
            Object(self.sprites_parameters['purple_planet'], (5.4, 2.0)),
            Object(self.sprites_parameters['red_planet'], (9.7, 7.4)),
            Object(self.sprites_parameters['grey_planet'], (13.7, 7.4)),
            Object(self.sprites_parameters['red_dragon'], (7.7, 7.4)),
            Object(self.sprites_parameters['grey_dragon'], (10.7, 5.4))
        ]


class Object:
    def __init__(self, parameters, pos):
        self.obj = parameters['sprite']
        self.angles_of_view = parameters['angles_of_view']
        self.shift = parameters['shift']
        self.scale = parameters['scale']
        self.animation = parameters['animation']
        self.start_animation_dist = parameters['start_animation_dist']
        self.animation_speed = parameters['animation_speed']
        self.count_of_frames = 0
        self.pos = self.x, self.y = pos[0] * TILE, pos[1] * TILE
        if self.angles_of_view:
            self.sprite_angles = [frozenset(range(i, i + 45)) for i in range(0, 360, 45)]
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angles, self.obj)}

    def sprite_location(self, player, walls):
        dx, dy = self.x - player.x, self.y - player.y
        dist_to_sprite = math.sqrt(dx ** 2 + dy ** 2)
        temp_angle = math.atan2(dy, dx)
        angle_between_centre_and_sprite = temp_angle - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            angle_between_centre_and_sprite += DOUBLE_PI

        delta_rays = int(angle_between_centre_and_sprite / ANGLE_BETWEEN_RAYS)
        current_ray = MAIN_RAY + delta_rays
        dist_to_sprite *= math.cos(HALF_FIELD_OF_VIEW - current_ray * ANGLE_BETWEEN_RAYS)

        if 0 <= current_ray < NUMBER_OF_RAYS - 1 and dist_to_sprite < walls[current_ray][0]:
            display_height = int(DISPLAY_COEF / dist_to_sprite * self.scale)
            half_display_height = display_height // 2
            shift = half_display_height // 2 * self.shift

            sprite_obj = self.obj
            if self.animation and dist_to_sprite < self.start_animation_dist:
                sprite_obj = self.animation[0]
                if self.count_of_frames < self.animation_speed:
                    self.count_of_frames += 1
                else:
                    self.animation.rotate()
                    self.count_of_frames = 0

            sprite_pos = (current_ray * SCALE - half_display_height, HALF_HEIGHT - half_display_height + shift)
            sprite = pygame.transform.scale(sprite_obj, (display_height, display_height))
            return (dist_to_sprite, sprite, sprite_pos)
        return (False,)
