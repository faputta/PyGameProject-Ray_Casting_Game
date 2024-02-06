import sys
import pygame
from math import pi, tan

SIZE = WIDTH, HEIGHT = 1600, 900

HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
TILE = 100

FPS = 60

player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 3

FIELD_OF_VIEW = pi / 3
HALF_FIELD_OF_VIEW = FIELD_OF_VIEW / 2
NUMBER_OF_RAYS = 400
MAX_DISTANCE = WIDTH // TILE
ANGLE_BETWEEN_RAYS = FIELD_OF_VIEW / NUMBER_OF_RAYS
DISTANCE = NUMBER_OF_RAYS / (2 * tan(HALF_FIELD_OF_VIEW))
DISPLAY_COEF = 4 * DISTANCE * TILE
SCALE = WIDTH // NUMBER_OF_RAYS

MINI_MAP_SCALE = 5
MINI_MAP_TILE = TILE // MINI_MAP_SCALE
MINI_MAP_WIDTH = WIDTH // MINI_MAP_SCALE
MINI_MAP_HEIGHT = HEIGHT // MINI_MAP_SCALE

TEXTURE_WIDTH = 1600
TEXTURE_HEIGHT = 1600
TEXTURE_SCALE = TEXTURE_WIDTH // TILE


def terminate():
    pygame.quit()
    sys.exit()