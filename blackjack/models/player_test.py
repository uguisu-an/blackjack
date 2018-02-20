from tramp import Heart
from blackjack.models.card import Card
from blackjack.models.player import Player


def test_player_point():
    john = Player(hand=[Card(Heart, 1)])
    jane = Player(hand=[Card(Heart, 1), Card(Heart, 10)])
    assert john.point == 11
    assert jane.point == 21

def test_hitting():
    deck = [1, 2, 3]
    hand = []
    john = Player(deck=deck, hand=hand)
    assert not john.frozen()
    john.hit()
    assert len(deck) == 2
    assert len(hand) == 1
    assert not john.frozen()

def test_standing():
    deck = [1, 2, 3]
    hand = []
    john = Player(deck=deck, hand=hand)
    assert not john.frozen()
    john.stand()
    assert len(deck) == 3
    assert len(hand) == 0
    assert john.frozen()
