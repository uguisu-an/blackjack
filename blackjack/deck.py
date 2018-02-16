import random
import tramp.suit as suit
import tramp.number as number
from tramp.card import Card
from blackjack.hand import Hand
from blackjack.player import Player


def generate_deck():
    deck = []
    for suit_ in suit.All:
        for number_ in number.All:
            deck.append(Card(suit_, number_))
    return deck

def deal(deck, hand):
    return (deck[1:], [deck[0], *hand])

def shuffled(deck):
    deck_ = deck[:]
    random.shuffle(deck_)
    return deck_


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