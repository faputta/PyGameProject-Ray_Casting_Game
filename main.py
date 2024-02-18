import os
import sys
import pygame

import sprite
from settings import *
from player import Player
from map import *
from ray_casting import ray_casting
from drawing import Drawing
from sprite import *

pygame.init()


def main():
    screen = pygame.display.set_mode(SIZE)
    mini_map_screen = pygame.Surface((MINI_MAP_WIDTH, MINI_MAP_HEIGHT))
    clock = pygame.time.Clock()
    player = Player()
    drawing = Drawing(screen, mini_map_screen)
    sprites = Sprites()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False

        player.movements()
        screen.fill((0, 0, 0))
        drawing.background(player.angle)
        walls = ray_casting(player, drawing.textures)
        drawing.world_drawing(walls + [object.sprite_location(player, walls) for object in sprites.sprite_objects])

        drawing.mini_map(player)

        pygame.display.flip()
        clock.tick(FPS)

    terminate()


if __name__ == '__main__':
    main()
