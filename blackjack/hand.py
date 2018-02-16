import blackjack.result as result


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