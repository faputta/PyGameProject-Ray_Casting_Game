import pygame
from settings import *


class Sprites:
    def __init__(self):
        self.types_of_sprites = {
            'wall': pygame.image.load('data/textures/wall2.png').convert_alpha()
        }
        self.sprite_objects = [
            Object(self.types_of_sprites['wall'], True, (6.3, 2.4), 1.8, 0.4)
        ]


class Object:
    def __init__(self, obj, isstatic, pos, trans, scale):
        self.object = object
        self.isstatic = True
        self.pos = self.x, self.y = pos[0] * TILE, pos[1] * TILE
        self.trans = trans
        self.scale = scale

    def sprite_location(self, player, walls):
        pass