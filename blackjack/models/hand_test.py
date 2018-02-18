from tramp import Card, Heart
import blackjack.models.hand as hd
import blackjack.models.point as pt
import blackjack.models.result as rs


def test_sum_of_hand():
    hand = [Card(Heart, 1), Card(Heart, 10)]
    assert hd.sum_of(hand) == 21
    assert hd.is_blackjack(hand)
    assert hd.is_double_blackjack(hand, hand)
    assert not hd.is_busted(hand)

def test_blackjack():
    assert not rs.is_blackjack(20)
    assert rs.is_blackjack(21)

def test_bust():
    assert not rs.is_busted(21)
    assert rs.is_busted(22)
