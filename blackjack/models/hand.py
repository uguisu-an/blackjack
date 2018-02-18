from blackjack.models.point import Point


def _numbers(hand):
    return [c.number for c in hand]

def point(hand):
    return Point(_numbers(hand))