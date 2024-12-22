import pygame

# General Setup
pygame.init() # Initialize the game
WINDOW_WITH,WINDOW_HEIGHT = 1280, 720
display_surface =  pygame.display.set_mode((WINDOW_WITH,WINDOW_HEIGHT))
pygame.display.set_caption('Space shooter')
running = True

# Plain Surface
surf = pygame.Surface((100, 200)) 
surf.fill('orange')
x = 100 

# Importing an image
player_surface = pygame.image.load('images/player.png')

while running:
    # create loop : inside for keyboard input, mouse input, timers, UI interaction...
    for event in pygame.event.get():
        # Quit the game
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    display_surface.fill('darkgrey')
    x += 0.1
    display_surface.blit(player_surface, (x, 150)) # blit link 2 surfaces : surface, target position begin to top left
    pygame.display.update() # update() entire window when flip update a part of a window 

pygame.quit() # <> init so we shutdown the game properly

