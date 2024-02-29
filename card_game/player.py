import pygame
from collections import deque
from deck import Deck

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

player = [Player(f"Player {i}") for i in range(1, 5)]
deck = Deck()