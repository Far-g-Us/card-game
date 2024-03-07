import pygame, controls
from card import Card

def run():

    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Дурак")
    bg_color = (0, 128, 0)

    while True:
        controls.events(screen)
        screen.fill(bg_color)
        pygame.display.update()
        # pygame.display.flip()

        clock.tick(60)
run()
