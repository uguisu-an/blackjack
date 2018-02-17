import tramp.number as nm
import blackjack.point as pt
import blackjack.result as result


def _numbers(hand):
    return [c.number for c in hand]

def sum_of(hand):
    return pt.sum_of_point(_numbers(hand))

def is_blackjack(hand):
    return result.is_blackjack(sum_of(hand))

def is_busted(hand):
    return result.is_busted(sum_of(hand))

def is_double_blackjack(a, b):
    return is_blackjack(a) and is_blackjack(b)