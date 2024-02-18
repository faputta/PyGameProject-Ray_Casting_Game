from settings import *
import pygame
from math import sin, cos
from map import collision_walls


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.mouse_angle = 0
        self.side = 50
        self.rect = pygame.Rect(self.x, self.y, self.side, self.side)

    @property
    def pos(self):
        return self.x, self.y

    def collision(self, px, py):
        new_rect = self.rect.copy()
        new_rect.move_ip(px, py)
        collided_objects = new_rect.collidelistall(collision_walls)

        if len(collided_objects):
            dx, dy = 0, 0
            for obj in collided_objects:
                hit_rect = collision_walls[obj]
                if px > 0:
                    dx += new_rect.right - hit_rect.left
                else:
                    dx += hit_rect.right - new_rect.left
                if dy > 0:
                    dy += new_rect.bottom - hit_rect.top
                else:
                    dy += hit_rect.bottom - new_rect.top

            if abs(dx - dy) < 10:
                px, py = 0, 0
            elif dx > dy:
                py = 0
            elif dy > dx:
                px = 0
        self.x += px
        self.y += py

    def movements(self):
        self.keys()
        self.mouse()
        self.angle %= DOUBLE_PI
        self.rect.center = self.x, self.y

    def keys(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            px = player_speed * cos(self.angle)
            py = player_speed * sin(self.angle)
            self.collision(px, py)

        if key[pygame.K_s]:
            px = -player_speed * cos(self.angle)
            py = -player_speed * sin(self.angle)
            self.collision(px, py)

        if key[pygame.K_a]:
            px = player_speed * sin(self.angle)
            py = -player_speed * cos(self.angle)
            self.collision(px, py)

        if key[pygame.K_d]:
            px = -player_speed * sin(self.angle)
            py = player_speed * cos(self.angle)
            self.collision(px, py)

        if key[pygame.K_LEFT]:
            self.angle -= 0.02

        if key[pygame.K_RIGHT]:
            self.angle += 0.02

    def mouse(self):
        pygame.mouse.set_visible(False)
        if pygame.mouse.get_focused():
            diff = pygame.mouse.get_pos()[0] - HALF_WIDTH
            pygame.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))
            self.angle += diff * MOUSE_SENSITIVITY

