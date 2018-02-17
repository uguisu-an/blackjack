from tramp import Card, Heart
from blackjack.player import Player


def test_player_is_blackjack():
    john = Player()
    assert not john.is_blackjack()
    john.hand = [Card(Heart, 13), Card(Heart, 1)]
    assert john.is_blackjack()

def test_player_is_busted():
    john = Player()
    john.hand = [Card(Heart, 13), Card(Heart, 1)]
    assert not john.is_busted()
    john.hand.append(Card(Heart, 1))
    assert john.is_busted()

def test_player_point():
    john = Player(hand=[Card(Heart, 1)])
    assert john.point == 11

def test_hitting():
    deck = [1, 2, 3]
    hand = []
    john = Player(deck, hand)
    assert not john.is_stand()
    john.hit()
    assert len(deck) == 2
    assert len(hand) == 1
    assert not john.is_stand()

def test_standing():
    deck = [1, 2, 3]
    hand = []
    john = Player(deck, hand)
    assert not john.is_stand()
    john.stand()
    assert len(deck) == 3
    assert len(hand) == 0
    assert john.is_stand()
