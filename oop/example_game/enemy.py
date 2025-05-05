import pygame
import random
import math

# import random
from settings import RED, ORANGE
from bullet import Bullet


class Enemy:
    def __init__(self, x, y, size=40):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = RED

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def update(self, *args, **kwargs):
        raise NotImplementedError("update() must be defined in subclasses.")


class ShootingEnemy(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = 2
        self.shoot_cooldown = 90
        self.timer = 0
        self.color = RED

    def move_towards_player(self, player_pos):
        dx = player_pos[0] - self.rect.centerx + random.randint(-200, 200)
        dy = player_pos[1] - self.rect.centery + random.randint(-200, 200)
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx /= dist
            dy /= dist
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed

    def update(self, bullets, player_pos):
        self.move_towards_player(player_pos)
        self.timer += 1
        if self.timer >= self.shoot_cooldown:
            self.timer = 0
            bullets.append(Bullet(self.rect.centerx, self.rect.centery, player_pos))


class ChargerEnemy(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.phase = "idle"
        self.idle_timer = 60
        self.charge_speed = 8
        self.vel_x = 0
        self.vel_y = 0
        self.color = ORANGE  # Add ORANGE = (255, 100, 0) to settings.py

    def update(self, player_pos):
        if self.phase == "idle":
            self.idle_timer -= 1
            if self.idle_timer <= 0:
                self.phase = "charging"
                dx = player_pos[0] - self.rect.centerx
                dy = player_pos[1] - self.rect.centery
                dist = math.hypot(dx, dy)
                if dist != 0:
                    self.vel_x = (dx / dist) * self.charge_speed
                    self.vel_y = (dy / dist) * self.charge_speed
        elif self.phase == "charging":
            self.rect.x += self.vel_x
            self.rect.y += self.vel_y
            if not (0 <= self.rect.x <= 800 and 0 <= self.rect.y <= 600):
                self.phase = "idle"
