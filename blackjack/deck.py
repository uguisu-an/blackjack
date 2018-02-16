import tramp
import tramp.suit as suit
import tramp.number as number


def generate_deck():
    deck = []
    for suit_ in suit.All:
        for number_ in number.All:
            deck.append(tramp.Card(suit_, number_))
    return deck

def deal(deck, hand):
    return (deck[1:], [deck[0], *hand])
