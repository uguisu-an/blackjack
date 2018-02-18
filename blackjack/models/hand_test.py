from tramp import Card, Heart
import blackjack.models.hand as hd
import blackjack.models.point as pt
import blackjack.models.result as rs


def test_hand_point():
    hand = [Card(Heart, 1), Card(Heart, 10)]
    assert hd.point(hand) == 21
