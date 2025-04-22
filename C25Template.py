import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balloon Buster Game")

# Set up clock and frame rate
clock = pygame.time.Clock()
FPS = 60

# Game loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Optional: fill screen with white
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
