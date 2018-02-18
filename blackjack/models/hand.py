import tramp.number as nm
import blackjack.models.point as pt
import blackjack.models.result as result
from blackjack.models.point import Point


def _numbers(hand):
    return [c.number for c in hand]

def sum_of(hand):
    return Point(_numbers(hand))

def is_blackjack(hand):
    return result.is_blackjack(sum_of(hand))

def is_busted(hand):
    return result.is_busted(sum_of(hand))

def is_double_blackjack(a, b):
    return is_blackjack(a) and is_blackjack(b)