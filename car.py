import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Racing Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define car properties
car_width, car_height = 70, 140
car_img = pygame.image.load("car.png")  # Replace "car.png" with your car image file

# Define road properties
road_width = 400
road_x = (screen_width - road_width) // 2
road_y = 0
road_color = WHITE

# Define clock to control the game's frame rate
clock = pygame.time.Clock()

# Game loop
def game_loop():
    # Initialize car position
    car_x = (screen_width - car_width) // 2
    car_y = screen_height - car_height - 20

    # Initialize obstacle position and size
    obstacle_width, obstacle_height = 70, 140
    obstacle_x = random.randint(road_x, road_x + road_width - obstacle_width)
    obstacle_y = -obstacle_height
    obstacle_speed = 5

    # Game state variables
    crashed = False

    while not crashed:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Move the car based on user input
        keys = pygame.key.get_pressed()
        car_speed = 5
        if keys[pygame.K_LEFT] and car_x > road_x:
            car_x -= car_speed
        if keys[pygame.K_RIGHT] and car_x < road_x + road_width - car_width:
            car_x += car_speed

        # Update obstacle position
        obstacle_y += obstacle_speed

        # Check for collision
        if car_y < obstacle_y + obstacle_height:
            if (
                car_x + car_width > obstacle_x
                and car_x < obstacle_x + obstacle_width
            ):
                crashed = True

        # Clear the screen
        screen.fill(BLACK)

        # Draw road
        pygame.draw.rect(screen, road_color, (road_x, road_y, road_width, screen_height))

        # Draw car
        screen.blit(car_img, (car_x, car_y))

        # Draw obstacle
        pygame.draw.rect(
            screen, RED, (obstacle_x, obstacle_y, obstacle_width, obstacle_height)
        )

        # Update the display
        pygame.display.update()

        # Set the frame rate
        clock.tick(60)

# Start the game
game_loop()
