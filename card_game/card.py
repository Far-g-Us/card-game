import pygame
from . import card_sprite
from . import game_object

class Card(game_object.GameObject):

    def __init__(self, suit, rank, pos, back_up=False):
        game_object.GameObject.__init__(self)
        self.suit = suit
        self.rank = rank
        self.sprite = card_sprite.CardSprite(suit, rank, pos, back_up)
        self.back_up = back_up

    def get_sprite(self):
        return self.sprite

    def render(self, screen):
        self.sprite.render(screen)

    def flip(self):
        self.back_up = not self.back_up
        self.sprite.flip()

    def is_clicked(self, pos):
        return self.sprite.is_clicked(pos)

    def unclick(self):
        self.sprite.clicked = False

    def check_mouse(self, pos, down):
        return self.sprite.check_mouse(pos, down)

    def check_collide(self, card_=None, pos=None):
        if card_ is not None:
            return self.sprite.check_card_collide(card_.sprite)
        elif pos is not None:
            return self.sprite.check_area_collide(pos)

    def set_pos(self, pos):
        self.sprite.pos = pos

    def offset_pos(self, pos):
        self.sprite_pos(pos)