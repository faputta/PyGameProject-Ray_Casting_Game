from settings import *
import pygame
from math import sin, cos


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self):
        return self.x, self.y

    def movements(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            self.x += player_speed * cos(self.angle)
            self.y += player_speed * sin(self.angle)

        if key[pygame.K_s]:
            self.x += -player_speed * cos(self.angle)
            self.y += -player_speed * sin(self.angle)

        if key[pygame.K_a]:
            self.x += player_speed * sin(self.angle)
            self.y += -player_speed * cos(self.angle)

        if key[pygame.K_d]:
            self.x += -player_speed * sin(self.angle)
            self.y += player_speed * cos(self.angle)

        if key[pygame.K_LEFT]:
            self.angle -= 0.03

        if key[pygame.K_RIGHT]:
            self.angle += 0.02
