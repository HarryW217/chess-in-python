import pygame
import os

# LeagueSpartan-Bold font file path
script_dir = os.path.dirname(__file__)
font_path = os.path.join(script_dir, 'assets','LeagueSpartan-Bold.otf')

pygame.init()
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
font = pygame.font.Font(font_path, 20)
big_font = pygame.font.Font(font_path, 50)
timer = pygame.time.Clock()
fps = 60

# RGB values for dark brown

dark_brown = (101, 67, 33)


# Main Game Loop
run = True
while run:
    timer.tick(fps)
    screen.fill(dark_brown)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.flip()
pygame.quit()