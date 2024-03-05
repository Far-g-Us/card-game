import pygame, controls


def run():

    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Дурак")
    bg_color = (255, 255, 255)

    while True:
        # controls.events(screen)
        controls.update(screen)
        # screen.fill(bg_color)
        # pygame.display.flip()
run()
