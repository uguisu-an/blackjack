import random
import tramp.suit as st
import blackjack.card as cr
from blackjack.hand import Hand
from blackjack.player import Player


class Deck:
    def __init__(self):
        deck = []
        for suit in st.All:
            for number in range(1, 13+1):
                deck = [cr.Card(suit, number), *deck]
        self._deck = deck
    
    def deal(self, hand):
        card = self._deck.pop()
        return Hand([card, *hand])
    
    def shuffle(self):
        random.shuffle(self._deck)