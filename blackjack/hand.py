import tramp.number as number
import blackjack.result as result


def point(number_):
    assert number_ in number.All
    if number_ > 10:
        return 10
    return number_

def sum_of_point(hand):
    s = 0
    for c in sorted(hand, reverse=True):
        s += point(c.number)
        if c.number == 1 and not is_busted(s+10):
            s += 10
    return s

def diff(a, b):
    return sum_of_point(a) - sum_of_point(b)

def is_blackjack(point_):
    return point_ == result.BLACKJACK

def is_busted(point_):
    return point_ > result.BLACKJACK


class Hand:
    def __init__(self, hand=[]):
        self._hand = hand
    
    def __lt__(self, other):
        return self.sum_of_points() < other.sum_of_points()
    
    def __gt__(self, other):
        return self.sum_of_points() > other.sum_of_points()
    
    def sum_of_points(self):
        s = 0
        for c in sorted(self, reverse=True):
            p = c.point()
            if s + p[1] > 21:
                s += p[0]
            else:
                s += p[1]
        return s

    def is_busted(self):
        return self.sum_of_points() > result.BLACKJACK

    def is_blackjack(self):
        return self.sum_of_points() == result.BLACKJACK
    
    def __iter__(self):
        return iter(self._hand)