import tramp
from blackjack.models.card import Card


def generate_deck():
    deck = []
    for suit in tramp.suit.All:
        for number in tramp.number.All:
            deck.append(Card(suit, number))
    return deck

def deal(deck, hand):
    return (deck[1:], [deck[0], *hand])

Deck = generate_deck
