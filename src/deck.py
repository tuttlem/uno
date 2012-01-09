
from random import shuffle

from card import Card

class Deck(object):

    '''Manages multiple cards in a shoe for the game'''

    def __init__(self):
        self.cards = list()

    def prepare(self, count):
        self.cards = list()

        for multiples in range(count):
            for value in range(13, 15):
                self.cards.append(Card(value, 0))

            for value in range(13):
                for colour in range(1, 5):
                    self.cards.append(Card(value, colour))

        shuffle(self.cards)

    def refill(self, stack):
        self.cards = [card for card in stack]
        shuffle(self.cards)

    def next_card(self):
        return self.cards.pop()

    def has_cards(self):
        return len(self.cards) > 0

