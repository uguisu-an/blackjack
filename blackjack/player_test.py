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