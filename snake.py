import pygame
import sys

pygame.init()


width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
snake_speed = 6

def game_loop():
    running = True
    while running:
        screen.fill((50, 153, 213))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        pygame.display.update()
        clock.tick(snake_speed)
    
    pygame.quit()
    sys.exit()

game_loop()

