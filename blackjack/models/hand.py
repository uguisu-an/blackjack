import tramp.number as nm
import blackjack.models.point as pt
import blackjack.models.result as result
from blackjack.models.point import Point


def _numbers(hand):
    return [c.number for c in hand]

def sum_of(hand):
    return Point(_numbers(hand))
