import pygame
import random
from collections import deque

# Загружаем изображения карт с цифрами от 6 до 10
card_images = []
for suit in ["hearts", "diamonds", "clubs", "spades"]:
    for value in range(6, 11):
        image = pygame.image.load(f"card_game/img/cards/{suit}_{value}.png")
        card_images.append(image)
    
# Загружаем изображения для карт валета, дамы, короля и туза
for suit in ["hearts", "diamonds", "clubs", "spades"]:
    for value in ["jack", "queen", "king", "ace"]:
        image = pygame.image.load(f"card_game/img/cards/{suit}_{value}.png")
        card_images.append(image)

# Классы Card и Deck
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.image = card_images[suit * 13 + value]

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in [0, 1, 2, 3] for value in range(0, 9)]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

# классы игроков и их рук
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = deque()

    def add_card(self, card):
        self.hand.append(card)

    def play_card(self, card):
        self.hand.remove(card)

    def __repr__(self):
        return f"{self.name}: {self.hand}"

# Игроки и их руки
players = [Player(f"Player {i}") for i in range(1, 5)]
deck = Deck()

# Игровая логика
def play_turn(player, deck):
    print(f"{player.name}'s turn: {deck}")
    # Обработка игрового хода
    pass

def main():
    pygame.init()

    # Устанавливаем размеры окна и создаем экран
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("4-Player Crazy Eights")

    # Цвета
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Рисуем карты на доске
    for card in deck.cards:
        screen.blit(card.image, (100 * card.value, 100 * card.suit))

    # Основной цикл игры
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Рисуем игровые руки
        for i, player in enumerate(players):
            for card in player.hand:
                screen.blit(card.image, (100 * i + 50, 100 * 4 + 50))

        # Обработка игрового хода
        # play_turn(players[0], deck)

        pygame.display.flip()

if __name__ == "__main__":
    main()