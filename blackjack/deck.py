import random


class Deck:
    def __init__(self):
        deck = []
        for x in range(4):
            for y in range(13):
                deck = [(x, y), *deck]
        self._deck = deck
    
    def deal(self, hand):
        card = self._deck.pop()
        return [card, *hand]
    
    def shuffle(self):
        random.shuffle(self._deck)