import pygame, random
from card import Card

class Deck():
    # deck = random.sample(Card.image_sprite(), 6)
    # deck_positions = [(50, 320), (200, 320), (350, 320)]
    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 10, 5)



    # # Перетасовка колоды
    # random.shuffle(Card.image_sprite.card_sprite)

    # # Создание руки игрока
    # player_hand = []

    # # Раздача карт игроку
    # for _ in range(6):
    #     player_hand.append(Card.image_sprite.card_sprite.pop())