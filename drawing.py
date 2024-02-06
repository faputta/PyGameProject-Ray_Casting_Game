import pygame
import os
from settings import *
from ray_casting import ray_casting
from math import sin, cos
from map import game_map, mini_map


class Drawing:
    def __init__(self, screen, mini_map_screen):
        self.screen = screen
        self.mini_map_screen = mini_map_screen
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.textures = {1: Drawing.load_image(self, 'wall.png'),
                         's': Drawing.load_image(self, 'sky.png')}

    def background(self):
        pygame.draw.rect(self.screen, (80, 0, 30), (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(self.screen, (80, 80, 80), (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def environment(self, player_pos, player_angle):
        ray_casting(self.screen, player_pos, player_angle, self.textures)

    def mini_map(self, player):
        self.mini_map_screen.fill((0, 0, 0))
        x_m, y_m = player.x // MINI_MAP_SCALE, player.y // MINI_MAP_SCALE
        pygame.draw.circle(self.mini_map_screen, 'red', (int(x_m), int(y_m)), 5)
        pygame.draw.line(self.mini_map_screen, 'blue', (x_m, y_m),
                         (x_m + WIDTH * cos(player.angle), y_m + WIDTH * sin(player.angle)), 2)

        for x, y in mini_map:
            pygame.draw.rect(self.mini_map_screen, 'green', (x, y, MINI_MAP_TILE, MINI_MAP_TILE))

        self.screen.blit(self.mini_map_screen, (116, 624))

    def load_image(self, name, colorkey=None):
        fullname = os.path.join('data', name)
        if not os.path.isfile(fullname):
            print(f'Файл сизображением "{fullname}" не найден')
            sys.exit()
        image = pygame.image.load(fullname).convert_alpha()
        return image
