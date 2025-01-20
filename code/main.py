import pygame
from os.path import join
from random import randint

# General Setup
pygame.init() # Initialize the game
WINDOW_WITH,WINDOW_HEIGHT = 1280, 720
display_surface =  pygame.display.set_mode((WINDOW_WITH,WINDOW_HEIGHT))
pygame.display.set_caption('Space shooter')
running = True
clock = pygame.time.Clock()

# Plain surface
surf = pygame.Surface((100,200))
surf.fill('orange')
x = 100

# Importing images
player_surface = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_surface.get_frect(center = (WINDOW_WITH / 2, WINDOW_HEIGHT / 2))
player_direction = pygame.math.Vector2(1, 1 )
player_speed = 300 

star_surface = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_position = [(randint(0, WINDOW_WITH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

meteor_surface = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surface.get_frect(center = (WINDOW_WITH /2, WINDOW_HEIGHT / 2))

laser_surface = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surface.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20))

while running:
    dt = clock.tick() / 1000 # miliseconds to seconds conversion
 
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

    # Showing element on screen
    display_surface.blit(meteor_surface, meteor_rect)
    display_surface.blit(laser_surface, laser_rect)
    
    # Player movement
    if player_rect.bottom >= WINDOW_HEIGHT or player_rect.top <= 0:
        player_direction.y *= -1
    if player_rect.right >= WINDOW_WITH or player_rect.left <= 0:
        player_direction.x *= -1

    player_rect.center += player_direction * player_speed * dt
    display_surface.blit(player_surface, player_rect)
    
    pygame.display.update() # update() entire window when flip update a part of a window 
    
pygame.quit() # <> init so we shutdown the game properly

