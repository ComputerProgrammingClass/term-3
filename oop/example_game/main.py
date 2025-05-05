import pygame, sys, random
from settings import *
from player import Player
from enemy import ShootingEnemy, ChargerEnemy
from bullet import Bullet

# Init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Enemies")
clock = pygame.time.Clock()

# Game objects
player = Player(WIDTH // 2, HEIGHT - 60)
enemies = [
    ShootingEnemy(random.randint(0, WIDTH - 40), random.randint(-500, -40))
    for _ in range(5)
]
chargers = [
    # ChargerEnemy(random.randint(0, WIDTH - 40), random.randint(-500, -40))
    ChargerEnemy(random.randint(0, WIDTH - 40), random.randint(1, 40))
    for _ in range(3)
]
bullets = []
keys = pygame.key.get_pressed()
running = True


def handle_input():
    # Input
    global keys
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global running
            running = False


def update():
    # Update
    player.move(keys)
    for enemy in enemies:
        enemy.update(bullets, player.rect.center)
        enemy.draw(screen)

    for charger in chargers:
        charger.update(player.rect.center)
        charger.draw(screen)

    for bullet in bullets[:]:
        bullet.move()
        if bullet.off_screen():
            bullets.remove(bullet)


def handle_collisions():
    for bullet in bullets:
        if bullet.rect.colliderect(player.rect):
            game_over()

    for enemy in enemies:
        if enemy.rect.colliderect(player.rect):
            game_over()

    for enemy in chargers:
        if enemy.rect.colliderect(player.rect):
            game_over()


def render():
    player.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)

    pygame.display.flip()


def game_over():
    print("Hit! Game Over")
    pygame.quit()
    sys.exit()


def main():
    # Game loop
    while running:
        clock.tick(FPS)
        screen.fill(WHITE)

        handle_input()
        update()
        handle_collisions()
        render()

    pygame.quit()


if __name__ == "__main__":
    main()
