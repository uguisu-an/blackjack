from tramp import Card, Heart
import blackjack.models.hand as hd
import blackjack.models.point as pt
import blackjack.models.result as rs


def test_sum_of_hand():
    hand = [Card(Heart, 1), Card(Heart, 10)]
    assert hd.sum_of(hand) == 21
