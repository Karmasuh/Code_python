
import pygame

# Initialize pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Collision Example")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create some rectangles (representing objects)
rect1 = pygame.Rect(100, 100, 50, 50)
rect2 = pygame.Rect(300, 100, 50, 50)

# Game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move the second rectangle using arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect2.x -= 5
    if keys[pygame.K_RIGHT]:
        rect2.x += 5
    if keys[pygame.K_UP]:
        rect2.y -= 5
    if keys[pygame.K_DOWN]:
        rect2.y += 5
    
    # Collision detection
    if rect1.colliderect(rect2):
        pygame.draw.rect(screen, RED, rect1)  # Change to red if colliding
        pygame.draw.rect(screen, RED, rect2)
    else:
        pygame.draw.rect(screen, BLUE, rect1)  # Normal color if no collision
        pygame.draw.rect(screen, BLUE, rect2)
    
    # Update display
    pygame.display.update()

pygame.quit()
