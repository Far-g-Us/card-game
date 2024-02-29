import pygame, sys


def events(screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # if event.type == pygame.MOUSEBUTTONDOWN:


        # elif event.type == pygame.KEYDOWN:
        # elif event.type == pygame.KEYUP:

def update(bg_color, screen):
    screen.fill(bg_color)


    pygame.display.flip()