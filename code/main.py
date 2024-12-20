import pygame

# General Setup
pygame.init()
WINDOW_WITH,WINDOW_HEIGHT = 1280, 720
display_surface =  pygame.display.set_mode((WINDOW_WITH,WINDOW_HEIGHT))
running = True
 

while running:
    # create loop : inside for keyboard input, mouse input, timers, UI interaction...
    for event in pygame.event.get():
        # 
        if event.type == pygame.QUIT:
            running = False


    # draw the game