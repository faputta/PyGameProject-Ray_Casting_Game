from settings import *
import pygame
from math import sin, cos


walls_group = pygame.sprite.Group()

class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.side = 50
        self.rect = pygame.Rect(self.x, self.y, self.side, self.side)

    @property
    def pos(self):
        return self.x, self.y

    def collision(self, px, py):
        new_rect = self.rect.copy()
        new_rect.move_ip(px, py)
        collided_objects = new_rect.collidelistall()
        pass

    def movements(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            px = player_speed * cos(self.angle)
            py = player_speed * sin(self.angle)

        if key[pygame.K_s]:
            px = -player_speed * cos(self.angle)
            py = -player_speed * sin(self.angle)

        if key[pygame.K_a]:
            px = player_speed * sin(self.angle)
            py = -player_speed * cos(self.angle)

        if key[pygame.K_d]:
            px = -player_speed * sin(self.angle)
            py = player_speed * cos(self.angle)

        if key[pygame.K_LEFT]:
            self.angle -= 0.03

        if key[pygame.K_RIGHT]:
            self.angle += 0.02

        self.angle %= DOUBLE_PI

    def mouse(self):
        pygame.mouse.set_visible(False)
        if pygame.mouse.get_focused():
            self.angle = (pygame.mouse.get_pos()[0] - HALF_WIDTH) * MOUSE_SENSIVITY
            self.angle %= DOUBLE_PI


