from tramp import Heart
from blackjack.models.card import Card


def test_card_point():
    assert Card(Heart, 1).point == 1
    assert Card(Heart, 11).point == 10