import pygame
from os.path import join
from random import randint

# General Setup
pygame.init() # Initialize the game
WINDOW_WITH,WINDOW_HEIGHT = 1280, 720
display_surface =  pygame.display.set_mode((WINDOW_WITH,WINDOW_HEIGHT))
pygame.display.set_caption('Space shooter')
running = True

# Plain Surface
x = 100 

# Importing images
player_surface = pygame.image.load(join('images', 'player.png')).convert_alpha()
star_surface = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_position = [(randint(0, WINDOW_WITH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

while running:
    # create loop : inside for keyboard input, mouse input, timers, UI interaction...
    for event in pygame.event.get():
        # Quit the game
        if event.type == pygame.QUIT:
            running = False

    # draw the game in order 
    # Wallpaper
    display_surface.fill('darkgrey')
    # Stars 
    for pos in star_position:
        display_surface.blit(star_surface, pos)
    x += 0.1
    # Ship 
    display_surface.blit(player_surface, (x, 150)) # blit link 2 surfaces : surface, target position begin to top left
    
    pygame.display.update() # update() entire window when flip update a part of a window 

    
pygame.quit() # <> init so we shutdown the game properly

