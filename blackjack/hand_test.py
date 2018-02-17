from tramp import Card, Heart
import blackjack.hand as hd
import blackjack.point as pt
import blackjack.result as rs


def test_point():
    assert pt.point(10) == 10
    assert pt.point(11) == 10

def test_sum_of_point():
    assert pt.sum_of_point([2, 3, 4, 5, 6, 7, 8, 9]) == 44

def test_sum_of_point_with_one():
    assert pt.sum_of_point([1, 10]) == 21
    assert pt.sum_of_point([1, 10, 10]) == 21

def test_sum_of_point_with_picture_card():
    assert pt.sum_of_point([11, 12, 13]) == 30

def test_sum_of_point_without_card():
    assert pt.sum_of_point([]) == 0

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
