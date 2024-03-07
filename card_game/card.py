import pygame
from pygame.sprite import Sprite

class Card(Sprite):
    def __init__(self, screen, image_sprite):
        super(Card, self).__init__()
        self.screen = screen
        self.image = image_sprite
        self.rect = self.image.get_rect()


    def image_sprite(self):
        card_sprite = []
        for suit in ["hearts", "diamonds", "clubs", "spades"]:
            for value in range(6, 11):
                image = pygame.image.load(f"img/cards/{suit}_{value}.png")
                card_sprite.append(image)

        for suit in ["hearts", "diamonds", "clubs", "spades"]:
            for value in ["jack", "queen", "king", "ace"]:
                image = pygame.image.load(f"img/cards/{suit}_{value}.png")
                card_sprite.append(image)
