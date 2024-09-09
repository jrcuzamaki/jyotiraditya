import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shooting Game")

# Player attributes
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# Bullet attributes
bullet_width = 10
bullet_height = 40
bullet_x = 0
bullet_y = player_y
bullet_speed = 10
bullet_state = "ready"

# Enemy attributes
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, screen_width - enemy_width)
enemy_y = random.randint(50, 150)
enemy_speed = 3

# Game loop
running = True
clock = pygame.time.Clock()

def fire_bullet():
    global bullet_state, bullet_x, bullet_y
    bullet_state = "fire"
    bullet_x = player_x + player_width // 2 - bullet_width // 2
    bullet_y = player_y

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    if (
        bullet_x < enemy_x + enemy_width
        and bullet_x + bullet_width > enemy_x
        and bullet_y < enemy_y + enemy_height
        and bullet_y + bullet_height > enemy_y
    ):
        return True
    return False

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Shoot when spacebar is pressed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if bullet_state == "ready":
                fire_bullet()

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # Move the bullet
    if bullet_state == "fire":
        bullet_y -= bullet_speed
        if bullet_y <= 0:
            bullet_state = "ready"

    # Move the enemy
    enemy_x += enemy_speed
    if enemy_x <= 0 or enemy_x >= screen_width - enemy_width:
        enemy_speed *= -1
        enemy_y += enemy_height

    # Check for collision
    if is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
        enemy_x = random.randint(0, screen_width - enemy_width)
        enemy_y = random.randint(50, 150)
        bullet_state = "ready"

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the player
    pygame.draw.rect(screen, (255, 255, 255), (player_x, player_y, player_width, player_height))

    # Draw the bullet
    if bullet_state == "fire":
        pygame.draw.rect(screen, (255, 0, 0), (bullet_x, bullet_y, bullet_width, bullet_height))

    # Draw the enemy
    pygame.draw.rect(screen, (0, 255, 0), (enemy_x, enemy_y, enemy_width, enemy_height))

    # Update the display
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

# Quit the game
pygame.quit()
