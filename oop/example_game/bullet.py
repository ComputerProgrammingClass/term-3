import pygame
import math
from settings import BLACK, WIDTH, HEIGHT


class Bullet:
    def __init__(self, x, y, target_pos):
        self.rect = pygame.Rect(x, y, 6, 6)
        angle = math.atan2(target_pos[1] - y, target_pos[0] - x)
        self.speed_x = math.cos(angle) * 5
        self.speed_y = math.sin(angle) * 5

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def draw(self, surface):
        pygame.draw.rect(surface, BLACK, self.rect)

    def off_screen(self):
        return not (0 <= self.rect.x <= WIDTH and 0 <= self.rect.y <= HEIGHT)
